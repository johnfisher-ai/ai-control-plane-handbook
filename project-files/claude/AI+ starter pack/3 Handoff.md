# AI+ starter pack 3 of 4: handoff for the JRF AI+ Hub project

Written on October 15, 2026, in the AI Control Plane project, for the first session of the new project. Nothing of the hub has been built yet. The detailed plan is the Claude Docs document **"Public site, journal and LinkedIn series: plan"** (https://claude.ai/code/artifact/a3292c9f-a578-4032-9430-5f6282116d50, last revised October 2, 2026). It is the source for the article list, the LinkedIn calendar and the site map. Parts of it have since been overtaken (see "What has changed since the plan").

## Where things stand

| Item | Status on October 15, 2026 |
|---|---|
| Site name and tagline | Decided: **AI+**, "AI, plus the data science, math, statistics and Python behind it"; "AI+ by John Fisher" where the name stands alone |
| GitHub account | `johnfisher-ai`. The hub becomes its user site, `johnfisher-ai.github.io` |
| AI Control Plane handbook | Live as its own site, https://johnfisher-ai.github.io/ai-control-plane-handbook/ (repository `johnfisher-ai/ai-control-plane-handbook`). Edition 2026.1, tagged `v2026.1` |
| The handbook's companions | Live on the same site: executive deck (58 slides, each a PowerPoint download), AI Control Plane Assessment toolkit (guide, client report template, client deck, templates as a Word download) and quantum briefing |
| John's other sites | Seven sites and two other repositories on the account (file 4) |
| Hub repository, Claude project, domain | Being set up now (file 1) |

## Decisions still open

These follow the plan's decision list (D2 to D16), updated to October 15. The first three are setup decisions (file 1).

| # | Decision | Recommendation | Note |
|---|---|---|---|
| D2 | Custom domain | Decide before the first LinkedIn post. If yes, a domain with John's name | Setting it on the hub moves the handbook under it too; the handbook project then updates its own addresses |
| D4 | Site builder | Quarto, rendered in Claude's workspace into `docs/` and committed as finished pages. Fallback: plain HTML with Pagefind, like the handbook | Check first that Quarto runs in the workspace. Claude cannot see GitHub Actions logs, so Actions only if scheduled publishing is wanted later |
| D9 | Licenses | CC BY 4.0 for articles and guide articles, MIT for code; the handbook stays CC BY-NC-ND 4.0 | John chose CC BY-NC-ND 4.0 for the handbook, its decks and the toolkit. Ask whether the AI control plane articles should match |
| D6 | Posting cadence | Eight posts a week (plan) | |
| D7 | Article link in the post or the first comment | Test both over the first 10 posts | |
| D8 | Audience tags | Developer in place of Software Engineer; add Analyst and CISO | |
| D11 | Web analytics | A cookie-free counter, or none | The handbook site has none; if added, add a privacy note |
| D12 | John's existing sites | Keep each under its own name, with a shared top bar | Changes go in each site's own repository |
| D13, D16 | Posts per guide article and per article from 36 on | Three for guides 1 to 20, two for 21 to 100; three per article from 36 on | |
| D14 | Article section name | Articles, at `/articles/` | |
| D15 | Research studies in Guides & Labs | Feature them, after the two research items below are settled | |

## What has changed since the plan

The plan was written on October 2, before the handbook site was built. Read it with these changes in mind.

- **Handbooks are their own sites.** The plan imported the handbook into the hub from Word (its "Word handbooks and PowerPoint decks as web pages" section and the `/handbooks/ai-control-plane/...` addresses). That is overtaken. The handbook is a separate site whose HTML pages are the master, maintained in the AI Control Plane project. The hub's Handbooks shelf links to it, and to the Visual Handbook, and never copies their pages.
- **Downloads.** The handbook site offers only the deck's one-slide PowerPoint files and the toolkit's templates as one Word document. There are no PDF or Word downloads of the handbook itself.
- **Decks live with their handbooks.** The executive deck is a companion on the handbook site, so the plan's Decks section can become cards that link there, or fold into the Handbooks shelf. Settle this when building the top bar.
- **The toolkit is public** (plan D5 said it would wait). Articles 45 to 50, drawn from the toolkit, can link to its pages.
- **Employer review and the disclaimer** (plan D10 and its disclaimer wording) are replaced by the public-edition approach: public information only, no job titles, only publicly available capabilities with no GA labels or roadmap, and the disclosure line in every footer (file 2).
- **The plan's private working repository is not needed.** Internal notes, punch lists and LinkedIn drafts live in this Claude project's files, never in the public repository.

## How the hub relates to John's other sites

- The hub is the user site. The handbook and the other project sites keep their addresses beneath it, for example `/ai-control-plane-handbook/` and `/Python-Visual-Guides/`.
- Never rename an existing repository: its site address would change, and GitHub does not redirect it.
- Never give a hub folder the same name as a repository, so no hub path ever collides with a project site.
- The Visual Handbook and Python, Visually address their pages by fixed slugs. Keep linking to those slugs, and ask before anything changes them.
- **Handbooks shelf:**
  - the AI Control Plane handbook (Published, edition 2026.1);
  - Statistics, Data Science and AI: A Visual Handbook (Hands-on, on its own site);
  - the planned Data Science, Statistics, and AI and Python Development Trends handbooks, marked "Coming next".
- **Guides & Labs:** cards for Python, Visually, the agent network and the study sites, as the plan's guide-article tables map them.

## Rules carried over from the handbook

- **Naming rule:** in the project instructions, pasted by John. In short, call integration capabilities MuleSoft (connectors, APIs, MCP Bridge) and the control plane MuleSoft Agent Fabric. CloudHub and Runtime Fabric may be named. The banned word never appears anywhere, so scans decode it at run time.
- **Public edition:** public information only; only publicly available capabilities, with no GA labels or roadmap; no job titles; the disclosure line in every footer.
- **Citations:** a superscript endnote for every sourced fact, numbered in order of first citation within each article. A source's name appears in the text only when the same sentence carries its endnote. Illustrative numbers are labelled. Survey figures are quoted on their own terms.
- **About page:** reuse the handbook's approved "About John Fisher" text (https://johnfisher-ai.github.io/ai-control-plane-handbook/handbook/appendix-e.html), adapted for the hub. Contact is via LinkedIn, https://www.linkedin.com/in/johnrfisher.
- **Style:** plain, specific English, the same standard as the handbook's October 14 style pass.
  - Short sentences, and the claim first.
  - No hype words or superlatives without evidence.
  - None of the stock phrasing that reads as machine-written.
- **No third-party files:** link to them instead of hosting them.

## Design system (shared with the handbook)

| Token | Value |
|---|---|
| Navy | `#0F172A`, with `#1E293B` for surfaces |
| Sky | `#0284C7`, light `#38BDF8` |
| Light background | `#F8FAFC` |
| Violet (the plus in the AI+ mark, and Guides & Labs) | `#7C3AED`, as the Visual Handbook uses |
| Typeface | Plus Jakarta Sans, self-hosted (the handbook repository's `assets/fonts/`, with `OFL.txt`) |

- Light and dark mode both follow the visitor's system setting. The handbook's `assets/css/site.css` is the reference for the tokens, the dark-mode values and the link colours.
- The mark is "AI+" on a rounded tile, with the plus in violet; it must read at favicon size.
- Social cards are 1200 × 630.

## How work flows

- **Who does what:** John pushes with GitHub Desktop. Claude writes into the connected folder (`~/Projects/johnfisher-ai.github.io`) and never pushes; a GitHub token is never needed.
- **Live tests:** Claude's cloud workspace cannot reach github.io, so live tests run in the desktop app's built-in browser. GitHub's own pages need John's approval for each page load, so check the repository through `git clone` and `git ls-remote`, which work from the workspace.
- **Before every delivery:** the HTML validator, axe at 1280 px light and 375 px dark, internal links and anchors, and the banned-word scan.
- **External links:** check them with the W3C Link Checker at each release.
- **Previews:** John checks each article's LinkedIn preview with Post Inspector before posting.
- **Change summaries:** every summary says what changed and what John commits. Keep the punch list current in the project files.

## Open items from the plan to check

These were open on October 2, 2026; confirm whether they are done.

- **Research items (plan Section 12):**
  - The nursing study's notebook embeds the 19 survey responses, though that repository's own rules hold row-level data back until the authors and the IRB approve. Record their approval, or switch the notebook to synthetic data.
  - The patient-aggression manuscript is public while under review: confirm the journal's posting policy with the corresponding author.
- **Five wording fixes on the Visual Handbook:**
  - "100+ Python notebooks" on its contents page against 345 on its home page;
  - "every chapter has a notebook" when 10 of 205 have none;
  - "real, messy datasets" when `data/README.md` says every dataset was written for the book;
  - the ANOVA chapter's contents line lists ANCOVA, which it does not cover;
  - the infographics page still calls Chapters 1 to 29 "this book so far".
- **The agent network** needs an OpenAI key for a live run: say so on its card.
- **AgenticFrameworkNotebook** has no license or material yet: add both, or leave it unlinked.
- **Before launch:** check the domain, the LinkedIn newsletter name and a trademark search on "AI+".

## Proposed first milestone

1. **Skeleton:**
   - the home page and the top bar (the plan's Home · Handbooks · Articles · Decks · Guides & Labs · About, with Follow on LinkedIn; Decks only if it stays a section);
   - About, with the disclosure, the licenses and how to cite;
   - the Handbooks shelf and the Guides & Labs page;
   - search, RSS for articles and guides, and the 404 page;
   - checks run on every delivery.
2. **Launch content, from the plan's phases:** articles 1 to 5, 56, 57, 81 and 108, and guide articles 1, 2 and 41, each with its card image and LinkedIn posts.
3. **Launch:** the first week of posts. The guide lanes start three and five weeks later, as in the plan's calendar.
