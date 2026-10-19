# Structure and ROI round (September 29, 2026)

**Status: applied; waiting for John's review.** Handbook changes are Word tracked changes by "Claude" with 19 comments, each starting "Structure and ROI round". The deck was rebuilt from the generator (55 slides).

## Request and decisions

John asked for three things:

1. Put the target reference architecture before MuleSoft Agent Fabric: thought leadership first (research, where the industry is heading, what leaders are weighing), then a recommended north-star architecture, then "MuleSoft Agent Fabric and Informatica: how to realize the north star."
2. Make it clear in Section 8 that ROI and business value arrive in every phase of the 12- to 24-month roadmap, with a couple of quotable sources; phase the three use cases with milestones, ROI and business value at each, and a final phase where all goals are met.
3. Review all section, figure and endnote numbering afterwards.

Decisions (John, September 29, 2026): expand Section 8 rather than add a section; make Section 6 vendor-neutral, with MuleSoft and Informatica only in Section 7; update the deck in the same pass.

## What changed

**Handbook**
- Section 6, "Target reference architecture: a north star for the AI control plane": new intro that synthesizes Sections 1–5 (endnotes 2, 4, 5, 6, 7), the design rule, a new vendor-neutral Figure 4, six layer bullets including "Across every layer", and "Principles that make it a north star". The former Section 7 is shown deleted.
- Section 7, "MuleSoft Agent Fabric and Informatica: realizing the north star": new intro; "The north star, realized" with Figure 5 (re-rendered with Informatica labels and a cross-cutting band); "Informatica: trusted data for every agent"; an Informatica row in the requirement-to-capability map (status "GA; MCP servers rolling out").
- Section 8, "The 12- to 24-month roadmap: value at every phase": two lead paragraphs on value (new sources below); Figure 7 re-rendered with a value box per phase; "Value at every milestone" (value and evidence at months 3, 8, 14 and 24); "Phasing in the use cases" (a table of the three use cases by milestone); "The north star reached: all goals met"; a new first-90-days bullet.
- Section 9: new "Value realized" metric. Section 10: new question on value per phase. Executive summary: the key takeaway and the Phase 1 decision now include value in every phase and the first use-case slice.
- Sections 11–13: each ends with "Phased implementation: value at every milestone" (table plus notes).
- Figures 8–22 renumbered (+1); cross-references updated (custom policies now Section 7; reference architecture now Section 6).

**Deck (55 slides)**: 17 north star (new); 18 realized architecture (moved, retitled, Informatica added); 19 capability map; 20 "Why Agent Fabric" with an Informatica row; 21 roadmap with value per phase; 22 "Value at every milestone" (research tiles and the use-case matrix, new); 23 ten-metric scorecard; phased-delivery slides 31, 40 and 49; executive summary and closing updated; endnotes on slides 52–55. Handbook Figures 1–7 are crops of slides 5, 8, 12, 17, 18, 19 and 21.

## New sources (endnotes 56–58)

- 56. PwC, "CEO confidence in revenue outlook hits five-year low – as AI becomes a defining divide between leaders and laggards: PwC 2026 Global CEO Survey," press release, January 19, 2026 (4,454 CEOs, 95 countries). [Link](https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-global-ceo-survey.html). Verified: 56% of CEOs "have seen no significant financial benefit to date"; 12% report both cost and revenue benefits; CEOs whose organizations have strong AI foundations "are three times more likely to report meaningful financial returns."
- 57. Dan Tinkoff, Lieven Van der Veken, and Michael Chui, with Tara Balakrishnan, "The state of AI in 2026: On the road to ROI," McKinsey & Company, August 25, 2026 (1,719 participants, May 4–June 8, 2026). [Link](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai). Verified: 37% attribute at least some EBIT impact to AI; high performers about 6%; nearly three-quarters of high performers fundamentally redesign workflows; "avoid simply accumulating tools or pilots and instead … build a repeatable capability."
- 58. Aditya Challapally, Chris Pease, Ramesh Raskar, and Pradyumna Chari, "The GenAI Divide: State of AI in Business 2025," MIT NANDA, July 2025. [Public copy](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf). Verified: "95% of organizations are getting zero return"; "Embedding in non-critical or adjacent processes with significant customization, demonstrating clear value, then scaling into core workflows is critical"; top performers averaged 90 days from pilot to full implementation, enterprises nine months or longer.

Gartner's June 2025 prediction (endnote 5: over 40% of agentic AI projects canceled by end of 2027 over cost, unclear value or inadequate risk controls) is reused in Section 8. All sources are cited by endnote only; the text does not name the publishers.

## Endnote renumbering

79 endnotes, first-citation order: 1–58 main sections, 59–79 use cases. Changes from the previous numbering: 49→48, 61→49, 48→50, 62→51, 63→52, 50→53, 51→54, 52→55, 53–60→59–66, 64–73→67–76, 74–76→77–79. New: 56 (PwC), 57 (McKinsey), 58 (MIT NANDA). John needs to update the ranges in the project instructions.

## Phasing values (illustrative, before platform, model and change costs)

Milestones at months 3, 8, 12 and 24. Run rates are derived from each use case's business case; cumulative value counts each run rate from its milestone. The use cases are different industries: never add them up.

| Use case | Month 3 | Month 8 | Month 12 (KPI targets met) | Cumulative by month 24 |
|---|---|---|---|---|
| 1. Engagement launch (10,000 launches a year) | ~$0.5M (1,000 launches × 4 h × $120) | ~$8M (capacity $3.6M + utilization $4.5M) | ~$30M (full business case) | ~$33M |
| 2. T+1 settlement (1,500 exceptions a day) | ~$0.8M (300/day × 5 min × 250 days × $125/h) | ~$5.5M (175 analyst hours a day) | ~$9.8M, plus fewer fails and penalties | ~$12M |
| 3. Compressor reliability (40 stations) | ~$0.4M (2 outages × $180K + 480 engineering hours) | ~$1.8M (6 outages; 5 h per event) | ~$3M (full business case) | ~$3.8M |

## Open items

- John: review and accept the tracked changes; update the project instructions' endnote ranges; check the phasing values against each client's baseline.
- Carried over: Michael S's six predicates, policy citation and preprint DOI, and his energy scenarios; "Vertex AI" mentions (deck slides 9, 18, 19; handbook Figures 5 and 6 and the Section 3 table); links for endnotes 37 and 46.
