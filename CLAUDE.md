# Claude's instructions for the AI Control Plane Handbook

This private repository is the home of the AI Control Plane handbook work in Claude Code. John decided on October 19, 2026 to move the work here from the claude.ai project "JRF The AI Control Plane White Paper", as the AI+ Hub moved the same day, because his Mac can't run the Claude desktop app and Claude Code sessions at claude.ai/code can clone his repositories and push review branches. The copies in this repository are the masters, and the claude.ai project keeps a snapshot from October 19.

## Start every session here

1. Read `project-files/claude/README_START_HERE.md`, `project-files/claude/Punch list 2026-10-14.md` and `project-files/claude/Rebuild kit/README.md` before changing anything. Read `project-files/claude/Companion pages 2026-10-14.md` before changing a deck, toolkit or quantum page, and a round record in `project-files/claude/` when a task reopens its subject.
2. Check access before any work. The session must have been started with `johnfisher-ai/ai-control-plane-handbook` and this repository selected. Run `git push --dry-run origin HEAD:refs/heads/<branch>` in each clone, which changes nothing on GitHub. If either push is refused, stop and follow what the kit README's "Deliver through GitHub" section says about that refusal.
3. Before a change that touches a slide, a template or the search index, set up the workspace as the kit README's "Set up a fresh cloud workspace" section says.
4. Finish every round by updating the punch list on a branch of this repository, with its own pull request, and ask John to merge it with the site's pull request so the next session starts from current notes. A cloud session keeps nothing that isn't committed, so decisions and lessons go in the punch list, in the kit README or in this file.

## Where things live

| What | Where |
|---|---|
| Project instructions | This file, under "Project instructions" |
| History to October 15, 2026, with the content map and the conventions | `project-files/claude/README_START_HERE.md` |
| Punch list | `project-files/claude/Punch list 2026-10-14.md` |
| Rebuild kit for the downloads and its README | `project-files/claude/Rebuild kit/` |
| How the companion pages and their downloads were made | `project-files/claude/Companion pages 2026-10-14.md` |
| Records of the Word-era rounds | `project-files/claude/Fact-check log 2026-09-29.md`<br>`project-files/claude/Feedback plan - Michael S 2026-09-29.md`<br>`project-files/claude/Structure and ROI round 2026-09-29.md`<br>`project-files/claude/Improvements round 2026-09-30.md`<br>`project-files/claude/Public edition 2026-10-02.md` |
| The AI+ starter pack this project prepared on October 15 | `project-files/claude/AI+ starter pack/`, kept as a record<br>The hub's private repository holds the current copies |
| Claude Docs this project used | "AI tells in the handbook: plan to fix", https://claude.ai/code/artifact/3b52b241-e496-4162-afd7-34045d386896<br>"Public edition without roadmap or GA: plan", https://claude.ai/code/artifact/b747a07e-db71-4e10-927b-40fd6be7c7aa<br>Both stay live on claude.ai, and README_START_HERE and the round records summarize them |
| John's private artifact "Site Rebuild Kit" | https://claude.ai/artifact/V2Swna2EiqsdyyJkYGowix, a spare copy of the kit |
| The site | `johnfisher-ai/ai-control-plane-handbook`, which is public, so internal notes and this file never go there |
| The archived Word and PowerPoint masters, generators and public-edition files | The Cowork folder JRF_AI_Control_Plane_White_Paper_Active on John's Mac |

The project files keep their claude.ai names and paths under `project-files/`, so `claude/Punch list 2026-10-14.md` in a note means `project-files/claude/Punch list 2026-10-14.md`. Older passages in README_START_HERE, the punch list and the kit README describe the Cowork route through connected folders, with John pushing from GitHub Desktop, and the kit README's last three sections win where they differ. No session can reach John's Mac, so a file that stayed in the Cowork folder is out of reach until John adds it to this repository.

## How John works

These notes come from the claude.ai projects' memory.

- John uses Claude only in a web browser, because his Mac is too old for the Claude desktop app.
- He has GitHub Desktop on that Mac with his repositories open.
- He connected GitHub to Claude and installed the Claude GitHub App.
- He reviews and merges pull requests on GitHub, then pulls in GitHub Desktop.
- The handbook, its decks and the toolkit are his own work, written on his own time with his own computer and Claude account, and were not made for his job.
- Since October 14, 2026 the site's HTML pages are the master. He wants no Word file or other file on his Mac updated for handbook changes, and the slide and template downloads kept in sync with the pages.
- He wants writing free of AI tells in all his projects, by the style rules below.

## Project instructions

These are the claude.ai project's instructions, changed only where the move requires it. The banned word is given in hex, the delivery sentence is the GitHub rule John agreed for the hub on October 19, the punch list and the rebuild kit live in this repository, and change summaries also name what John must merge or do by hand.

This project maintains The AI Control Plane handbook and its companions (executive deck, assessment toolkit, quantum briefing) as a public website: GitHub repository johnfisher-ai/ai-control-plane-handbook, local clone ~/Projects/ai-control-plane-handbook. The HTML pages are the master: edit them directly. The Word and PowerPoint files in the archived Cowork folder are no longer updated. Read README_START_HERE.md and the latest punch list in this repository's `project-files/claude/` before changing anything, and keep the punch list current there. Claude works on a fresh clone of each repository and pushes every round to a review branch with a pull request; it never pushes to main or force-pushes. John reviews and merges the pull request on GitHub, which publishes, then pulls in GitHub Desktop.

Keep the downloads in sync with the pages. When a change touches an executive deck slide (its text, image or speaker notes), update that slide's one-slide PowerPoint file in deck/slides/ and its image in the same change. When a change touches a toolkit template (Sections 7 and 8, T1 to T13, or their sources and notices), rebuild the Word download in toolkit/downloads/. Every change summary says which downloads were updated, or that none were affected, and what John needs to merge or do by hand.

To check or rebuild the downloads, use the rebuild kit described in `project-files/claude/Rebuild kit/README.md`.

Naming rule: one product name must never appear in any page, document, slide, speaker note, figure, caption, file property or discussion. It is the word whose ASCII bytes are hex `416e79706f696e74`, so scans decode it at run time and it is never typed. Call integration capabilities MuleSoft (connectors, APIs, MCP Bridge) and the control plane MuleSoft Agent Fabric. CloudHub, the runtime for Agent Fabric, may be named, as may Runtime Fabric.

Keep one endnote list shared by the handbook and the decks, numbered in order of first citation. Name a source (an analyst, publisher, magazine or company) in the text only when the same sentence carries its endnote. Cite sources with superscript numbers on pages and slides and bracketed numbers in speaker notes. Label illustrative numbers as illustrative. Name only publicly available capabilities, with no GA labels or roadmap.

Writing style: no AI tells. Apply these rules to everything you write or edit, and check for them before delivering.

1. Headings say what the section argues or covers, in plain words and sentence case. No number formulas ("Two uncertainties, one hedge"), and no colon or comma devices ("Delegation chains: narrow authority at every hop", "The north star, realized"). Proper names are exempt.
2. Never put a colon before a list of clauses joined by semicolons. Write a list of actions as one sentence with commas, or as a real bulleted list.
3. Never use two semicolons in a sentence, and use at most one in a paragraph. Split chained clauses into separate sentences of different lengths.
4. In tables, put one item per line in a cell. Never separate items with semicolons.
5. Don't use a colon to set up a reveal ("The answer is X: a governed layer that..."). Write a full sentence instead. Colons that introduce a list or a table are fine.
6. State the point directly instead of using "X, not Y", "not only... but also", or more than one "rather than" in a paragraph. Keep a contrast only where precision or legal wording needs it.
7. No punchlines. Don't end a paragraph with a short sentence after long ones, and don't write fragments such as "Sequence matters." Fold the point into the sentence it introduces. Allow at most one short emphatic line per section.
8. No number signposts or summary openers ("Two rules apply.", "Together they say the same thing:"). Let the content carry itself.
9. In bullets, use bold only for a label that names a thing (a component, role, metric or decision), never for a headline sentence. Don't use "Key takeaways"; use a plain heading such as "In brief".
10. Parallel sections, such as use cases or case studies, must not share sentence frames or subheading patterns. Write each one in its own words.
11. No em dashes in prose.
12. Aim for variety, not blandness. Vary sentence length, and keep a few strong lines where they carry the argument.

A style edit never changes:

- meaning, numbers or dates;
- citations: each one stays on the claim it supports, and a named source keeps its citation in the same sentence;
- quotations, source titles, or legal and disclosure wording;
- labels such as "Illustrative", product names or defined terms.

Before delivering an edited text:

- count the semicolons, colons, "not" contrasts, punchline endings and headings with a colon or comma;
- compare each changed paragraph with the original for lost qualifiers, shifted claims or citations that came apart from their claim;
- read a changed passage aloud, and rewrite anything that still sounds like a slide.
