# Rebuild kit for the site downloads (October 15, 2026)

> Note added October 19, 2026, for Claude Code sessions. Sections 1 and 3 describe the old Cowork route, with archives unpacked into the clone on John's Mac and pushes from GitHub Desktop. The three sections at the end (Set up a fresh cloud workspace, Naming scan, Deliver through GitHub) replace them and win wherever an older passage differs. Where section 4 says the desktop app's browser, John's own browser does the same job.

**Standing rule (John, October 15, 2026):** keep the downloads, and the search index, in sync with the HTML pages. The pages are the master. When a change touches an executive deck slide (its text, title or speaker notes), update that slide's one-slide PowerPoint file and its image in the same change. When a change touches a toolkit template (Sections 7 and 8, T1 to T13, the Part 3 introduction, the notices or About, a cited endnote, or a figure on those pages), rebuild the Word download. When a change touches the text of any page, rebuild the search index. Every change summary says which downloads were updated, or that none were affected.

The kit is one Python file, `rebuild_kit.py` (October 15, 2026, third version, with the site search index; 72,147 bytes; MD5 `3277bcdb851c19ead681a9a164a03c00`). It reads only the site's own files, so it works in any session that has a copy of the repository.

- **Runnable copy:** attached to John's private artifact **Site Rebuild Kit**, https://claude.ai/artifact/V2Swna2EiqsdyyJkYGowix (the page itself is this README in readable form).
- **Readable backup:** `claude/Rebuild kit/rebuild_kit.py` in this project. Project docs come back as inline text, so use this copy for reading, not for running.

| Download | Made from |
|---|---|
| `deck/slides/the-ai-control-plane-slide-01.pptx` to `-58.pptx` | These files are the editable form of each slide (there is no full deck to rebuild from). The speaker notes, the credit line and the file title come from the deck pages. |
| `deck/img/slide-01.png` to `-58.png` | Renders of those files: LibreOffice, 120 dpi (1601 × 900), 256 colours, Plus Jakarta Sans from the site's own fonts. |
| `pagefind/` | The site search: Pagefind 1.4.0 (pinned in the kit as `PAGEFIND`) indexes the `<main>` of every page that carries `data-pagefind-body`, with the result title from the page's `pagefind:title` meta and a Publication filter. The build is deterministic, so `check` rebuilds it and compares. |
| `toolkit/downloads/ai-control-plane-assessment-templates.docx` | `toolkit/section-07.html` (Part 1), `section-08.html` (Part 2), the first paragraph of `part-3.html` (the Part 2 introduction), `appendix-e.html` (notices, with three wording swaps), `appendix-f.html` (About), the entries in `handbook/appendix-b.html` for the endnotes cited, and the figures in `toolkit/img/`. The cover, "About this document", the Sources introduction, the header and the footer are fixed text in the kit (`build_model()` and `WORD_JS`). |

## 1. Get the kit and the site into the session workspace

1. Get the runnable file with the Artifact tool: `action: "read"`, `url: "https://claude.ai/artifact/V2Swna2EiqsdyyJkYGowix"`, `path: "rebuild_kit.py"`. The tool saves the file locally and says where; copy it to `/home/claude/kit/rebuild_kit.py` and check its MD5 against the value above. Never retype it from tool output. (If the artifact is gone, ask John before rebuilding the kit from the readable backup.)
2. Get the site:
   - **The clone has changes that are not pushed yet** (the usual case right after editing pages). Make one archive on John's computer, outside the folder first, so tar does not read its own output:
     ```
     N=kit-in-$(date +%Y%m%d-%H%M).tar.gz
     tar czf $HOME/$N --exclude=.git -C $HOME/mnt/ai-control-plane-handbook . && mv $HOME/$N $HOME/mnt/ai-control-plane-handbook/$N && md5sum $HOME/mnt/ai-control-plane-handbook/$N
     ```
     Stage it (`/Users/johnfisher/Projects/ai-control-plane-handbook/<name>`), check the md5 in the workspace, then `mkdir -p /home/claude/site && tar xzf <staged file> -C /home/claude/site && touch /home/claude/site/.kit-stamp`. Delete the archive on John's computer afterwards (ask once for delete permission on the clone folder if this session does not have it; if he declines, tell him the file name to delete).
   - **Everything is pushed:** `git clone --depth 1 https://github.com/johnfisher-ai/ai-control-plane-handbook /home/claude/site && touch /home/claude/site/.kit-stamp`.
3. `python3 /home/claude/kit/rebuild_kit.py setup /home/claude/site` (once per session). It installs python-pptx, lxml, Pillow and fontTools if missing, installs Plus Jakarta Sans Regular, Bold and Italic from the site's fonts (without glyph substitutions, as the slide images were rendered), and checks LibreOffice, poppler, Node, npx and the docx package (`npm install -g docx@9` if missing). The first `search` or `check` fetches Pagefind with npx.

## 2. Find what is out of sync, and fix it

`python3 rebuild_kit.py check SITE` compares every download with the pages (about 5 seconds) and prints `IN SYNC` or a list of items, each with the command that fixes it. Add `--render` to re-render all 58 slides and compare them with their images (about 2 minutes); run it before delivering any slide change.

| What changed on the pages | What to run |
|---|---|
| Speaker notes of slide N | `notes SITE N` |
| A slide's title or text (the heading or the "Slide text" panel) | Edit the page's HTML, then change the slide itself: `edit SITE N --old "..." --new "..."` (add `--all` for every occurrence), then `render SITE N`, and `title SITE N` if the title changed. Look at the new image: the kit changes text, not layout, so shorten wording if it no longer fits. |
| Section 7 or 8, the Part 3 introduction, the toolkit notices or About, a cited endnote in the handbook's Appendix B, or a figure on those pages | `word SITE` |
| Any of the above | `sizes SITE` (the commands above already run it): updates the sizes shown next to the download links |
| Any text inside a page's `<main>`, or a page added or removed | `search SITE`: rebuilds `pagefind/` |

Then run `check SITE --render` again until it says `IN SYNC`.

What `check` looks at: for each slide, the notes against the page's notes, the slide title and text against the page's heading and "Slide text" panel, the file title, the size shown on the page, duplicate paragraph properties (they make PowerPoint ask to repair the file) and the banned word; with `--render`, the image against a fresh render. For the Word file, it rebuilds the document from the pages and compares text, links and figures with the download, and checks the sizes on the toolkit pages, the bookmark ids and the banned word.

## 3. Deliver to the clone

Collect the files the commands changed (`find /home/claude/site -type f -newer /home/claude/site/.kit-stamp`), together with any pages edited in the workspace, into one archive with a new name each time (a reused name can deliver an old copy):

```
cd /home/claude/site && N=kit-out-$(date +%Y%m%d-%H%M).tar.gz
find . -type f -newer .kit-stamp ! -name .kit-stamp | sed 's|^\./||' > /tmp/kit-files.txt
tar czf /mnt/user-data/outputs/$N -T /tmp/kit-files.txt && md5sum /mnt/user-data/outputs/$N
```

Commit it to `/Users/johnfisher/Projects/ai-control-plane-handbook/<name>`, check the md5 there, and unpack it in the clone with `tar --overwrite -xzf <name>` (plain `tar xzf` fails with "File exists" while the session cannot delete files there). If `search` rebuilt the index, delete `pagefind/` in the clone first, because its file names change with the content (`rm -rf pagefind` needs delete permission on the clone folder; ask once). Then delete the archive and run `git status --short` to confirm the expected files changed. Validate changed files with the docx and pptx skills' `office/validate.py` if they are available. John commits and pushes with GitHub Desktop; tell him which downloads changed.

## 4. Check the external links (once per edition)

Decided (John, October 15, 2026): the endnotes keep their links. Once per edition, and after any change to Appendix B, check them on the live site and fix the broken ones; updating redirects is optional tidying.

1. The session workspace cannot reach github.io, so use the desktop app's built-in browser and open the W3C Link Checker on the live site, recursively:
   `https://validator.w3.org/checklink?uri=https%3A%2F%2Fjohnfisher-ai.github.io%2Fai-control-plane-handbook%2F&summary=on&no_referer=on&recursive=on&depth=`
   For the endnotes alone (about 4 minutes), use `.../handbook/appendix-b.html` without `recursive`. Poll the page with short waits; the result appears only when the run ends.
2. Sort what it flags:
   - **Known false alarms** (they load in a browser or a fetch, but refuse the checker): endnotes 2 (Salesforce news, 500), 16 (Salesforce Developers), 73 (NIST AI 100-1 PDF), 96 (SIX) and 99 (DTCC), all 404 or intermittent; 3 (Forbes), 42 (Medium) and 54 (New York Times; it blocks fetches too, so a person clicks it), all 403; and the LinkedIn profile (robots.txt). Before calling any other flagged link a false alarm, fetch it or open it by hand.
   - **Broken:** find the source's new address (search for its exact title), check the page carries the cited figures, then change the address everywhere it appears: `handbook/appendix-b.html`, `toolkit/appendix-d.html`, `toolkit/template.html` and the quantum briefing's own sources (`quantum/index.html`).
   - **Redirects:** optional. Check the destination before adopting it: a "latest edition" page is not the cited edition (endnote 44 links to the 2025 report's PDF for this reason).
3. If a changed endnote is one the toolkit templates cite (`check` names them as Word differences), run `word SITE`. No slide file holds endnote addresses.

Last run: October 15, 2026, after commit `54e490d`: 62 documents checked recursively in about 8.5 minutes; no redirects, every anchor valid, and only the known false alarms flagged.

## Notes

- Tested on October 15, 2026 against commit `e20c1a8`: the Word file rebuilt from the pages matches the published download in text, character formatting, links and figures; the speaker notes rebuilt from the pages are byte-identical in all 58 slide files; all 58 slide images match fresh renders; edited slides and the rebuilt Word file pass the OOXML validators. Simulated page edits (notes, a template sentence, a slide title and slide text) were each detected by `check` and fixed by the matching command.
- If a page's structure changes (an element the kit has not seen inside Sections 7 and 8), `word` stops and names the element; extend `page_blocks()` or `callout_block()`.
- A new page joins the search when its `<main>` carries `data-pagefind-body` (and, for a companion page, `data-pagefind-filter="Publication:…"`), with `<meta property="pagefind:title" data-pagefind-meta="title[content]" content="…">` in its head; breadcrumbs, the pager, slide download lines and the endnotes' "Cited in" lines carry `data-pagefind-ignore`. Give it the header's Search link and the footer's What's new link like the other pages.
- To move to a newer Pagefind, change `PAGEFIND` in the kit, run `search`, test the search page, and note the version in the repository README.
- The credit lines in the slide notes (including the pointer to the deck's adaptation permission) and the Word file's cover and license text are fixed text in the kit, so `check` does not compare them with the pages. After changing them in the kit, run `notes SITE all` and `word SITE`.
- If the notices wording on `appendix-e.html` changes, `word` warns when one of its three wording swaps no longer applies; update `NOTICE_WORDING`.
- The Word file's page count ("about 85 pages" on the toolkit pages) is LibreOffice's count; Word shows 86.
- The naming rule applies to the kit too: it never spells out the banned word (it holds it encoded) and refuses to write a Word file that contains it.
- If the kit changes: republish the artifact with the new file (pass its URL as `url`; read it first), save the same file over `claude/Rebuild kit/rebuild_kit.py`, and update the MD5, size and date here and on the artifact page.

## Set up a fresh cloud workspace

From October 2026 the kit runs in Claude Code sessions at claude.ai/code. A session started from the saved link in the punch list clones both repositories, each into a folder named after it, and these commands run from the folder that holds them. Cloud sessions come with Python, Node and Java, but without LibreOffice, poppler or the docx package, which the kit also needs.

```bash
apt-get update -qq
apt-get install -y -qq --no-install-recommends libreoffice-impress libreoffice-writer poppler-utils fontconfig
npm install -g docx@9.9.0
KIT="ai-control-plane-handbook-notes/project-files/claude/Rebuild kit/rebuild_kit.py"
python3 "$KIT" setup ai-control-plane-handbook
python3 "$KIT" check ai-control-plane-handbook --render
```

Keep docx at 9.9.0. From 9.10.0, released October 10, 2026, the package stores the #figure part of a link separately, so check reports five figure links in the published Word download as changed when nothing has, and word would rewrite them. With these tools on Ubuntu 24.04, the system cloud sessions run, check --render on a fresh clone of main at 52f3b15 said IN SYNC for the 58 slide files, the Word download and the search index on October 19, 2026. To save the install time in every session, the apt-get and npm lines can go in the cloud environment's setup script at claude.ai/code, which caches what it installs.

The kit can't remake the client deck's slide images or the guide's figures in toolkit/img/. Both came from Word and PowerPoint files that stayed in the Cowork folder, so a change to one of them needs its source file from John.

## Naming scan

The scan stays out of the public repository, because the decoded word must never appear there. Save it as `naming_scan.py` in the workspace, outside both repositories, and run it on each clone before every delivery:

```python
import pathlib, sys
word = bytes.fromhex('416e79706f696e74').lower()
hits = 0
for f in pathlib.Path(sys.argv[1]).rglob('*'):
    if f.is_file() and '.git' not in f.parts and 'node_modules' not in f.parts and word in f.read_bytes().lower():
        hits += 1; print('FOUND in', f)
print(f'naming scan: {hits} file(s) with a match'); sys.exit(1 if hits else 0)
```

## Deliver through GitHub

From October 19, 2026, John works on a Mac that can't run the Claude desktop app, so sessions can't reach his folders, and Claude delivers through GitHub, as the AI+ hub does:

1. Check access before changing anything. `git push --dry-run origin HEAD:refs/heads/<branch>` in each clone tests pushing without changing anything on GitHub. A refusal saying a repository "is not in this session's authorized repository set" means the session started without it, so ask John to start a new session from the saved link in the punch list.
2. Make the change, bring the downloads in sync with the kit, and run the checks: the HTML validator, axe at 1280 px light and 375 px dark with no sideways scroll, internal links and anchors, the kit's check (with --render after any slide change) and the naming scan.
3. Commit the round on its own branch, named for the work, such as `link-to-ai-plus`, and push that branch. Never push to main, never force-push, and never rewrite a pushed commit. The session's GitHub proxy refuses tag pushes and branch deletions and lets a push update any branch, so this rule rests on Claude unless John protects main on GitHub.
4. Open a pull request whose description is the change summary (what changed, which downloads were updated or that none were affected, the check results, and anything John must do by hand), or give John the link to create it. Use the REST API, `gh api repos/johnfisher-ai/<repository>/pulls` with `title`, `head`, `base` and `body` fields, because the proxy refuses `gh pr`, which uses GraphQL. In a claude.ai/code session John can also use Create PR in the diff view.
5. Update the punch list in this private repository in the same round, on a branch with its own pull request.
6. John reviews the changes on GitHub and merges the pull requests, and the site's merge publishes through GitHub Pages. He then fetches and pulls in GitHub Desktop so his Mac matches. Releases and tags stay with John, because the proxy refuses tag pushes.
7. Sessions can't reach github.io under the default network setting, so John looks at the changed pages on the live site after a merge and runs the W3C Link Checker in his browser at each edition (section 4). A session can do both itself if John adds johnfisher-ai.github.io and validator.w3.org to the cloud environment's allowed domains.
