# Public edition: change list (October 2, 2026)

The public edition is a separate copy of the six documents, written as an independent architect's view that realizes the vendor-neutral north star with MuleSoft and Informatica from public information. John works for Salesforce; a disclosure line says so and that the views are his own. The originals in `deliverables/` are untouched (checked by checksum before and after). The rules are in `capability_register.md`.

## Files

| File | What it is |
|---|---|
| `public_edition/JRF_AI_Control_Plane_Handbook_Executive_Public.docx` | Handbook, ready to publish: every change accepted, no comments. 97 pages in LibreOffice. |
| `public_edition/JRF_The_AI_Control_Plane_Public.pptx` | Executive deck, 66 slides, built from `build/public`. |
| `public_edition/JRF_AI_Control_Plane_Assessment_Client_Deck_Public.pptx` | Client deck, 53 slides, built from `build/public`. |
| `public_edition/JRF_AI_Control_Plane_Assessment_Client_Template_Public.docx` | Client report template, built from `build/public`. |
| `public_edition/JRF_Assessing_AI_Control_Plane_Project_Public.docx` | Assessment guide (toolkit), built from `build/public`. |
| `public_edition/JRF_Quantum_Security_Executive_Briefing_Public.docx` | Quantum briefing: the original text (it names no Salesforce, MuleSoft or Informatica product, no roadmap and no job title), with two appendices added: notices and About John Fisher. |
| `public_edition/review/JRF_AI_Control_Plane_Handbook_Executive_Public_REVIEW_tracked.docx` | The same handbook with every change as a tracked change by "Claude" and 131 comments, each starting "Public edition:". For review only: it still contains the removed text, so never publish it. |
| `public_edition/review/capability_register.md`, `CHANGES.md` | Private working files: what may be named, with sources, and this list. |
| `build/public/` | Self-contained generator copy for the public deck, diagrams and toolkit, with the public figures, `handbook_endnotes.json` (107 public endnotes) and `scripts/` (how the edition was made). `build/` itself is unchanged, so the masters still build as before. |

## Notices and About John Fisher (October 2, 2026)

John asked whether the files should disclose or credit the products they name, and for an "About John Fisher" appendix modeled on an example bio, from his LinkedIn profile (he supplied it as a PDF). He chose CC BY-NC-ND 4.0.

| File | Where |
|---|---|
| Handbook | Appendix D "Notices and disclosures" and Appendix E "About John Fisher", each from a new page; contents lines D and E; About this handbook names both, and the disclosure points to Appendix D. Tracked in the review copy, with comments starting "Public edition:". |
| Executive deck | Slides 65 (notices, three columns) and 66 (About), after the endnotes; the closing slide's footer says they follow. |
| Client deck | Slides 52 and 53, after the sources; slide 2's notes say to keep the credit line, the icon credit and the trademark notice in readouts built from Part 2. |
| Guide | Appendices E and F; contents, the Appendices bullet and the disclosure note updated. |
| Client template | On the guidance page (deleted before sending): the license, the toolkit permission, the advice note and About John Fisher. Report-level Appendix E "Notices", which stays in completed reports: the toolkit credit, the trademarks the report names, the icon credit, and prompts for the assessor's vendor relationships and own notices. |
| Quantum briefing | Appendices A and B after References & Endnotes. |

**Notices** (`scripts/notices.py`, one source for all six files):
- Copyright and license: © 2026 John Fisher, CC BY-NC-ND 4.0 with a plain-language summary, a suggested credit, and what the license does not cover (trademarks, the credited icons and typeface, and the sources' material).
- Toolkit only: an additional permission to use and adapt the toolkit for assessments, inside an organization or for clients, including paid work, if each completed report or readout carries "Based on the AI Control Plane Assessment toolkit by John Fisher, used with his permission." It does not cover selling the toolkit or publishing changed versions.
- Disclosure: John works for Salesforce; he wrote the work independently, on his own time and not as part of his work, from public information; the views are his own; it is not sponsored or endorsed by Salesforce or any company named.
- Trademarks: the owner of every mark the file names (Salesforce, SAP, Microsoft, Amazon, Google, Anthropic, OpenAI, Snowflake, Workday, Databricks, Kong, Cloudflare, LangChain, Airbyte, Nutanix, S.W.I.F.T., the American Bankers Association, The Linux Foundation, the OWASP Foundation, The MITRE Corporation and the Rust Foundation, as each file needs), in the wording the owners publish where they publish one, then a catch-all; names identify products only and imply no endorsement or affiliation beyond the disclosed employment.
- Sources and quotations, illustrative material, product information (documentation checked in September and October 2026; custom policies are not MuleSoft products), not professional advice (as is; no liability to the extent the law allows), and credits: Font Awesome Free icons, recolored, CC BY 4.0; in the decks, Plus Jakarta Sans, SIL OFL 1.1.

**About John Fisher:** five short first-person paragraphs from his LinkedIn profile, the same in every file: Salesforce (helping enterprises architect the data foundation: MuleSoft, Informatica, MCP and A2A), fourteen years at TIBCO, his two master's degrees, statistical work at the West Chester Statistics Institute, Aethos, what he writes about, how he uses Salesforce technology as one example of a pattern, and that the views are his own. No job title.

**How it was made:** `notices.py build` reads the previous public files for the marks each names and writes `notices.json`; `notices_gen.py` patches the deck and toolkit generators to render it through `notices_kit.js`; `add_notices_hb.py` adds the handbook appendices to the review copy as tracked changes, and `accept_xml.py` makes the clean copy; `add_notices_quantum.py` adds the briefing's appendices; `notices.py check` confirms that each file's notice names exactly the marks the file names and that every notice paragraph is in the file.

**Checks:** OOXML validation passes for all seven files, and the review copy passes the tracked-change check against John's master; the banned word appears nowhere; the term search adds only false positives (the documents' own titles and "SAP SE"); the handbook's 107 endnotes and their order are unchanged; figures are unchanged except the guide's thumbnail of four template pages, whose page numbers moved; the new pages and slides were rendered and checked; an independent review checked the notice text and the trademark owner statements, and its findings were applied.

**For John:**
1. Confirm the About text. It uses the university's name, "West Chester Statistics Institute"; your LinkedIn profile says "Statistical Institute".
2. The © line and the licenses assume the copyright in this independent work is yours under your employment agreement.
3. The toolkit's additional permission is optional; remove it in `scripts/notices.py` to keep the plain license.
4. Optional: a line on AI assistance in drafting, and the AI+ site URL in the suggested credit once the site exists.

## What changed

**Everywhere**
- No job title: the cover, footer and title slides read "John Fisher" (the toolkit template keeps its "[name, title]" prompt for whoever fills it in).
- The disclosure line: handbook "About this handbook"; executive deck closing slide and slide 1 notes; client deck slide 1 and slide 2 notes; guide "About this toolkit"; template "How to use this template".
- Removed: Agent Evals, CLAIRE agents and skills, agentic MDM, the MDM MCP server, the Agent Fabric Context Catalog, the Data Steward Agent, budget caps and payload optimization, Headless 360 / Headless Toolkit / AIforce, the Salesforce AI Control Plane and Trusted Enterprise AI Harness, NemoClaw, the Forrester Wave line, prices, GA labels and dates, "announced"/"introduced"/"preview"/"rolling out", Dreamforce and TDX, fiscal years, availability and packaging checks, "confirm with the account team", status columns and the product rows of the as-of tables.
- Added or reworded: evaluation runs on any evaluation tool, with Agent Visualizer for quality and risk signals; cost controls are token-based rate limits and spend attribution; Informatica is "the data foundation", with Multidomain MDM reached through governed APIs, Data Governance and Catalog with the CDGC Metadata Search MCP server, and data quality with the Address Verification MCP server; Salesforce "exposes its platform capabilities as APIs, MCP tools and CLI commands"; "roadmap" (the reader's plan) reads "plan"; MuleSoft "can realize" both halves rather than "provides" them; B2B/EDI in place of Partner Manager; no "formerly Flex Gateway".

**Handbook** (tracked in the review copy, by section)
- Cover subtitle without "with MuleSoft Agent Fabric"; "Prepared by John Fisher" on the cover and in the footer; About: "product facts from public documentation" and the disclosure paragraph.
- Contents and headings: Section 7 "Realizing the north star with MuleSoft and Informatica"; Section 8 "The 12- to 24-month plan: value at every phase".
- Sections 1–5: the edits listed above in the executive summary, lifecycle, MuleSoft, routing and cost, tiers, identity, evaluation and shadow-agent paragraphs.
- Section 7: no product history; the job table names LLM Governance and Agent Visualizer; "Informatica: the data foundation for every agent"; "How the realization covers the requirements" (four dimensions, no Trajectory); the requirement-to-capability map rebuilt as two columns without status, footnotes or the roadmap row; "Agent Fabric and Agentforce" without the Harness paragraph; the coexistence table without GA labels or the roadmap; "What to check in any agent platform" (four checks); "Standards and regulation dates" with only A2A, MCP, AP2, the EU AI Act and the US post-quantum deadlines.
- Sections 8–10: plan wording, token limits, evaluation, federation in phase 4; scorecard source "Evaluation results recorded in the registry".
- Use cases 1–3: realization tables and text without Agent Evals, CLAIRE, agentic MDM, the MDM MCP server, the Context Catalog or availability checks; KPI "Within target".
- Appendix A: the rows for endnotes 12, 16 and 29 (public numbers) reworded; Appendix B as below.
- Figures 3, 5, 6, 7, 12, 17 and 22 re-rendered from the public generators (each swap carries a comment); Figure 7's alt text reads "plan".

**Executive deck:** title slide and subject; slides 2, 8, 9 ("Salesforce: capabilities as APIs, MCP tools and CLI"), 10, 12, 14, 16, 19, 21–23, 24 (rebuilt as a two-column requirements-to-capabilities table), 25, 26 ("A 12- to 24-month plan"), 29, 57 (name and disclosure) and 58 ("Standards and regulation dates"); speaker notes in the independent voice throughout; use-case realization slides 35, 44 and 53 and their notes; endnote slides 59–64 regenerated (1–107).

**Client deck, template and guide:** written for architects and project teams (lead architect, engagement lead, project team) rather than SE and AE; readout section names in the third person; no Status columns; "Standards and regulation dates" in place of the fast-moving facts; the same capability changes as the handbook; the guide's "What to check in any agent platform"; figures re-rendered from the public decks; Sources lists recomputed with the public numbers.

## Endnotes

- 107 endnotes, numbered in order of first citation in the public handbook: 1–88 main sections, 89–107 use cases. One list for all five files; the quantum briefing keeps its own 1–14.
- Merged: 17 and 18 into 16; 23, 26 and 89 into 24; 84 and 86 into 87. Dropped: 25, 65, 83, 85 and 90. Launch and general-availability posts give way to documentation pages in 16, 24, 68, 87 and 88.
- Master to public: 1–16 → 1–16; 19–22 → 17–20; 24 → 21; 27–64 → 22–59; 66–82 → 60–76; 87–88 → 77–78; 91–119 → 79–107.

## How it was made (build/public/scripts)

1. `deck_pub.py`: content changes to the deck and diagram generators (master numbering).
2. Toolkit generators re-audienced (assess_*.js, guide_part*.js, build_assess_*.js).
3. `run_pub.py` with `pub_spec.py`: the handbook copy, as tracked changes with comments, renumbered; `accept_xml.py` makes the clean copy by accepting at the XML level (nothing else in the package changes).
4. `remap_pub.py`: every citation in the generators renumbered to the public list; the deck's endnote array, the endnote slides and `handbook_endnotes.json` regenerated.
5. `review_fixes.py`: fixes from an independent review pass.
6. Builds: `npm run deck`, `node build_uc_diagrams.js`, `python3 render_figs.py diagrams`, `python3 render_figs.py deckfigs out/JRF_The_AI_Control_Plane.pptx`, `npm run assess`. `check_terms.py` and `check_endnotes.py` are the checks below. `trackedit.py` and `blocks.py` are the tracked-change helpers the handbook scripts use.

## Checks

- The banned word appears in no part of any of the seven files (text, Office XML, notes, properties).
- Term search (status words, removed capabilities, vendor voice, titles) on every file; each remaining hit is a false positive: titles of cited sources, the client's own pilots and plans, protocol dates, the reader's own questions, vendor-neutral practice words in the vendor-neutral architecture, and "Informatica from Salesforce" as the title of the page cited in endnote 77.
- An independent review of the full text of all six files against the rules; its findings were fixed (the quantum briefing items are left to John below).
- Handbook: superscripts run in first-citation order 1–107 and match Appendix B; Appendix A follows; all 125 endnote link texts match their targets; the review copy passes OOXML validation including the check that every change is tracked; the clean copy passes OOXML validation and was rendered and checked page by page where it changed.
- Decks and toolkit: OOXML validation passes for all four; no glyphs outside the embedded font; no table word breaks mid-word; Sources lists match the citations; the changed slides and pages were rendered and checked; handbook Figures 3, 5, 6 and 7 match the final deck's slides exactly.

## For John

1. Publish the six files in `public_edition/`. The review copy is for reading only.
2. Optional for the quantum briefing, which ships unchanged: the subtitle says "Strategic Roadmap" and the introduction says "This upgraded framework". Neither concerns a product, but you may prefer "Strategic Plan" and "This briefing".
3. Later edits to the master generators in `build/` need carrying across to `build/public/` if the public edition should follow them.
