# Punch list (revised October 15, 2026): the handbook site first

Last updated October 19, 2026. That day the AI+ hub moved to Claude Code, and John decided to move this project the same way. The work moves to Claude Code sessions that start with both repositories, and this file and the other project files move to the private repository johnfisher-ai/ai-control-plane-handbook-notes (see "Move to Claude Code" below). Main was still at 52f3b15 when checked on October 19.

The A–F round is done and accepted (see README_START_HERE.md, Status). The next step is the website for the public edition of the handbook: a public GitHub repository in John's account, hosted with GitHub Pages from that repository. Start simple: repository, landing page, publish, then convert the Word handbook to HTML. The AI+ name, hub site and daily articles come later.

**Repository: `johnfisher-ai/ai-control-plane-handbook`**, site **https://johnfisher-ai.github.io/ai-control-plane-handbook/** (live since October 14, 2026). The name matches the handbook's title, reads clearly in the URL, avoids product trademarks and the "JRF" initials, and works as one of several sibling repositories that the AI+ hub (`johnfisher-ai.github.io`) can link to without renaming.

Owner: **J** = John (account, settings, pushes); **C** = Claude (authoring, conversion, checks).

## Move to Claude Code (October 19, 2026)

- [x] The AI+ hub moved to Claude Code (October 19). Its notes went to the private repository `johnfisher-ai/ai-plus-social-media-promotion`, and its first pull request from a Claude Code session was merged the same day.
- [x] Decide to move this project the same way (J, October 19).
- [x] Prepare the move (C, October 19). A kit for a new private repository holds `CLAUDE.md`, which carries the project instructions adapted for Claude Code and the notes from the projects' memory, and `project-files/`, which holds all 14 project files at their project paths and a short README. In the copy of README_START_HERE the banned word is masked. The rebuild kit's README gains sections on a fresh cloud workspace, the naming scan and delivery through GitHub.
- [x] Check the kit on a fresh clone of main at 52f3b15 (C, October 19). With docx 9.9.0, `check --render` says IN SYNC for the 58 slide files, the Word download and the search index. From docx 9.10.0 the check reports five figure links in the Word download as changed, so the workspace setup pins 9.9.0.
- [ ] Create the private repository `johnfisher-ai/ai-control-plane-handbook-notes` on github.com, with **Private** chosen and **Add a README file** ticked, then clone it with GitHub Desktop to `~/Projects/ai-control-plane-handbook-notes` (J).
- [ ] Add both `johnfisher-ai/ai-control-plane-handbook` and the new repository to the Claude GitHub App's repository access at github.com/settings/installations (J). A private repository is listed at claude.ai/code only when the app's repository access includes it.
- [ ] Add the kit to `~/Projects/ai-control-plane-handbook-notes`, with `CLAUDE.md` and `project-files/` at its root, and commit and push it with GitHub Desktop (J). From that commit the repository's copies are the masters, and the claude.ai project keeps an October 19 snapshot.
- [ ] Start each Claude Code session from the saved link, which selects both repositories and asks Claude to read `CLAUDE.md` first (J). The link is https://claude.ai/code?repositories=johnfisher-ai/ai-control-plane-handbook,johnfisher-ai/ai-control-plane-handbook-notes&prompt=Read%20ai-control-plane-handbook-notes%2FCLAUDE.md%20and%20the%20files%20it%20lists%20before%20anything%20else.. The first session repeats the access check, confirms that `project-files/` matches the kit and runs the kit's `check --render`.
- [ ] First pull requests (C, first Claude Code session). The site's README gains a section saying that changes reach the site through pull requests, as the hub's README now does, and the handbook links to AI+ in the places John chooses. The hub already links to the handbook, and no handbook page links back yet.
- [ ] Consider requiring a pull request for main in both repositories, with a ruleset or branch protection (J). The session's GitHub proxy refuses tag pushes and branch deletions and lets a push update any branch, so today only Claude's instructions keep a session off main. The rule would also apply to John's own pushes from GitHub Desktop, and adding him to a bypass list would likely let sessions through too, since they push with his GitHub credentials.
- [ ] Once the kit is committed, change the claude.ai project's instructions to say that the work moved to Claude Code and that the masters are in the private repository (J). `CLAUDE.md` already carries the new delivery rule.

## Open items (October 15, 2026)

The rest of this list records what was done and decided; these are the items still open. Latest pushed commit: `52f3b15` (site search and What's new, edition 2026.1, tagged `v2026.1`, October 15); a fresh clone matches Claude's working copy.

Done (J, October 15): the repository About panel; "Enforce HTTPS" confirmed and the wiki and projects settled; two-factor authentication confirmed; Lighthouse, LinkedIn Post Inspector, and a look in Safari and Edge; the New York Times link in endnote 54; a read-through on a phone and a review of the live site.

Decided (J, October 15) and done (C): keep everything, including the site code, under CC BY-NC-ND 4.0; add permissions to adapt the shared slides and the Word templates (deck notices, toolkit Appendix E and G, the deck and toolkit index pages, the README, the credit line in all 58 slide files and the Word file's license text; the rebuild kit updated to match); drop the Word Accessibility Checker on the public handbook. Pushed (J, October 15, commit `c1cb5e3`, 70 files); a fresh clone of the pushed commit matches Claude's working copy.

Done (J, October 15): the note to Michael S with the five asks; the pre-readout checks (illustrative figures against the client's baseline; Informatica MCP servers, Agent Evals, per-agent budget caps and who supports the custom policies); the old handbook copy on the Desktop deleted or archived (items 34–36).

Done (C, October 15): live test of commit `c1cb5e3` in the desktop app's browser. All 279 files are served with HTTP 200 and are byte-identical to the repository (SHA-256), including the Word download and all 58 slide downloads, which are served with the right Word and PowerPoint content types. 57 pages, 4,397 internal links and 1,979 #anchors resolve, with no duplicate ids; a missing page returns the custom 404. The deck notices' additional permission (`#permission`), toolkit Appendix E (`#word-templates-permission`) and Appendix G ("License and permissions") show the pushed wording, and every download link points at its file. axe 4.10: no violations on any of the 57 pages at 1280 px light or 375 px dark, and no sideways scroll. The rebuild kit's `check` on a fresh clone says IN SYNC; the banned word appears nowhere, inside the Office files included.

Done (J, October 15): John reviewed the companion pages and the quantum briefing.

Done (C, October 15) and pushed (J, commit `54e490d`, 10 files):
- **Endnote links.** Decided (J): keep the links in the endnotes. The 16 permanently redirected links (in 14 endnotes: 8, 20, 21, 23, 28, 29, 33, 44, 61, 65, 72, 82, 95 and 103; two links each in 8 and 33) now use their final addresses, in handbook Appendix B, toolkit Appendix D and `toolkit/template.html`. Exception: the Microsoft Digital Defense Report 2025 address (endnote 44) now redirects to the 2026 report, so endnote 44 links to Microsoft's PDF of the 2025 report instead (it confirms the 32%, 97% and 99% figures Section 5 cites). The NIST CAISI blog (61) has moved to a "CAISSI Research Blog" address; the citation keeps the publisher's name at publication. Endnote 96 (SIX) loads (J checked); 2, 16, 73 and 99 load when fetched; 3, 42 and 54 block automated checkers.
- **Scorecard.** "Policy enforcement" now includes exposure-limit breaches refused by a custom aggregate-risk policy where one is in place (data source "Gateway aggregate-risk refusals"), and its leading indicator counts exposure-limit refusals separately: handbook Section 9, toolkit Section 6, template T6 in toolkit Section 7, and executive deck slide 29 (slide text, the "Slide text" panel and two speaker-note additions).
- **Downloads updated:** `deck/slides/the-ai-control-plane-slide-29.pptx` and `deck/img/slide-29.png`; `toolkit/downloads/ai-control-plane-assessment-templates.docx` (endnotes 21, 72 and 82 and template T6). Sizes on the pages unchanged.
- **Checks:** rebuild kit `check --render` IN SYNC (58 slides and the Word file); OOXML validators pass; W3C validator and axe (1280 px light, 375 px dark) clean on the 7 changed pages, no sideways scroll; internal links and anchors resolve; no old addresses left; banned word nowhere. Delivered to the clone (checksums match).

Done (C, October 15): live link checks after commit `54e490d`, in the desktop app's browser. W3C Link Checker on Appendix B and recursively over the whole site (62 documents): no redirects left, every anchor valid, nothing broken. Only the known false alarms were flagged (endnotes 2, 16, 73 and 99 refuse the checker but load; 3, 42 and 54 block automated checkers; the LinkedIn profile is excluded by robots.txt). The once-per-edition procedure is now section 4 of `claude/Rebuild kit/README.md` and on the Site Rebuild Kit artifact.

Done (C, October 15) and pushed (J, commit `52f3b15`, 142 files: 60 changed, 82 new); release "Edition 2026.1" and tag `v2026.1` created on that commit (J):
- **Site search.** `search.html` with Pagefind 1.4.0's search interface, themed with the site's colours (light and dark), result titles such as "Handbook · Section 9. Measuring success", sub-results that link to the section or slide, and a Publication filter (Handbook, Executive deck, Assessment toolkit, Quantum briefing). Only each page's `<main>` is indexed; breadcrumbs, pagers, slide download lines and the endnotes' "Cited in" lines are left out. A Search link is in every page header (and on the 404 page); `?q=` opens the page with a search. The index is in `pagefind/` (79 files, about 1.2 MB); Pagefind's MIT license is in `assets/licenses/`.
- **What's new.** `whats-new.html`: edition 2026.1, the changes of October 15 and what was published on October 14, how editions work, and how to cite the edition. Linked from every page's footer, from the landing page ("Edition 2026.1 · What's new") and in the sitemap (57 URLs). The landing page's book data now carries version 2026.1.
- **README** (repository): edition 2026.1, the Editions section, search and Pagefind's license.
- **Rebuild kit, third version** (72,147 bytes, MD5 `3277bcdb851c19ead681a9a164a03c00`): `search SITE` rebuilds the index and `check` reports a stale one; the endnote "Cited in" stripping tolerates extra attributes. Artifact, project copy and README updated.
- **Downloads:** none affected (the slide files and the Word file are unchanged; `check --render` IN SYNC).
- **Checks:** W3C validator (59 pages and the CSS) and axe (59 pages, 1280 px light and 375 px dark, including the search page with results) clean, no sideways scroll; 4,561 internal links and anchors resolve; search tested in Chromium (results, sub-result anchors, filters, no console errors); banned word nowhere.
- **Live test (C, October 15), desktop app's browser:** all 282 site files byte-identical to the repository, and Pagefind's entry, scripts, styles, wasm and metadata files match; the index reports Pagefind 1.4.0 and 57 pages, every page's search data loads, and every result address resolves. Search on the live page: `?q=` opens with results, typing searches, the Publication filter narrows ("kill switch": 30 results, 6 in the executive deck), sub-results link to sections and slides. 59 pages, 4,561 internal links and 1,987 anchors resolve. axe: no violations on the search page with results, What's new, the landing page, Section 9 and deck Part 3, at 1280 px light and 375 px dark; no sideways scroll. The What's new page's tag link (github.com/…/tree/v2026.1) opens the tagged files.

**Optional and later**
1. Each edition: re-run the link check (Rebuild kit README, section 4) and fix any broken links; add the edition to the What's new page and tag it.
2. Done: the AI+ hub has its own repository (`johnfisher-ai.github.io`), went live on October 15 and has worked in Claude Code since October 19. The starter pack this project prepared stays in `claude/AI+ starter pack/` as a record. Still to do here: link the handbook to the hub (see "Move to Claude Code"), and update the handbook's addresses if a custom domain is added.

## Progress (October 14, 2026)

- Done: account `johnfisher-ai`; repository public, branch `main`; local clone `~/Projects/ai-control-plane-handbook`, connected to Cowork. John commits and pushes with GitHub Desktop (Claude cannot push: no GitHub connection in Claude, and a token would be needed).
- Done and live: the starter commit "Add landing page and starter files" (now `0049730`, authored with the GitHub no-reply address; John replaced the first commit, which had used his personal email): README.md, LICENSE (CC BY-NC-ND 4.0 legal code), .nojekyll, .gitignore, sitemap.xml, index.html, 404.html, assets/css/site.css, Plus Jakarta Sans (five woff2 with OFL.txt), favicon (SVG, 32 px PNG), Apple touch icon, 1200×630 social card. The images carry Anthropic content credentials (C2PA metadata) added when the files were written.
- Landing page tested locally (W3C validator, axe, Lighthouse 100) and live in the desktop app's browser (every file HTTP 200 and byte-identical, custom 404, fonts, og:image, axe at 1280 px light and 375 px dark, no sideways scroll, W3C on the live URLs). Live Lighthouse not run: PageSpeed Insights' daily quota from this network was used up, and Claude's workspace cannot reach github.io.
- **Phase 4 done and live (October 14, 2026, commit `fccb762` "Add the handbook, one page per section and appendix").** John's decision: one page per section and appendix, no downloads. Claude wrote into the clone:
  - `handbook/`: 20 pages (introduction `index.html`, `executive-summary.html`, `section-01.html`–`section-13.html`, `appendix-a.html`–`appendix-e.html`) and `handbook/img/figure-01.png`–`figure-22.png`.
  - `tools/build_handbook.py`: the converter (since removed; the pages are now the master).
  - Updated: `index.html` ("Read the handbook" now links to the handbook; contents items link to their pages), `assets/css/site.css` (handbook page styles), `sitemap.xml` (21 URLs), `README.md` (status and file list), `.gitignore` (blocks .docx, .doc and .pdf).
- Phase 4 tests (local copy): every citation matches the Word file endnote by endnote (310 citations, 279 superscripts, 107 endnotes); every section, figure (22) and table is present; axe: no violations on any of the 22 pages, desktop light and phone dark; 1,346 internal links, none broken; W3C validator: no errors; Lighthouse 99–100 on the pages tested; banned word nowhere; the term check adds only hits already in the approved public Word file. External links: see the live tests below.
- Found in conversion and fixed: the public handbook's Section 7 cited "2177" instead of 21,77 in two places (Figure 5 caption and the "Capabilities and data" bullet). The clean and review copies in `public_edition/` are updated, with the script `build/public/scripts/fix_cites_2026_10_14.py` and a note in `public_edition/review/CHANGES.md`. The masters are unaffected.
- Live tests (desktop app's browser, October 14, 2026): all 57 files served with HTTP 200 and byte-identical to the clone; a missing page returns the custom 404; 1,498 internal links and every #anchor resolve; axe: no violations on the 22 pages at 1280 px light and 375 px dark, and no sideways scroll; Section 7 shows 21,77; endnote links land on their entries. W3C Link Checker (recursive, 23 documents): no broken links. It flagged seven endnote links (2, 3, 16, 42, 54, 73, 99) that reject its automated requests; six load normally when fetched, and the New York Times link (54) blocks automated tools, so J clicked it (done October 15). Fifteen endnote links redirect permanently (for example the CDO Magazine, ISO 42005, BIS BCBS 239 and SEC links); optional: switch them to their new addresses at the next edition. Live Lighthouse still not run (PageSpeed Insights quota from this network); the files are identical to those that scored 99–100 locally.
- Done (J, October 15): LinkedIn Post Inspector; Lighthouse at pagespeed.web.dev; repository About panel; "Enforce HTTPS" confirmed; the New York Times link in endnote 54. Items 6 and 8 decided October 15 (see Phase 0).

## The website is the master; style pass done (October 14, 2026)

- Decided (John): the HTML pages in the site repository are the master copy from now on. Edit them directly. The Word files are no longer updated, and the converter `tools/build_handbook.py` was removed from the repository.
- Done: the style pass that removes AI tells, applied to every page of the site in one go (plan, results and before-and-after counts in the Claude Docs doc "AI tells in the handbook: plan to fix", https://claude.ai/code/artifact/3b52b241-e496-4162-afd7-34045d386896). Checks passed: 308 citations unchanged and on the same claims, links and anchors, axe (22 pages, desktop light and phone dark), W3C validator, banned word; an independent review's 31 findings were fixed. Pushed and live, with the grid fix (table cells without bullets, one entry per line; commit `691c5e1`).
- Done (J, October 15): the project instructions field now says the website is the master, with the download sync rule and a pointer to the rebuild kit.
- Done: the same pass for the companions (next section).

## Companion pages (October 14–15, 2026)

- John's choices: the executive deck as slide images with the slide text and speaker notes; the templates as web pages only; AI tells removed during the conversion; all three companions at once.
- Done and pushed (commit `f568cfe`, October 14): `deck/` (9 pages), `toolkit/` (24 pages: the guide, the client report template and the client deck) and `quantum/` (1 page), with a "Companion materials" section on the landing page, a "Companions" header link on the handbook pages, the sitemap (55 URLs) and the README. Handbook Figures 2, 3 and 7 re-rendered from the edited deck. Details, the style-pass numbers and the checks are in `claude/Companion pages 2026-10-14.md`.
- Done and pushed (October 15): every executive deck slide (1–58) has a one-slide PowerPoint download under its image (`deck/slides/`), with the website's speaker notes and a credit and license line (commit `6dc3aad`). The PowerPoint repair prompt on those files was fixed (adjacent duplicate paragraph properties left by the slide-text edits) and pushed (commit `e90f108`); John downloaded and confirmed.
- Done and pushed (October 15, commit `e20c1a8`): the toolkit's thirteen templates as one Word document, `toolkit/downloads/ai-control-plane-assessment-templates.docx` (Part 1 blank, Part 2 filled in for use case 1), with a new Appendix G "Templates to download", a download box in "About this toolkit", a "Templates to download" item in "What is inside", and a download line in Sections 7 and 8. Opened cleanly in John's Word for Mac. Details and checks in `claude/Companion pages 2026-10-14.md`.
- Done (C, October 15): live test after the pushes (commit `c1cb5e3`): all 279 files byte-identical to the repository, links and anchors resolve, axe clean on all 57 pages at both widths; details under Open items.
- **Standing rule (John, October 15, 2026): keep the downloads in sync with the pages.** When a change touches an executive deck slide (its text, image or speaker notes), update that slide's one-slide PowerPoint file in `deck/slides/` and its image in the same change. When a change touches a toolkit template (Sections 7 and 8, T1 to T13, or their sources and notices), rebuild `toolkit/downloads/ai-control-plane-assessment-templates.docx`. Each change summary says which downloads were updated, or that none were affected. Appendix G tells readers the pages are the current version.
- Done (J, October 15): the rule is in the project instructions field.
- Done (C), October 15: a rebuild kit that works from the site's HTML alone, so any later session can check and regenerate the downloads. One Python file with `setup`, `check`, `word`, `notes`, `edit`, `title`, `render` and `sizes` commands. Runnable copy attached to John's private artifact "Site Rebuild Kit" (https://claude.ai/artifact/V2Swna2EiqsdyyJkYGowix); readable copy and workflow in `claude/Rebuild kit/`. Tested against commit `e20c1a8`: `check --render` says IN SYNC for all 58 slides and the Word file.
- Decided (J, October 15) and done (C): an additional permission lets readers adapt the slide downloads and the Word templates for their own presentations and work, inside their organization or with clients, including paid work, with credit; selling them or publishing changed versions is not covered. The base license stays CC BY-NC-ND 4.0. Pushed (commit `c1cb5e3`, October 15).
- Next from John's review: further changes to the companions, then the quantum briefing.

## Phase 0. Decide and prepare

1. Done: account `johnfisher-ai`, which will also host the AI+ hub.
2. Done: commits use the GitHub no-reply email; two-factor authentication confirmed (J, October 15).
3. Done: John pushes with GitHub Desktop; Claude writes the files into the connected local folder.
4. J+C: Only the public edition goes on the site, starting with `public_edition/JRF_AI_Control_Plane_Handbook_Executive_Public.docx`. Never the masters in `deliverables/`, and never the review copy.
5. Done: plain hand-authored HTML and CSS, no build step and no framework; Pages serves `main` from the root, with `.nojekyll`.
6. Decided (J, October 15): everything, including the site code, stays under CC BY-NC-ND 4.0 (in `LICENSE`), with additional permissions to adapt the slide downloads and the toolkit's Word templates (deck notices; toolkit Appendix E).
7. Decided (October 14, 2026): no downloads; the site offers web pages only. Changed October 15, 2026, at John's request: the executive deck offers each slide as a one-slide PowerPoint download, and the toolkit offers its templates as one Word document (Appendix G). Other Word files and all PDF files stay out of the repository.
8. Dropped (J, October 15): Word's Accessibility Checker on the public handbook; the Word files are archived and the site is the master.

## Phase 1. Repository: done

9. Done: repository created; About panel filled in (description, website link and topics; J, October 15).
10. Done: starter files; `handbook/` added in Phase 4.
11. Done: pushed, and Pages is on; "Enforce HTTPS" confirmed and the wiki and projects settled (J, October 15).

## Phase 2. Landing page: done

12–16. Done: landing page, styles, metadata and share image, 404 page, accessibility basics (see Progress).
17. J: No analytics for now. If they're added later, add a privacy note.

## Phase 3. Publish and test the landing page: done

18. Done: live at the URL above.
19. Done: live validator, axe, phone width and file integrity; Lighthouse, LinkedIn Post Inspector, and a look in Safari and Edge (J, October 15).
20. Done: content checks (banned word, terms, disclosure, license).

## Phase 4. Convert the Word handbook to HTML: done and live

21. Done: one page per section and appendix: an introduction, the executive summary, Sections 1–13, Appendices A–E (Appendix B is the endnotes page; D the notices; E About John Fisher). Header links to Contents, Endnotes, Companions and About the author; breadcrumbs, a contents sidebar (open on wide screens) and previous/next links on every page; footer with the license, the Notices link and the disclosure.
22. Done: the pages are now the master and are edited directly; the converter was removed.
23. Done: Figures 1–22 as PNGs with their alt text, each in a `figure`/`figcaption` pair, with `id="figure-N"` so references can link to them.
24. Done: tables have header rows; wide tables scroll sideways on phones and can be reached with the keyboard; one-cell boxes (such as the first-90-days box) are styled asides.
25. Done: each superscript links to its entry on the Appendix B page, and each entry lists where it is cited, with links back; the numbering stays 1–107; Appendix A's endnote column links too.
26. Done: "Section 7", "Figure 5", "Appendix C" and similar are internal links (not on the page they point to).
27. Done: Appendix D (notices) and E (About John Fisher) are pages, linked from the footer and the header.
28. Done: tests locally and live (see Progress); a read-through on a phone (J, October 15).
29. Done: the landing page's "Read the handbook" link and contents links point at the pages, and `sitemap.xml` lists them; live site reviewed (J, October 15).

## Phase 5. Later (same repository)

30. Done and live (October 14, 2026): the executive deck (slide images with the slide text and notes; one-slide PowerPoint downloads added and pushed October 15), the assessment toolkit (guide, template, client deck; the templates as a Word download added and pushed October 15) and the quantum briefing as web pages (see "Companion pages" above).
31. Done (October 15): site search (Pagefind), the "What's new in this edition" page, and release "Edition 2026.1" with tag `v2026.1` (commit `52f3b15`).
32. AI+: moved to its own Claude project and repository (October 15; starter pack in `claude/AI+ starter pack/`). The handbook repository keeps its name and is linked from the hub.

## Carried over

33. Done (J, October 15): the project instructions field was rewritten; the leftover fragment is gone.
34. Done (J, October 15): the note to Michael S with the five asks.
35. Done (J, October 15): the pre-readout checks (illustrative value figures against the client's baseline; Informatica MCP servers, Agent Evals, per-agent budget caps and who supports the custom policies). Repeat before each new client readout.
36. Done (J, October 15): the old handbook copy on the Desktop.
37. Done (C, October 15): exposure-limit refusals counted under "Policy enforcement" in the scorecard (see Open items).
