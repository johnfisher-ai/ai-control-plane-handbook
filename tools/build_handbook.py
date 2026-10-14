#!/usr/bin/env python3
"""Convert the public edition of The AI Control Plane Handbook (Word) into the site's handbook pages.

Usage:
    python3 tools/build_handbook.py <public-handbook.docx> [repository root]

Reads only the public edition (JRF_AI_Control_Plane_Handbook_Executive_Public.docx). Writes:
    handbook/index.html            introduction and contents
    handbook/executive-summary.html
    handbook/section-01.html ... section-13.html
    handbook/appendix-a.html ... appendix-e.html
    handbook/img/figure-01.png ... figure-22.png
and rewrites sitemap.xml. The Word file itself is never copied into the repository.

The converter relies on the handbook's structure: a small uppercase kicker ("SECTION 4", "APPENDIX") and a
Heading 1 start each page; Heading 2 and bold 11.5-point paragraphs are subheadings; one-cell shaded tables are
callout boxes; a picture paragraph is followed by its "Figure N." caption; Appendix B holds the numbered endnotes.
Superscript numbers become links to the endnotes, and "Section N", "Figure N" and "Appendix X" become links.
Requires Python 3.9+ and lxml.
"""
import html, os, re, shutil, struct, sys, zipfile
from lxml import etree

SITE = 'https://johnfisher-ai.github.io/ai-control-plane-handbook/'
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
WP = '{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
PKG = '{http://schemas.openxmlformats.org/package/2006/relationships}'
esc = lambda s: html.escape(s, quote=True)

DISCLOSURE = ('John Fisher works for Salesforce. The views here are his own, not Salesforce’s, and are drawn from '
              'public information; this handbook is not affiliated with or endorsed by Salesforce.')


# ---------------------------------------------------------------------------------------------------------- reading
class Doc:
    def __init__(self, path):
        z = zipfile.ZipFile(path)
        self.z = z
        self.root = etree.fromstring(z.read('word/document.xml'))
        rels = etree.fromstring(z.read('word/_rels/document.xml.rels'))
        self.rels = {r.get('Id'): r.get('Target') for r in rels.iter(PKG + 'Relationship')}
        self.numfmt = {}
        if 'word/numbering.xml' in z.namelist():
            n = etree.fromstring(z.read('word/numbering.xml'))
            absfmt = {}
            for a in n.findall(W + 'abstractNum'):
                lv = a.find(W + 'lvl')
                absfmt[a.get(W + 'abstractNumId')] = lv.find(W + 'numFmt').get(W + 'val')
            for num in n.findall(W + 'num'):
                self.numfmt[num.get(W + 'numId')] = absfmt.get(num.find(W + 'abstractNumId').get(W + 'val'), 'bullet')


def rpr_flags(r):
    rpr = r.find(W + 'rPr')
    f = {'b': False, 'i': False, 'sup': False, 'color': None, 'sz': None}
    if rpr is None:
        return f
    b = rpr.find(W + 'b')
    f['b'] = b is not None and b.get(W + 'val') not in ('0', 'false')
    i = rpr.find(W + 'i')
    f['i'] = i is not None and i.get(W + 'val') not in ('0', 'false')
    va = rpr.find(W + 'vertAlign')
    f['sup'] = va is not None and va.get(W + 'val') == 'superscript'
    c = rpr.find(W + 'color')
    f['color'] = c.get(W + 'val').upper() if c is not None else None
    s = rpr.find(W + 'sz')
    f['sz'] = s.get(W + 'val') if s is not None else None
    return f


def segments(doc, p):
    """[(text, bold, italic, sup, href)] for a paragraph, adjacent equal formats merged."""
    out = []

    def add(text, f, href):
        if not text:
            return
        key = (f['b'], f['i'], f['sup'], href)
        if out and out[-1][1:] == key:
            out[-1] = (out[-1][0] + text,) + key
        else:
            out.append((text,) + key)

    def walk(el, href):
        for c in el:
            if c.tag == W + 'r':
                f = rpr_flags(c)
                for k in c:
                    if k.tag == W + 't':
                        add(k.text or '', f, href)
                    elif k.tag == W + 'tab':
                        add('\t', f, href)
                    elif k.tag == W + 'br' and k.get(W + 'type') not in ('page', 'column'):
                        add('\n', f, href)
            elif c.tag == W + 'hyperlink':
                url = doc.rels.get(c.get(R + 'id')) if c.get(R + 'id') else None
                walk(c, url or href)
            elif c.tag in (W + 'ins', W + 'smartTag', W + 'sdt', W + 'sdtContent', W + 'fldSimple'):
                walk(c, href)
    walk(p, None)
    return out


def ptext(doc, p):
    return ''.join(s[0] for s in segments(doc, p))


def pstyle(p):
    s = p.find(W + 'pPr/' + W + 'pStyle')
    return s.get(W + 'val') if s is not None else ''


def first_run_flags(p):
    for r in p.iter(W + 'r'):
        if ''.join(t.text or '' for t in r.iter(W + 't')).strip():
            return rpr_flags(r)
    return rpr_flags(etree.Element(W + 'r'))


def numinfo(p):
    n = p.find(W + 'pPr/' + W + 'numPr')
    if n is None:
        return None
    nid = n.find(W + 'numId')
    lvl = n.find(W + 'ilvl')
    return (nid.get(W + 'val') if nid is not None else '0', int(lvl.get(W + 'val')) if lvl is not None else 0)


def picture(doc, p):
    for d in p.iter(WP + 'inline', WP + 'anchor'):
        pr = d.find(WP + 'docPr')
        blip = d.find('.//' + A + 'blip')
        if blip is not None:
            return {'target': doc.rels[blip.get(R + 'embed')], 'alt': (pr.get('descr') or pr.get('title') or '').strip()}
    return None


# ---------------------------------------------------------------------------------------------------------- blocks
def classify(doc, p):
    text = ptext(doc, p)
    st = pstyle(p)
    f = first_run_flags(p)
    pic = picture(doc, p)
    if pic:
        return ('picture', pic)
    if not text.strip():
        return ('empty', None)
    if st == 'Heading1':
        return ('h1', text.strip())
    if st == 'Heading2':
        return ('h2', text.strip())
    if f['b'] and f['color'] == '0284C7' and f['sz'] == '18' and text.strip().isupper():
        return ('kicker', text.strip())
    if f['b'] and f['color'] == '0F172A' and f['sz'] == '23':
        return ('h3', text.strip())
    if f['color'] == '475569' and re.match(r'Figure \d+\.', text.strip()):
        return ('caption', p)
    if numinfo(p):
        return ('li', p)
    return ('p', p)


def parse_pages(doc):
    """Split the body into pages: [{kicker, title, blocks}] (cover blocks dropped)."""
    body = doc.root.find(W + 'body')
    pages, cur, kicker = [], None, None
    for el in body:
        if el.tag == W + 'p':
            kind, val = classify(doc, el)
            if kind == 'kicker':
                kicker = val
                continue
            if kind == 'h1':
                cur = {'kicker': kicker or '', 'title': val, 'blocks': []}
                pages.append(cur)
                kicker = None
                continue
            if cur is None or kind == 'empty':
                continue
            cur['blocks'].append((kind, val if kind not in ('p', 'li', 'caption') else el))
        elif el.tag == W + 'tbl' and cur is not None:
            cur['blocks'].append(('table', el))
    return pages


# ---------------------------------------------------------------------------------------------------------- site map
def page_files(pages):
    """Assign file names and labels in reading order."""
    for pg in pages:
        k, t = pg['kicker'].upper(), pg['title']
        m = re.match(r'SECTION (\d+)', k)
        ma = re.match(r'Appendix ([A-E])\.\s*(.*)', t)
        if k == 'INTRODUCTION':
            pg.update(file='index.html', label='About this handbook', short='Introduction', key='intro')
        elif t.lower().startswith('executive summary'):
            pg.update(file='executive-summary.html', label='Executive summary', short='Executive summary', key='exec')
        elif m:
            n = int(m.group(1))
            pg.update(file=f'section-{n:02d}.html', label=t, short=f'Section {n}', key=f'S{n}', num=str(n))
        elif ma:
            L = ma.group(1)
            pg.update(file=f'appendix-{L.lower()}.html', label=ma.group(2), short=f'Appendix {L}', key=f'A{L}', num=L)
        else:
            raise SystemExit(f'unrecognized page: {k!r} {t!r}')
    return pages


# ---------------------------------------------------------------------------------------------------------- rendering
class Renderer:
    def __init__(self, doc, pages, outdir):
        self.doc, self.pages, self.out = doc, pages, outdir
        self.byk = {p['key']: p for p in pages}
        self.cites = {}          # endnote -> [(page file, anchor id, page short)]
        self.cite_seq = 0
        self.figures = {}        # figure number -> page file
        self.images = []         # (source in docx, dest name)
        self.cur = None
        self.ids = set()

    # --- ids
    def uid(self, base):
        base = re.sub(r'[^a-z0-9]+', '-', base.lower()).strip('-')[:60] or 'part'
        u, k = base, 2
        while u in self.ids:
            u, k = f'{base}-{k}', k + 1
        self.ids.add(u)
        return u

    # --- inline
    def cite_html(self, text):
        out = []
        for tok in re.split(r'(\d+)', text):
            if tok.isdigit():
                n = int(tok)
                self.cite_seq += 1
                aid = f'cite-{n}-{self.cite_seq}'
                self.cites.setdefault(n, []).append((self.cur['file'], aid, self.cur['short']))
                href = ('' if self.cur['file'] == 'appendix-b.html' else 'appendix-b.html') + f'#en-{n}'
                out.append(f'<a href="{href}" id="{aid}" aria-label="Endnote {n}">{n}</a>')
            elif tok:
                out.append(esc(tok))
        return '<sup class="cite">' + ''.join(out) + '</sup>'

    XREF = re.compile(r'\b(Sections?|Figures?|Appendix|Appendices)\s+((?:\d+|[A-E])(?:(?:\s*(?:,|and|to|or|–)\s*)(?:\d+|[A-E]))*)\b')

    def link_xrefs(self, s_escaped):
        def target(kind, tok):
            if kind.startswith('Section') and tok.isdigit() and 1 <= int(tok) <= 13:
                f = self.byk[f'S{int(tok)}']['file']
                return None if f == self.cur['file'] else f
            if kind.startswith('Append') and len(tok) == 1 and tok in 'ABCDE':
                f = self.byk[f'A{tok}']['file']
                return None if f == self.cur['file'] else f
            if kind.startswith('Figure') and tok.isdigit() and int(tok) in self.figures:
                f = self.figures[int(tok)]
                return ('' if f == self.cur['file'] else f) + f'#figure-{int(tok)}'
            return None

        def rep(m):
            kind, lst = m.group(1), m.group(2)
            out, first = [], True
            for t in re.split(r'(\d+|[A-E])', lst):
                if re.fullmatch(r'\d+|[A-E]', t):
                    label = f'{kind} {t}' if first else t
                    tgt = target(kind, t)
                    out.append(f'<a href="{tgt}">{label}</a>' if tgt else label)
                    first = False
                else:
                    out.append(t)
            return ''.join(out)
        return self.XREF.sub(rep, s_escaped)

    def inline(self, segs, xref=True, strip_lead=None):
        out = []
        for text, b, i, sup, href in segs:
            if sup and re.fullmatch(r'[\d,–\- ]+', text.strip() or 'x'):
                out.append(self.cite_html(text.strip()))
                continue
            t = esc(text).replace('\t', ' ').replace('\n', '<br>')
            if xref and not href and not sup:
                t = self.link_xrefs(t)
            if sup:
                t = f'<sup>{t}</sup>'
            if i:
                t = f'<em>{t}</em>'
            if b:
                t = f'<strong>{t}</strong>'
            if href:
                t = f'<a href="{esc(href)}">{t}</a>'
            out.append(t)
        s = ''.join(out)
        s = re.sub(r'</strong><strong>', '', s)
        return s.strip()

    # --- blocks
    def para(self, p, cls=None):
        segs = segments(self.doc, p)
        c = f' class="{cls}"' if cls else ''
        return f'<p{c}>{self.inline(segs)}</p>'

    def render_blocks(self, blocks, toc=None, in_callout=False):
        html_out, i = [], 0
        while i < len(blocks):
            kind, val = blocks[i]
            if kind == 'h2':
                hid = self.uid(val)
                if toc is not None:
                    toc.append((hid, val))
                html_out.append(f'<h2 id="{hid}">{esc(val)}</h2>')
            elif kind == 'h3':
                html_out.append(f'<h3 id="{self.uid(val)}">{esc(val)}</h3>')
            elif kind == 'p':
                html_out.append(self.para(val))
            elif kind == 'li':
                nid, lvl = numinfo(val)
                fmt = self.doc.numfmt.get(nid, 'bullet')
                items = []
                while i < len(blocks) and blocks[i][0] == 'li' and numinfo(blocks[i][1])[0] == nid:
                    items.append(f'<li>{self.inline(segments(self.doc, blocks[i][1]))}</li>')
                    i += 1
                tag = 'ol' if fmt == 'decimal' else 'ul'
                html_out.append(f'<{tag}>' + ''.join(items) + f'</{tag}>')
                continue
            elif kind == 'picture':
                cap = None
                if i + 1 < len(blocks) and blocks[i + 1][0] == 'caption':
                    cap = blocks[i + 1][1]
                html_out.append(self.figure(val, cap))
                i += 2 if cap is not None else 1
                continue
            elif kind == 'caption':
                html_out.append(self.para(val, 'caption'))
            elif kind == 'table':
                html_out.append(self.table(val, toc))
            i += 1
        return '\n'.join(html_out)

    def figure(self, pic, cap):
        capsegs = segments(self.doc, cap) if cap is not None else []
        captext = ''.join(s[0] for s in capsegs)
        m = re.match(r'Figure (\d+)\.', captext)
        n = int(m.group(1)) if m else len(self.images) + 1
        name = f'figure-{n:02d}.png'
        self.images.append((pic['target'], name))
        data = self.doc.z.read('word/' + pic['target'])
        w, h = struct.unpack('>II', data[16:24]) if data[:8] == b'\x89PNG\r\n\x1a\n' else (0, 0)
        dims = f' width="{w}" height="{h}"' if w else ''
        caphtml = ''
        if capsegs:
            caphtml = f'<figcaption>{self.inline(capsegs, xref=False)}</figcaption>'
        return (f'<figure id="figure-{n}">'
                f'<img src="img/{name}" alt="{esc(pic["alt"])}"{dims} loading="lazy" decoding="async">'
                f'{caphtml}</figure>')

    def cell_blocks(self, tc):
        blocks = []
        for el in tc:
            if el.tag == W + 'p':
                kind, val = classify(self.doc, el)
                if kind == 'empty':
                    continue
                if kind in ('h1', 'h2', 'h3', 'kicker'):
                    blocks.append(('p', el))
                else:
                    blocks.append((kind, val if kind not in ('p', 'li', 'caption') else el))
            elif el.tag == W + 'tbl':
                blocks.append(('table', el))
        return blocks

    def table(self, tbl, toc):
        rows = tbl.findall(W + 'tr')
        first = rows[0].findall(W + 'tc')
        fill = lambda tc: (tc.find(W + 'tcPr/' + W + 'shd').get(W + 'fill') or '').upper() if tc.find(W + 'tcPr/' + W + 'shd') is not None else ''
        # one-cell shaded table: a callout box
        if len(rows) == 1 and len(first) == 1:
            blocks = self.cell_blocks(first[0])
            title = ''
            if blocks and blocks[0][0] == 'p':
                segs = segments(self.doc, blocks[0][1])
                if segs and all(s[1] for s in segs if s[0].strip()):
                    title = ''.join(s[0] for s in segs).strip()
                    blocks = blocks[1:]
            hid = self.uid(title) if title else None
            if title and toc is not None:
                toc.append((hid, title))
            head = f'<h2 id="{hid}">{esc(title)}</h2>' if title else ''
            labelled = f' aria-labelledby="{hid}"' if hid else ''
            return f'<aside class="callout-box"{labelled}>{head}{self.render_blocks(blocks, None, True)}</aside>'
        header = fill(first[0]) == '0F172A'
        endnote_col = False
        out = ['<div class="table-wrap" role="region" tabindex="0" aria-label="Table">', '<table>']
        body_rows = rows
        if header:
            ths, plain = [], []
            for tc in first:
                ps = [p for p in tc.findall(W + 'p') if ptext(self.doc, p).strip()]
                cell = ' '.join(self.inline(segments(self.doc, p)) for p in ps)
                ths.append('<th scope="col">' + re.sub(r'</?strong>', '', cell) + '</th>')
                plain.append(' '.join(ptext(self.doc, p).strip() for p in ps))
            out.append('<thead><tr>' + ''.join(ths) + '</tr></thead>')
            body_rows = rows[1:]
            out[0] = f'<div class="table-wrap" role="region" tabindex="0" aria-label="Table: {esc(", ".join(plain)[:90])}">'
            endnote_col = plain and plain[0] == 'Endnote'
        out.append('<tbody>')
        for tr in body_rows:
            tds = []
            for ci, tc in enumerate(tr.findall(W + 'tc')):
                span = tc.find(W + 'tcPr/' + W + 'gridSpan')
                cs = f' colspan="{span.get(W + "val")}"' if span is not None else ''
                blocks = self.cell_blocks(tc)
                if endnote_col and ci == 0:
                    raw = ' '.join(ptext(self.doc, q) for q in tc.findall(W + 'p')).strip()
                    inner = re.sub(r'\d+', lambda m: f'<a href="appendix-b.html#en-{m.group(0)}">{m.group(0)}</a>', esc(raw))
                elif len(blocks) == 1 and blocks[0][0] == 'p':
                    inner = self.inline(segments(self.doc, blocks[0][1]))
                else:
                    inner = self.render_blocks(blocks)
                tds.append(f'<td{cs}>{inner}</td>')
            out.append('<tr>' + ''.join(tds) + '</tr>')
        out.append('</tbody></table></div>')
        return ''.join(out)

    # --- endnotes (Appendix B)
    def endnotes_list(self, blocks):
        intro, items = [], []
        for kind, val in blocks:
            if kind != 'p':
                continue
            segs = segments(self.doc, val)
            text = ''.join(x[0] for x in segs)
            m = re.match(r'(\d+)\.\t', text)
            if not m:
                intro.append(self.para(val, 'lede'))
                continue
            n, cut, body, links = int(m.group(1)), len(m.group(0)), [], []
            for seg in segs:
                t = seg[0]
                if cut:
                    drop = min(cut, len(t))
                    t, cut = t[drop:], cut - drop
                if not t:
                    continue
                if seg[4]:
                    links.append(seg[4])
                else:
                    body.append((t,) + seg[1:])
            body_html = self.inline(body, xref=False).strip()
            link_html = ' '.join(f'<a class="url" href="{esc(u)}">{esc(u)}</a>' for u in dict.fromkeys(links))
            items.append((n, body_html, link_html))
        return intro, items

    # --- page assembly
    def nav_list(self, current):
        rows = []
        for pg in self.pages:
            cur = ' aria-current="page"' if pg is current else ''
            num = pg.get('num', '')
            numhtml = f'<span class="n">{num}</span>' if num else '<span class="n" aria-hidden="true">•</span>'
            sub = ''
            if pg is current and current.get('toc'):
                sub = '<ol class="onpage">' + ''.join(f'<li><a href="#{h}">{esc(t)}</a></li>' for h, t in current['toc']) + '</ol>'
            label = 'Contents and introduction' if pg['key'] == 'intro' else pg['label']
            rows.append(f'<li><a href="{pg["file"]}"{cur}>{numhtml}<span>{esc(label)}</span></a>{sub}</li>')
        return '<ol class="doc-toc">' + ''.join(rows) + '</ol>'

    @staticmethod
    def full_title(pg):
        if pg['key'] == 'intro':
            return 'Contents'
        if pg['key'] == 'exec':
            return 'Executive summary'
        return f"{pg['short']}. {pg['label']}"

    def page_html(self, pg, main_html, idx):
        prev_pg = self.pages[idx - 1] if idx > 0 else None
        next_pg = self.pages[idx + 1] if idx + 1 < len(self.pages) else None
        title = self.full_title(pg)
        head_title = f'{title} · The AI Control Plane Handbook'
        desc = pg.get('desc', '')
        canon = SITE + 'handbook/' + ('' if pg['file'] == 'index.html' else pg['file'])
        pn = []
        for p2, cls, word, rel in ((prev_pg, 'prev', 'Previous', 'prev'), (next_pg, 'next', 'Next', 'next')):
            if p2:
                pn.append(f'<a class="pn {cls}" href="{p2["file"]}" rel="{rel}"><span class="pn-dir">{word}</span>'
                          f'<span class="pn-title">{esc(self.full_title(p2))}</span></a>')
            else:
                pn.append('<span></span>')
        crumbs = ('<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="../index.html">Home</a></li>'
                  + ('<li><a href="index.html">Handbook</a></li>' if pg['key'] != 'intro' else '')
                  + f'<li><span aria-current="page">{esc(pg["short"] if pg["key"] != "intro" else "Handbook")}</span></li></ol></nav>')
        kicker = {'intro': 'Executive Edition · 2026', 'exec': 'Overview'}.get(pg['key'], pg['short'])
        return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(head_title)}</title>
  <meta name="description" content="{esc(desc)}">
  <meta name="author" content="John Fisher">
  <meta name="color-scheme" content="light dark">
  <meta name="theme-color" content="#0F172A">
  <link rel="canonical" href="{canon}">
  <link rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">
  <link rel="icon" href="../assets/img/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="../assets/img/favicon-32.png" sizes="32x32" type="image/png">
  <link rel="apple-touch-icon" href="../assets/img/apple-touch-icon.png">
  <link rel="preload" href="../assets/fonts/plus-jakarta-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="../assets/css/site.css">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="The AI Control Plane Handbook">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="{canon}">
  <meta property="og:image" content="{SITE}assets/img/social-card.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="The AI Control Plane Handbook, by John Fisher, 2026 edition">
  <meta name="twitter:card" content="summary_large_image">
</head>
<body class="doc-page">
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="wrap">
      <a class="brand" href="../index.html">
        <svg viewBox="0 0 32 32" aria-hidden="true" focusable="false"><rect width="32" height="32" rx="7" fill="#1E293B"/><g stroke="#64748B" stroke-width="1.6"><line x1="9" y1="9" x2="19" y2="15"/><line x1="8" y1="23" x2="19" y2="15"/><line x1="25" y1="25" x2="19" y2="15"/><line x1="24" y1="7" x2="19" y2="15"/></g><g fill="#0F172A" stroke="#94A3B8" stroke-width="1.4"><circle cx="9" cy="9" r="2.6"/><circle cx="8" cy="23" r="2.6"/><circle cx="25" cy="25" r="2.6"/><circle cx="24" cy="7" r="2.6"/></g><circle cx="19" cy="15" r="4.6" fill="#38BDF8"/></svg>
        <span>The AI Control Plane Handbook</span>
      </a>
      <nav class="site-nav" aria-label="Main">
        <ul>
          <li><a href="index.html">Contents</a></li>
          <li><a href="appendix-b.html">Endnotes</a></li>
          <li><a href="appendix-e.html">About the author</a></li>
        </ul>
      </nav>
    </div>
  </header>
  <div class="wrap doc-layout">
    <details class="doc-nav" id="doc-nav">
      <summary>Contents</summary>
      <nav aria-label="Handbook contents">
        {self.nav_list(pg)}
      </nav>
    </details>
    <main id="main" class="doc-main">
      {crumbs}
      <p class="doc-kicker">{esc(kicker)}</p>
      <h1>{esc('The AI Control Plane Handbook' if pg['key'] == 'intro' else pg['label'])}</h1>
{main_html}
      <nav class="pager" aria-label="Previous and next">{''.join(pn)}</nav>
    </main>
  </div>
  <footer class="site-footer">
    <div class="wrap">
      <p>© 2026 John Fisher · <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/">CC BY-NC-ND 4.0</a> · <a href="appendix-d.html">Notices</a> · <a href="https://github.com/johnfisher-ai/ai-control-plane-handbook">Source on GitHub</a> · <a href="https://www.linkedin.com/in/johnrfisher">LinkedIn</a></p>
      <p class="small">{esc(DISCLOSURE)} Product names are trademarks of their owners; Appendix D lists them. Set in Plus Jakarta Sans, licensed under the SIL Open Font License 1.1.</p>
    </div>
  </footer>
  <script>
    (function () {{ var d = document.getElementById('doc-nav'); var m = window.matchMedia('(min-width: 1000px)'); function s() {{ d.open = m.matches; }} s(); m.addEventListener ? m.addEventListener('change', s) : m.addListener(s); var c = d.querySelector('[aria-current="page"]'); if (c && m.matches) {{ d.scrollTop = Math.max(0, c.offsetTop - d.clientHeight / 3); }} }})();
  </script>
</body>
</html>
'''

    def build(self):
        # figures first (cross-references need the figure -> page map)
        for pg in self.pages:
            for kind, val in pg['blocks']:
                if kind == 'caption':
                    m = re.match(r'Figure (\d+)\.', ptext(self.doc, val))
                    if m:
                        self.figures[int(m.group(1))] = pg['file']
        bodies = {}
        endnote_page = None
        for pg in self.pages:
            self.cur, self.ids, pg['toc'] = pg, set(), []
            first_p = next((ptext(self.doc, v) for k, v in pg['blocks'] if k == 'p'), '')
            pg['desc'] = re.sub(r'\s+', ' ', first_p).strip()
            if len(pg['desc']) > 158:
                pg['desc'] = pg['desc'][:155].rsplit(' ', 1)[0] + '…'
            if pg['key'] == 'intro':
                # drop the Word contents list ("In this handbook" and its lines); the site generates its own
                blocks, skip = [], False
                for kind, val in pg['blocks']:
                    if kind == 'h2' and val.lower().startswith('in this handbook'):
                        skip = True
                        continue
                    if not skip:
                        blocks.append((kind, val))
                parts = []
                for kind, val in blocks:
                    t = ptext(self.doc, val) if kind == 'p' else ''
                    if t.startswith('Disclosure.'):
                        parts.append(self.para(val, 'callout'))
                    else:
                        parts.append(self.render_blocks([(kind, val)], pg['toc']))
                pg['desc'] = ('A vendor-neutral handbook for CTOs and CIOs on the enterprise AI control plane: architecture, '
                              'orchestration, trust and security, a north-star reference architecture, and a 12- to 24-month plan.')
                contents = ['<h2 id="contents">Contents</h2>', '<ol class="contents-list">']
                for p2 in self.pages[1:]:
                    num = p2.get('num', '')
                    contents.append(f'<li><a href="{p2["file"]}"><span class="n">{num or "•"}</span><span>{esc(p2["label"])}</span></a></li>')
                contents.append('</ol>')
                pg['toc'].append(('contents', 'Contents'))
                byline = ('<p class="doc-sub">Architecture, orchestration, and zero-trust security for the agentic enterprise</p>'
                          '<p class="doc-byline">John Fisher · 2026</p>')
                pg['toc'].insert(0, ('about', 'About this handbook'))
                bodies[pg['file']] = (byline + '\n<h2 id="about">About this handbook</h2>\n' + '\n'.join(parts) + '\n'
                                      + '\n'.join(contents))
            elif pg['key'] == 'AB':
                endnote_page = pg
                bodies[pg['file']] = None
            else:
                bodies[pg['file']] = self.render_blocks(pg['blocks'], pg['toc'])
        # endnotes last, with "cited in" back-links
        self.cur, self.ids = endnote_page, set()
        intro, items = self.endnotes_list(endnote_page['blocks'])
        li = []
        for n, body_html, link_html in items:
            seen, back = set(), []
            for f, aid, short in self.cites.get(n, []):
                if f in seen:
                    continue
                seen.add(f)
                back.append(f'<a href="{f}#{aid}">{esc(short)}</a>')
            cited = f'<span class="cited">Cited in {", ".join(back)}</span>' if back else ''
            li.append(f'<li id="en-{n}" value="{n}">{body_html}{(" " + link_html) if link_html else ""}{cited}</li>')
        bodies[endnote_page['file']] = '\n'.join(intro) + '\n<ol class="endnotes">' + '\n'.join(li) + '</ol>'
        endnote_page['desc'] = 'The 107 sources cited in The AI Control Plane Handbook, numbered in order of first citation, with links.'
        self.endnote_numbers = [n for n, _, _ in items]
        # write
        os.makedirs(os.path.join(self.out, 'img'), exist_ok=True)
        for idx, pg in enumerate(self.pages):
            html_text = self.page_html(pg, bodies[pg['file']], idx)
            with open(os.path.join(self.out, pg['file']), 'w', encoding='utf-8') as fh:
                fh.write(html_text)
        for src, name in self.images:
            with open(os.path.join(self.out, 'img', name), 'wb') as fh:
                fh.write(self.doc.z.read('word/' + src))


def write_sitemap(root, pages):
    urls = [SITE] + [SITE + 'handbook/' + ('' if p['file'] == 'index.html' else p['file']) for p in pages]
    with open(os.path.join(root, 'sitemap.xml'), 'w', encoding='utf-8') as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for u in urls:
            fh.write(f'  <url>\n    <loc>{u}</loc>\n  </url>\n')
        fh.write('</urlset>\n')


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    src = sys.argv[1]
    root = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    outdir = os.path.join(root, 'handbook')
    if os.path.isdir(outdir):
        for f in os.listdir(outdir):
            if f.endswith('.html'):
                os.remove(os.path.join(outdir, f))
        if os.path.isdir(os.path.join(outdir, 'img')):
            shutil.rmtree(os.path.join(outdir, 'img'))
    doc = Doc(src)
    pages = page_files(parse_pages(doc))
    rd = Renderer(doc, pages, outdir)
    rd.build()
    write_sitemap(root, pages)
    cited = set(rd.cites)
    listed = set(rd.endnote_numbers)
    print(f'pages: {len(pages)}; figures: {len(rd.images)}; endnotes listed: {len(listed)}; '
          f'citations: {sum(len(v) for v in rd.cites.values())} to {len(cited)} endnotes')
    if cited - listed:
        print('!! cited but not listed:', sorted(cited - listed))
    if listed - cited:
        print('!! listed but never cited:', sorted(listed - cited))


if __name__ == '__main__':
    main()
