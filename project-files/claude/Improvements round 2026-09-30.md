# Improvements round, September 30, 2026

John asked for recommendations to improve the handbook, the executive deck and the assessment toolkit, drawing on 2025–2026 work from Google, Microsoft, AWS, Deloitte, KPMG and BCG and the main standards bodies. Claude wrote twenty recommendations (R1–R20) in the Claude Docs doc "AI Control Plane: recommended improvements"; John then asked to implement all of them.

- **Handbook:** tracked changes by "Claude" in John's master, with 38 comments that each start "Improvements round, Sept 30, 2026 (R#)". John reviewed the round and accepted the changes on September 30, 2026; no tracked changes or comments remain.
- **Endnotes:** 40 new sources; all renumbered in first-citation order, 1–100 main sections and 101–119 reference use cases (the project instructions field still shows the old ranges until John edits it).
- **Executive deck:** rebuilt, 64 slides (seven new). **Toolkit:** guide (about 130 pages, new template T13), client report template (32 pages) and client deck (51 slides) rebuilt.

## Where each recommendation landed

Endnote numbers are the new ones. "Guide" is the SE and AE toolkit guide; "template" is the client report template.

| # | Recommendation | Handbook | Executive deck | Toolkit | New endnotes |
|---|---|---|---|---|---|
| R1 | 2026 "why now" evidence | Section 1 (four surveys, each on its own terms) | Slide 4 | Guide Section 1 callout | 7, 8, 9, 10 |
| R2 | Payback benchmarks beside the milestones | Section 8 | Slide 27 band | Guide Section 6, T2, T11; template Section 11; client deck slides 23 and 46 | 94, 95, 96 |
| R3 | The value of orchestration and reuse | Sections 1 and 3 | Slide 4 band; notes | — | 4, 20 |
| R4 | Operating model: owners, decision rights, skills | Section 8 (roles table) | Slide 28 | Guide Section 6 and new T13; template Sections 10 and 12; client deck slides 24 and 47 | 96, 97, 98 |
| R5 | Agent lifecycle, with sponsors and recertification | Section 2; first-90-days box; board question 1 | Slide 8 | Guide Section 3, T3d; use case 1 T3d | 12, 13, 14 |
| R6 | Could AI, should AI (work modes) | Section 8; board question | Slide 28 | Guide Section 2, T1; template Section 2; client deck slides 24 and 47 | 97, 99 |
| R7 | Coexisting with the hyperscalers' agent control planes | Sections 2 and 7 (table and default division of labor) | Slide 25 | Guide Section 5, T10, question bank, questions to expect; template Section 9; client deck slides 18 and 41 | 12, 14, 52, 68 |
| R8 | Protocol facts for 2026 (A2A 1.0, MCP 2026-07-28, AP2) | Section 4 "Open protocols"; endnotes 31 and 32 | Slide 13 and notes | Guide Section 4 table, T5 tips; use case 1 T5 | 31, 32, 33 |
| R9 | Review frameworks (Well-Architected, Cloud Adoption Framework, Google's 20 questions) | Section 6 table; audit mode in phase 1 (Section 8) | Notes, slide 26 | Guide Section 5, T7 design-review checklist, question bank; template Section 7 | 14, 52, 82 |
| R10 | Delegation chains | Section 4 | Slide 15 band | Guide Section 4, T9 delegation check | 41, 42 |
| R11 | Threats mapped to controls (OWASP, Microsoft, MITRE ATLAS) | Section 5 table | Slide 17 | Guide Section 4, T5 threat coverage; template Section 6 | 53, 42, 54 |
| R12 | Tier crosswalk; promotion and demotion | Section 4 | Slide 15 | Guide Section 4, T5; client deck security slides | 38, 39, 40 |
| R13 | Agent identity (NIST NCCoE, IETF) | Section 5 | Notes, slide 16 | Guide Section 4 checklist, T4 and T5 tips; use case 1 SR-01 | 50, 51 |
| R14 | Standards crosswalk for compliance teams | Section 5 and new Appendix C | — | Guide Section 4; control IDs in T4 and T5; template Section 6 | 78, 79, 80, 81 |
| R15 | Human takeover after the kill switch | Section 5; time to contain (Section 9); board question | Notes, slide 19; slide 29 | Guide Section 4, T5, T12; use case 1 OR-03 | 70, 71, 8 |
| R16 | Leading indicators and shared definitions | Section 9 table | Slide 29 | Guide Section 6, T6 library; template Section 11; client deck slides 22 and 45 | 66, 100 |
| R17 | Evaluation as a lifecycle, vendor-neutral options | Section 5; Section 7 footnote | Notes, slides 19 and 24 | Guide Section 4, T4, T10; client deck mapping slides 17 and 40 | 66, 67, 68, 69 |
| R18 | AI cost visibility as a control | Section 4; new scorecard metric (Section 9); board question | Slide 29 | Guide Sections 3 and 6, T6, T11; template Sections 4 and 11; client deck slides 22 and 45 | 8, 14, 27, 28 |
| R19 | Fast-moving facts in one dated place | Section 7 table (as of September 30, 2026) | Slide 58 | Guide Section 5 and conventions; client deck slides 2 and 49 | — |
| R20 | Accessibility and navigation | Contents lines link to their sections | Icons marked decorative | Contents links in the guide and template; client deck icons marked decorative | — |

## Notes for the next round

- The fast-moving facts live in four places that must change together: handbook Section 7, executive deck slide 58, client deck slide 49 and the guide's Section 5 (the data is in `assess_method.js`, `asOf`).
- The client deck's Sources slides are computed from the citations on its slides and in its notes; the guide's and the template's from their superscripts. `handbook_endnotes.json` is regenerated from the handbook and lists only the links a reader sees.
- Survey figures are self-reported and use different definitions; quote each on its own terms and never chart them as one trend. The AP2 standard work at the FIDO Alliance and the IETF and NIST NCCoE identity work are drafts: present them as emerging.
