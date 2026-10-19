# Fact-check log, September 29, 2026

Covers the three files in `deliverables/`: the master handbook (`JRF_AI_Control_Plane_Handbook_Executive.docx`), the executive deck (`JRF_The_AI_Control_Plane.pptx`, changed through its generator) and the quantum briefing (`JRF_Quantum_Security_Executive_Briefing.docx`).

**Method.** Every dated, numbered, attributed or product-status claim was checked against its cited source and, where possible, a primary source: vendor release notes and announcements, government orders and memoranda, and the original research. Sources that could not be opened are flagged below, not guessed.

**How changes were made.** In both Word files, every change is a tracked change by "Claude", and each fact-check change has a comment giving its source. Nothing is final until John reviews and accepts. The deck is generated, so its changes were made in `build/build_deck3.js`, `build/uc_slides.js` and `build/build_uc_diagrams.js`, and the deck was rebuilt.

## Status

| File | What changed | Waiting for |
|---|---|---|
| Handbook | 58 text edits, 41 endnote updates, Figures 4 and 16 re-rendered; 62 comments; Author property John Fisher | John's review, then Accept All |
| Deck | 63 generator edits, presenter filled in, endnote slides generated from Appendix B, source footers aligned; rebuilt, glyph check passed | Nothing |
| Quantum briefing | 17 corrections; eight references replaced by endnotes 1–14 with links; 16 comments; title and Author properties | John's review, then Accept All |

## Handbook and deck corrections

### Product status: MuleSoft Agent Fabric and Salesforce

- **MCP Bridge:** GA March 6, 2026 (was "April 2026"). [MuleSoft Blog](https://blogs.mulesoft.com/news/mcp-bridge/)
- **AI Gateway LLM governance**, including intelligent model routing: GA March 31, 2026 (was "April 2026"; routing was "Available*"). [MuleSoft Blog](https://blogs.mulesoft.com/news/ai-gateway/)
- **Deterministic orchestration** (Agent Script in Agent Broker): announced April 2026; GA moved from June to July 2026 and shipped in the July 14, 2026 release. The language is Agent Script (was "Agentforce Script"). [Release notes](https://docs.mulesoft.com/general/agent-fabric-release-notes)
- **Agent Kill Switch:** GA September 2, 2026 (was "Available*"). [MuleSoft Blog](https://blogs.mulesoft.com/news/stop-a-rogue-agent-in-seconds-agent-kill-switch-is-now-ga/)
- **Agent Visualizer and Agent Evals:** Visualizer has been GA since October 2025. Evals was announced at Dreamforce on September 15, 2026 with no GA date. The status table had "New (Sept 2026)" for both. AI cost controls arrived earlier in 2026, so they are no longer described as a Dreamforce launch. [MuleSoft Blog](https://blogs.mulesoft.com/news/welcome-to-dreamforce-2026-turning-ai-ambition-into-measurable-roi-with-agent-fabric/)
- **Where things run:** CloudHub is MuleSoft-managed; only Runtime Fabric runs on the customer's own infrastructure. Guardrails on Runtime Fabric went GA in April 2026 and agent networks on Runtime Fabric on August 31, 2026 (release notes, endnote 14).
- **Salesforce Trusted Enterprise AI Harness** (announced September 10, 2026) draws on MuleSoft and Agent Fabric. New AI Control Plane capabilities are planned to begin rolling out in early fiscal 2028 (from February 2027). Endnote 41 now cites this global announcement instead of the September 11 Asia-Pacific release. [Salesforce](https://www.salesforce.com/news/stories/enterprise-ai-harness/)
- **Architecture layer:** Data 360 and Informatica are Salesforce products, so the layer now reads "Capabilities and data (MuleSoft, with Data 360 and Informatica)".
- **Use cases:** the realization sections now say to confirm availability of Agent Evals and of per-agent or per-desk budget caps (MuleSoft said in August 2026 that caps were due "later this quarter"). Informatica CLAIRE Agent Skills are labeled preview and the Data Steward Agent as planned for Q4 2026 (endnotes 52 and 53). Omni Gateway has no replay-protection policy, so Figure 16 and the use case 2 slides now say "rate limits".

### Product names

- Azure AI Foundry is now **Microsoft Foundry**, and Google's platform is **Gemini Enterprise Agent Platform (formerly Vertex AI)**. Updated in the handbook text and the deck text and notes. Figure 4 was re-rendered for the Microsoft name. Short "Vertex AI" labels remain in a few places (see judgment calls).

### Security and post-quantum policy

- **US federal post-quantum policy:** Executive Order 14412 (June 22, 2026) and OMB Memorandum M-26-15 (June 24, 2026) bind federal agencies now. The order directs the FAR Council to propose a contractor rule within 180 days; none had been published by September 21, 2026. The handbook now says "For US federal systems, the timeline is now set by policy." Endnote 27 now cites M-26-15; the old entry was a July 16, 2026 Tech Times market story misattributed to MSN. [EO 14412](https://www.whitehouse.gov/presidential-actions/2026/06/securing-the-nation-against-advanced-cryptographic-attacks/) · [M-26-15](https://www.whitehouse.gov/wp-content/uploads/2026/06/M-26-15-Execution-of-the-Migration-to-Post-Quantum-Cryptography.pdf)
- **AI-assisted cryptanalysis:** Anthropic's July 28, 2026 post reports that Claude Mythos Preview found attacks on AES-128 cut to seven of its ten rounds, 200 to 800 times faster than the best earlier attack (only The New York Times printed 1,000), and on HAWK, a candidate post-quantum signature scheme. Deployed standards were not affected. [Anthropic](https://www.anthropic.com/research/discovering-cryptographic-weaknesses)
- **Board guide:** the Director's Handbook on Cyber-Risk Oversight is published by NACD and the Internet Security Alliance (the text had ISA with Carnegie Mellon's Software Engineering Institute). The quantum guide's authors are Gregory Touhill and Larry Clinton. [ISA PDF](https://isalliance.org/wp-content/uploads/2026/06/2026_Directors-Handbook-Cyber-Risk_QuantumComputing.pdf)
- **CISO survey (endnote 20):** the 5th-edition survey is public. The handbook now quotes its finding: only 37% of CISOs report a deep, trusted relationship with the CTO, and 22% with the chief architect. The "yesterday's security model" wording comes from endnote 1 and is now cited there.
- **NVIDIA NemoClaw:** announced at GTC on March 16, 2026 as an alpha early-access preview, not a GA product.
- **Deck slide 13:** the threat list now matches its source (hallucinations and anomalous agent behavior, not tool misuse and drift).

### Research and analyst claims

- **Horizon architecture (endnote 7):** the source says "significant technology challenges" and weak oversight, not "serious technology failures".
- **Endnote 11** has no public copy. Where the same content appears in the endnote 1 article, endnote 1 is now cited too, and the research digest no longer says Bain corroborates it.
- **Bain's phasing (endnote 12)** puts governance and trust first and federation last. The handbook's four-phase roadmap is now presented as its own, and Figure 6 is labeled "author's synthesis".
- **CDO Magazine (endnote 19)** has the scorecard go quarterly to the AI governance board, not the board of directors. Section 9 now says so.
- **Endnote 8 replaced:** the cited piece was a consultancy blog (tailoredd.com) giving 60+ tools and 30+ skills. Salesforce's own Headless 360 announcement (April 15, 2026) supports "more than 100 new tools and skills".
- **Forrester Wave, API Management Software, Q3 2026:** several vendors are Leaders (Kong, WSO2 and IBM also announced Leader placements); the endnote says so.
- **Citations moved** so each sits on the part its source supports, for example ^14,37 on AI cost controls, ^1,23 on the identity fabric, ^1,24 on the time/data/authority/risk bound, and ^1,26 on the perimeter point.
- **Narrative attributions removed** (project rule): "Info-Tech Research Group advises" became "Independent analysts advise", and the CDO Magazine attribution was dropped from the Section 9 scorecard sentence.

### Reference use cases

- **T+1:** the US moved most broker-dealer securities trades, including equities and corporate bonds, to T+1 on May 28, 2024, with broker-dealers required to complete allocations, confirmations and affirmations "as soon as technologically practicable" (SEC release 2023-29). [SEC](https://www.sec.gov/news/press-release/2023-29)
- **Settlement fails:** the 71% (counterparty shorts) and 21% (data issues) figures describe survey respondents' 2024 fails (Firebrand Research, June 2025, cited by Northern Trust, endnote 57), not all fails.
- **Europe:** the EU, UK and Switzerland go live with T+1 together on October 11, 2027 (year added on the deck).
- **SEC Rule 17a-4(f):** since the 2022 amendments, WORM is one of two allowed storage options; the other is an audit-trail system.
- **DORA (deck notes):** an event is logged as an ICT-related incident and reported to the authority only if it meets the major-incident criteria.
- **Security rows:** signed agent cards and mTLS/OAuth are cited to the A2A specification (endnote 45); OAuth-protected MCP servers, scopes and schema validation to the MCP specification (endnote 46). Allow-lists, pinned tool definitions and read/write separation are now labeled firm practice, because the specification does not define them.
- **Standards** now cite their own endnotes: ISO 20022, FIBO and CDM (60–62) and BCBS 239 (63).

## Shared endnotes (1–64)

- **Structure:** 64 entries in order of first citation (1–43 main sections, 44–64 use cases). Every entry is cited at least once.
- **Deck against handbook:** the deck's endnote slides (38–41) are generated from Appendix B and match its text exactly for all 64 entries. The deck omits links by design.
- **Replaced:** 8 (Salesforce Headless 360 announcement) and 27 (OMB M-26-15).
- **Expanded:** 14 (release notes, plus the GA posts for MCP Bridge, LLM governance and Kill Switch); 28 (adds EO 14412; King & Spalding numbers it 14409, the official number is 14412); 32 (adds Anthropic's own post).
- **Updated:** 41 (global announcement, September 10, 2026); 50 (OWASP Top 10 for LLM Applications 2026, August 3, 2026); 51 (the OpenTelemetry GenAI conventions moved to their own repository on June 12, 2026); 26 (links the Microsoft report itself); 1 (link added, "more than 30 expert interviews"); 2 (title and date); plus author, date or link fixes on about 25 other entries.
- **No link:** 11 (no public copy), 33 and 38 (Deloitte-produced content on deloitte.wsj.com, which the checks could not open; author and date unconfirmed).

## Quantum briefing

**Corrections** (tracked, with comments):

- **Who is bound:** the June 2026 order and OMB M-26-15 bind federal agencies now. Contractors will be bound once a FAR rule is proposed and finalized, and critical-infrastructure owners are assisted rather than mandated. An executive order is signed, not "signed into law".
- **Standards:** NIST's PQC standards are published, not codified; FIPS 205 is SLH-DSA.
- **Harvest now, decrypt later** is a risk US government sources warn about, not an observed campaign, and no source dates a cryptographically relevant quantum computer. 2030 is a migration deadline, not a threat date.
- **Deadline table:** end-2030 for key establishment and end-2031 for signatures, in agencies' high value assets and high-impact systems (National Security Systems excluded). 2035 is the end-state goal from NSM-10, CNSA 2.0, M-26-15 and the draft NIST IR 8547, not from the June order. "Zero-tolerance enforcement" was removed (no source).
- **Contractors:** the order does not name SaaS, PaaS, IaaS or managed services, set a proof-of-compliance test or tie compliance to contract eligibility; those details await the FAR rule.
- **Board plan:** now rests on Bain (January 20, 2026) and the NACD–ISA guide; the quarterly cadence is framed as an example.
- **AI multiplier:** Anthropic reports 200 to 800 times (not 1,000); the work was capability research, almost entirely autonomous for AES and semi-autonomous for HAWK. "Years to weeks or days" was replaced with sourced figures: time-to-exploit averaged 63 days in 2018–19 and 5 days in 2023 (Mandiant), and Anthropic's June 2026 tests produced working exploits within hours.
- **Removed:** a sentence citing "MSN Cybersecurity Pulse", which could not be found.

**References.** The eight originals were replaced: [27] ("MSN Cybersecurity Pulse") and [33] ("Swarmia Engineering Governance Series") could not be found, and [28]–[32] and [34] had wrong titles, authors, publishers or dates, with no links. New list, numbered 1–14 in order of first citation (entries shared with the handbook use its wording):

1. The White House, Executive Order 14412, June 22, 2026 (shared with handbook endnote 28)
2. OMB Memorandum M-26-15, June 24, 2026 (handbook endnote 27)
3. Quantum Computing Cybersecurity Preparedness Act, Public Law 117-260, December 21, 2022
4. National Security Memorandum 10, May 4, 2022
5. NIST, first three finalized post-quantum encryption standards, August 13, 2024
6. Buchanan Ingersoll & Rooney (Kurt Sanger and Nathalina A. Hudson), 2026 PQC requirements for federal contractors, September 21, 2026
7. NSA, CNSA 2.0 and Quantum Computing FAQ, version 2.1, December 2024
8. NIST IR 8547 (initial public draft), November 12, 2024
9. Bain & Company, "How businesses can prepare for post-quantum cybersecurity threats," January 20, 2026
10. NACD and ISA, "Board discussion guide on quantum computing," 2026 (handbook endnote 34)
11. Anthropic, "Discovering cryptographic weaknesses with Claude," July 28, 2026 (part of handbook endnote 32)
12. The New York Times (Dustin Volz), July 28, 2026 (handbook endnote 31)
13. Anthropic, "Measuring LLMs' impact on N-day exploits," June 8, 2026
14. Google Cloud (Mandiant), 2023 time-to-exploit trends, October 15, 2024

## Judgment calls for John (not changed)

1. **Narrative attributions** still in the handbook body, against the project rule: Forbes/Nutanix and Gartner (Section 1), HCLTech (Section 2), Bain (Section 3), Airbyte and CDO Magazine (Section 4), and the World Economic Forum, the Cloud Security Alliance and the NACD–ISA guide (Section 5). All are cited correctly; the question is style.
2. **Hedging:** the endnote 1 article hedges three points the handbook states flatly: the next five years "are likely to be shaped" by two uncertainties; agents "increasingly become" the primary consumers and architecture "might need to shift"; and the greater leverage "may be" orchestration.
3. **"Vertex AI"** remains in short labels: the Section 3 paradigm table, deck slides 9, 16 and 18, and so Figures 4 and 5.
4. **Which board:** Section 4 still says the CDO Magazine plan reports "to the board quarterly"; the source says the AI governance board, which Section 9 now uses.
5. **Figure 1** is cited to endnote 1, but the article's only figure shows the three capabilities. Consider "(author's illustration)".
6. **Endnote 35 (AI-native banking):** the article stresses permissioned autonomy and governance built into the product, not output validation, so "illustrate why this matters" is loose.
7. **Endnote 33:** the claim that post-quantum work needs board oversight and cross-functional ownership could not be checked (site blocked). The NACD–ISA guide (34) or Bain could support it.
8. **Endnote 20 date:** the entry says May 2026 (as endnote 1 cites it); Deloitte Australia labels the report April 2026.
9. **Deck slide 14** names RSA and ECC, while endnote 1 speaks of asymmetric cryptography in general. Keep the names only with a source that names them (NIST IR 8547 does).
10. **Deck slide 2** says "continuous trust"; the article's heading is "trust, security, and resilience". A fair paraphrase; keep or align.
11. **Deck slide 9 notes** say hybrid/federated is the pattern Agent Fabric is "designed for" [14]. The product page does not discuss patterns, so this is the author's reading.
12. **Gateway policy cells** in the use case 1 and 2 realization tables cite ^14,16; endnote 16 supports the April expansion but not every listed policy.
13. **Optional updates:** Headless 360's August 2026 expansion and the growth in Agent Scanners coverage are not mentioned. The claim that Microsoft Agent Framework succeeds Semantic Kernel could not be verified, so deck slide 13 notes still say "Microsoft Foundry and Semantic Kernel".
14. **Quantum briefing Section 4, second paragraph** ("A critical architectural vulnerability…") has no source and was left unchanged. It needs a citation or softer wording. The deadline table also has no table style (cosmetic).
15. **Housekeeping:** `build/build_doc3.js` (the reference generator) does not have these corrections. A copy of the handbook outside the project folder (on the Desktop) still has the old content; use the one in `deliverables/`.

## Follow-up, September 30, 2026

John asked for judgment calls 1, 3 and most of the smaller ones to be resolved. The handbook changes are tracked changes by "Claude" with comments starting "Fact-check follow-up"; the deck was rebuilt from the generator. The item numbers below are the judgment-call numbers above; their endnote and slide numbers predate two renumberings, so current numbers are given in brackets.

- **Resolved:** 1 (John's ruling: analyst, publisher and magazine names stay in the text when the sentence carries its endnote, and company and product names are fine; the one uncited mention, HCLTech's second point, now cites it); 2 (the three hedges restored in Sections 1, 3 and 4 and on deck slides 4 and 7); 3 ("Gemini Enterprise Agent Platform" in the Section 3 table and on deck slides 9, 18 and 19, so handbook Figures 5 and 6 were re-rendered); 4 ("AI governance board" in Section 4); 5 (Figure 1 labeled "(author's illustration)"); 6 (the AI-native banking sentence [39] reworded to match its source); 9 (RSA and elliptic-curve now cite OMB M-26-15 [31], in Section 5 and on slide 14); 10 (slide 2 names the three capabilities as the handbook does); 11 (the slide 9 notes separate the sourced fact from the author's reading); 12 (the Omni Gateway agent-policy documentation [53] added to the gateway rows of all three use cases).
- **Still open:** 7 (the board-oversight claim [37] has no checkable source; the NACD–ISA guide [38] could support it); 8 (the CISO survey date [24]); 13 (optional updates); 14 (quantum briefing); 15 (housekeeping); and links for the Deloitte-sponsored Wall Street Journal pieces [37] and [46]. Endnote [12] has no public copy, as its entry says.
