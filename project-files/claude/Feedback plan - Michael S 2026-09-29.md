# Plan: incorporating Michael S's feedback (September 29, 2026)

**Status: applied on September 29, 2026; waiting for John's review.** The handbook carries the changes as Word tracked changes by "Claude" with 16 comments, each starting "Feedback round". The deck was rebuilt from the generator (50 slides). The plan below (sections 1–8) is kept as written; its slide numbers refer to the 41-slide deck from before this round. Michael's feedback is at the end of this doc, as received.

## Outcome

**John's decisions (September 29, 2026)**

- Use case 3: build an energy, utilities and oil and gas use case now, from public sources; add Michael's scenarios later.
- Michael's policies: name them now and explain what they do, described as custom Omni Gateway policies (custom policies are straightforward to build on MuleSoft).
- Scorecard: keep the coverage metric (renamed "Oversight coverage") and add an "Oversight effectiveness" row.
- OT: a new deck slide after slide 15.

**Applied**

- **Small fixes:** the colon after "interact" restored; Headless 360 described as the Headless Toolkit behind AIforce (Section 3, the Appendix A row, slide 7); slide 10's LLM Governance GA date corrected to March 2026 (missed in the fact-check); the placeholder line removed from the closing notes.
- **Oversight (item 2):** Section 4 gains a paragraph on exercisable oversight (Green; Sterz et al.; EU AI Act Articles 14 and 26), tier-table controls "Approvals bound to the exact action and time-limited; read-only tools" (Level 1) and "Spend and exposure limits" (Level 3), and a safe-defaults paragraph under Figure 3. Section 5 adds the exercisable-oversight sentence; Section 6 a fifth "What to verify" point, "Oversight you can exercise"; Section 8 phase 3 "approvals bound to actions; kill-switch and approver drills"; Section 9 "Oversight coverage" plus "Oversight effectiveness"; Section 10 two questions. Use cases 1 and 2: approvals bound to the exact change and time-limited (use case 2: expiring before the cutoff), and use case 2's daily borrow limit held across agents and sessions. Deck: slide 12 (tier controls and an "Oversight must be exercisable" line), 13, 15 ("Keep humans able to intervene"), 20 (roadmap) and 21 (nine-metric scorecard; board questions 7 to 10 in the notes).
- **Exposure limits (item 4):** a Section 4 paragraph on limits that hold across calls, agents and sessions; slide 10 notes.
- **OT (item 3):** Section 5 subsection "When agents can move equipment" (four design rules; IEC 61511, the joint CISA and ASD guidance, ISA/IEC 62443, NIST SP 800-82 Rev. 3, EU AI Act Annex III); the Section 7 design rule; a Section 10 question; new deck slide 16.
- **Policies (item 4):** Section 6 subsection "Extending the gateway with custom policies" (Approval-to-Execution Binding; Cross-Session Aggregate-Risk Gate; decoy and honeytoken policies), stated plainly as custom policies, not MuleSoft products; a "Custom (PDK)" row in the capability map and a "Custom" row on deck slide 18; decoys added to "Plan for shadow agents" and to the slide 17 notes.
- **Use case 3 (Section 13; deck slides 38–45):** compressor reliability at a natural gas transmission operator, persona Elena Morales, Figures 17–21, all figures illustrative. Sources: PHMSA 49 CFR 192.631 (control room management) and Part 192 Subpart N (operator qualification), TSA Security Directive Pipeline-2021-02F, and the joint CISA and ASD guidance.
- **Endnotes:** 12 new sources; all 76 renumbered in order of first citation (1–52 main sections, 53–76 use cases); number changes tracked; Appendix A renumbered, with new rows for endnotes 23 and 43; the deck's endnote slides regenerated from Appendix B on four slides (47–50).
- **Figures:** 3 (tiers) and 6 (roadmap) re-rendered from the rebuilt deck and swapped in the handbook; Figures 17–21 added.

**Not done**

- The refinery example: no public source yet.
- Endnote 32 (formerly 28) still leads with the King & Spalding summary; Executive Order 14412 is cited inside it as "see also". Optional.
- Scorecard: aggregate-limit refusals are not counted under "Policy enforcement" (the plan listed this as an option).
- The project instructions still give the old endnote ranges; John updates them (now 1–52 and 53–76).

**Open items**

- For Michael: the six predicates of Approval-to-Execution Binding (the handbook says "six predicates, including…") and how the separate attester works; whether the policies can be cited publicly and whether "P4A" should appear (it does not today); the DOI for the decoy and honeytoken preprint (a comment marks where it goes); a public source for the refinery example; and his energy and oil and gas scenarios for use case 3.
- For John: review the tracked changes and comments in Word, accept, delete the comments and save; update the ranges in the project instructions.

## Baseline (before this round)

- **Handbook:** all tracked changes from the fact-check have been accepted and the comments removed (saved in Word on September 29). The text matches the fact-checked version except for one stray edit: the colon after "interact" is missing in Section 3, "Start with capabilities, not channels" ("…the places people interact websites, mobile apps and contact centers"). Restore it in the next pass.
- **Deck:** unchanged since the September 29 rebuild (41 slides).
- **Quantum briefing:** its fact-check tracked changes were still waiting for review when this plan was written; John has since accepted them.

## 1. The claims Michael flagged: all verified

He could not find these and suspected AI-filled detail. All of them exist in primary sources.

| Claim | Result | Evidence | Action |
|---|---|---|---|
| Anthropic's Claude Mythos Preview broke reduced AES and HAWK (endnotes 31–32) | Verified. Anthropic's post of July 28, 2026 reports an attack on AES-128 reduced to 7 of its 10 rounds, 200 to 800 times faster than the best earlier attack, and a stronger attack on HAWK, a NIST third-round candidate. It says no production software has to change. Independent coverage: The Quantum Insider, The Decoder, DeepLearning.AI's The Batch. | [Anthropic](https://www.anthropic.com/research/discovering-cryptographic-weaknesses) · [The Quantum Insider](https://thequantuminsider.com/2026/07/29/ai-finds-new-weaknesses-in-cryptographic-algorithms-anthropic-says/) | Keep. The "1,000×" he saw came from The New York Times and was removed in the fact-check; the text now says 200 to 800. |
| The June 22, 2026 executive order and its 2030/2031 deadlines (endnotes 27–30) | Verified. Executive Order 14412, "Securing the Nation Against Advanced Cryptographic Attacks": post-quantum key establishment in high value assets and high-impact systems by December 31, 2030, and digital signatures by December 31, 2031; the FAR Council must propose, within 180 days, a rule requiring covered contractors to comply by December 31, 2030. OMB M-26-15 (June 24, 2026) implements it. | [EO 14412 (White House PDF)](https://www.whitehouse.gov/wp-content/uploads/2026/06/eo-14412.pdf) · [Federal Register public inspection](https://public-inspection.federalregister.gov/2026-12909.pdf) · [OMB M-26-15](https://www.whitehouse.gov/wp-content/uploads/2026/06/M-26-15-Execution-of-the-Migration-to-Post-Quantum-Cryptography.pdf) | Keep. Optional: lead endnote 28 with the order itself rather than the King & Spalding summary. |
| Dreamforce naming: "Trusted Enterprise AI Harness" / "AI Control Plane", September 11 | Both names are real, and so is AIforce; they are separate announcements. The Harness and its AI Control Plane were announced on September 10 (September 11 is the Asia-Pacific release; the handbook already cites September 10). AIforce, the interface layer (Claudeforce, Slackforce, Agentforce Coworker and the Headless Toolkit), was the Dreamforce keynote announcement on September 15–16. Salesforce's own Dreamforce recap (September 24) covers both. | [Salesforce, Sept 10](https://www.salesforce.com/news/stories/enterprise-ai-harness/) · [Salesforce, "Five Big Ideas Coming Out of Dreamforce 2026," Sept 24](https://www.salesforce.com/news/stories/five-dreamforce-2026-takeaways/) | Keep. Add AIforce and the Headless 360 rename (item 5). |
| Agent Broker GA in June 2026 (he lists it as checking out) | GA was July 14, 2026, after a month in beta. June was the original target. | [Agent Fabric release notes](https://docs.mulesoft.com/general/agent-fabric-release-notes) · [MuleSoft Blog, July 14, 2026](https://blogs.mulesoft.com/news/guided-determinism-in-agent-broker/) | Keep "GA (July 2026)". |

## 2. Human oversight: ability, not assignment

**The gap.** The scorecard's "Human oversight" metric (share of tier 3–4 high-risk actions with approval or audit) shows that someone was assigned, not that they could have intervened in time. Proposed principle: oversight counts only when the person has the authority, the information and the time to act, and a stop path that works. Every approval and every signal the control plane relies on has a validity window, with a defined safe default when it lapses.

**Sources to add (verified):**
- EU AI Act, Article 14(4): the people overseeing a high-risk system must be able to understand its limits, stay aware of automation bias, override or reverse its output, and interrupt it "through a 'stop' button or a similar procedure" that brings it to a halt in a safe state. [AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14)
- EU AI Act, Article 26(2): deployers assign oversight to people with the necessary competence, training and authority, and give them support.
- Timing: after the Digital Omnibus on AI (in force July 27, 2026), high-risk obligations apply from December 2, 2027 for Annex III systems and August 2, 2028 for Annex I. [Lewis Silkin](https://www.lewissilkin.com/insights/2026/07/27/the-digital-omnibus-on-ai-enters-into-force-today-102nedo)
- Ben Green, "The flaws of policies requiring human oversight of government algorithms," Computer Law & Security Review 45 (2022): oversight requirements can give a false sense of security because people often cannot perform the oversight functions. [arXiv](https://arxiv.org/abs/2109.05067)
- Sarah Sterz et al., "On the quest for effectiveness in human oversight," ACM FAccT 2024: effective oversight needs causal power, epistemic access, self-control and fitting intentions, mapped to Article 14(4). [arXiv](https://arxiv.org/abs/2404.04059)
- The refinery example from the LinkedIn post: use it only with a public source, ideally the incident investigation report.

**Handbook**
- **Section 4, "Tier autonomy and bind each tier to controls":** after the opening paragraph, add two or three sentences separating assigned oversight from the demonstrated ability to intervene. In the tier table, sharpen Level 1's "Approval gates" to approvals bound to the exact action and time-limited. Under the table, state the safe defaults (the handbook's own recommendation): an expired approval blocks the action and asks again, and stale telemetry drops an agent to propose-only until it recovers.
- **Section 5, "Govern output integrity and protect human judgment":** next to the existing automation-bias sentence, add the oversight-illusion point (Article 14; Green; Sterz et al.).
- **Section 6:** in "What to verify before you commit", add a fifth point, "Oversight you can exercise": approvals bound to the executed call, expiry checked at the gateway, stop drills. In the requirement-to-capability map, add a row "Approval bound to the executed action": Trusted Agent Identity with mobile approval (GA), plus binding and expiry checks as a custom Omni Gateway policy (item 4).
- **Section 8 roadmap, phase 3 (months 9–14):** add approver drills and fail-closed handling of expired approvals next to "kill-switch drills".
- **Section 9 scorecard:** rename the current row "Oversight coverage" and add "Oversight effectiveness", for example the share of high-risk actions executed exactly as approved and within the approval's validity window, plus the time to stop an agent in a drill. Data: Trusted Agent Identity logs, gateway policy events, drill records. Alternative: replace the row to keep eight metrics.
- **Section 10:** add "Could the person who approves our riskiest agent actions actually stop one in time, and when did we last prove it?" and "What happens by default when an approval expires or monitoring goes quiet?"
- **Use cases:** in use case 1 (the SAP write needs independence cleared, partner approval and a signed letter) and use case 2 (SSI changes, the approval token for SSI and payment writes, "agents cannot approve their own proposals"), say that approvals are bound to the exact change and expire, for example before the settlement cutoff. Optional day-in-the-life beat: an approval lapses and the write holds until someone re-approves it.

**Deck**
- **Slide 12 (tiers):** one line under the tiers, for example "Oversight must be exercisable: approvals bound to the action, time-limited, fail closed"; sources in the notes.
- **Slide 13 (identity):** the mobile-approval bullet adds "bound to the exact action and time-limited".
- **Slide 15 (output integrity):** card 4 "Keep humans central" becomes "Keep humans able to intervene" (automation bias, override, stop).
- **Slide 19 (roadmap):** phase 3 adds approver drills.
- **Slide 20 (scorecard):** oversight coverage plus effectiveness; the notes add the two board questions.
- **Slides 25 and 33 (component interaction), notes:** binding and expiry at the approval steps.

## 3. Physical and OT operations

**The gap.** Everything today is enterprise IT. When an agent can command equipment, the gateway is one layer among several. Independent safety layers (safety instrumented systems, hardwired interlocks, relief devices) must be able to act whatever the agent does, and people stay responsible for functional safety.

**Sources**
- Verified: joint guidance "Principles for the Secure Integration of Artificial Intelligence in Operational Technology" (CISA, Australia's ACSC and seven partner agencies, December 2025). Key points: "Ultimately, humans are responsible for functional safety"; limit active control of OT by AI without a human in the loop; build failsafes so AI systems fail gracefully; add "how to bypass or replace an AI system" to functional safety procedures. [ACSC PDF](https://www.cyber.gov.au/sites/default/files/2025-12/principles-for-the-secure-integration-of-artificial-intelligence-in-operational-technology.pdf)
- Verified: EU AI Act Annex III, point 2. AI used as a safety component in the management and operation of critical digital infrastructure, road traffic, or the supply of water, gas, heating or electricity is high-risk, so Article 14 applies to it from December 2, 2027. [AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3)
- To confirm at drafting: NIST SP 800-82 Rev. 3 (OT security), the ISA/IEC 62443 series (industrial cybersecurity) and IEC 61511 (safety instrumented systems).

**Handbook**
- **Section 5:** a new short subsection after "Establish AI-specific runtime controls", for example "When agents can move equipment". The control plane governs what agents may request; the safety layer decides what equipment may do; the two stay independent. The safe state is set by process-safety engineering, not by the gateway, so "fail closed" means "fall back to the engineered safe state", which is not always "stop".
- **Section 7:** one sentence on the "Infrastructure and resilience" layer or the design rule: for cyber-physical systems, the control plane sits above the safety layer and never replaces it.
- **Section 10:** add "Where can an agent's action reach physical equipment, and what independent layer stops it if the agent is wrong?"
- **New reference use case 3** (energy, utilities or oil and gas), built from Michael's scenarios. Same structure as use cases 1 and 2: overview, business case (illustrative), KPIs, vendor-neutral architecture with a safety-architecture layer, a day in the life, component interaction, and realization with MuleSoft Agent Fabric and Informatica.

**Deck**
- A new slide after slide 15 (or a callout on slide 13 or 15), "When agents can move equipment", showing the layers: agent, control plane, OT boundary, control system, independent safety layer.
- **Slide 18 notes:** the OT sentence.
- **Use case 3:** about eight slides mirroring slides 21–28. The closing and endnote slides move back.

## 4. Michael's gateway policies and decoys as evidence

**Framing.** Omni Gateway, formerly Flex Gateway ([Futurum, May 13, 2026](https://futurumgroup.com/insights/mulesoft-omni-gateway-as-close-to-an-agent-control-plane-as-it-gets)), supports custom policies written in Rust and compiled to WebAssembly with the Policy Development Kit ([MuleSoft docs](https://docs.mulesoft.com/pdk/latest/policies-pdk-develop-custom-policies)). Michael's policies are custom, not MuleSoft products, so under the GA-versus-roadmap rule they get their own label, for example "custom policy (field-built)". The included agent policies in [MuleSoft's list](https://docs.mulesoft.com/gateway/latest/agent-policies) cover access control, allow and block lists, schema validation, PII detection, guardrails and token-based rate limits. None of them binds an approval to the executed call or enforces a shared exposure budget across sessions, which is why these two are worth showing. Check the overlap with Trusted Agent Identity's mobile approval first: if it already ties an approval to one transaction, present the custom policy as adding expiry against the gateway clock, the separate attester and coverage of MCP and A2A calls.

- **Approval-to-Execution Binding** (the runtime for item 2)
  - Handbook: a short box in Section 6, "Extending the gateway with custom policies", after the requirement-to-capability map; the new map row from item 2; the use case 1 and 2 "Realizing the use case" tables (the SAP write gate; SSI and payment writes).
  - Deck: slide 17 notes (or a footnoted row); notes on slides 26 and 34.
  - Regulatory mapping: EU AI Act Article 14(4)(d)–(e) and Article 26(2). The two-person verification in Article 14(5) applies only to remote biometric identification, so present the separate-attester check as maker-checker practice (as use case 2 already does), not as an Article 14 requirement.
- **Cross-Session Aggregate-Risk Gate** (limits on what agents do, not only on what they spend)
  - Handbook: the Section 4 cost-control paragraph ("Route every task to the right model, place and price") and the Level 3 row ("financial and computational circuit breakers"); the Section 6 "Economics" point; use case 2's rule that agents may book internal borrows "up to a notional limit per trade and per day", where the per-day limit across agents and sessions is exactly what a per-call gate misses; use case 1's token budgets per launch.
  - Deck: slide 10 notes (cost), slide 12 (Level 3 controls), slides 30, 33 and 34 (borrows within limits).
  - Scorecard option: count aggregate-limit refusals under "Policy enforcement".
  - Overlap: MuleSoft's per-agent budget caps (announced August 2026 as due "later this quarter") cover token spend; the aggregate gate covers business exposure.
- **Decoy and honeytoken family**
  - Handbook: Section 5, "Plan for shadow agents" (decoy credentials and decoy MCP tools reveal agents working outside the governed path); Section 6, "Scope of enforcement".
  - Deck: slide 16 notes; the "Continuous runtime defense" card on slide 13.
  - Needs the preprint's DOI.

## 5. Naming updates found while checking

- **Headless 360** has been folded into AIforce as its Headless Toolkit. Salesforce's Dreamforce IT post ([September 22, 2026](https://www.salesforce.com/blog/dreamforce-2026-top-it-announcements/)) describes AIforce as an interface layer powered by the Headless Toolkit, and Techzine reports the rename ([September 22, 2026](https://www.techzine.eu/blogs/analytics/144459/aiforce-brings-headless-capabilities-to-claude-slack-and-soon-teams/)). Confirm the exact wording with a Salesforce source, then update Section 3, "Start with capabilities, not channels" (the Headless 360 sentence), the Appendix A row and the slide 7 notes. AIforce also supports the "agent-mediated interfaces" uncertainty in Section 1 and on slide 4.
- **Flex Gateway is now Omni Gateway.** The handbook already uses Omni Gateway; use that name for Michael's policies.

## 6. Endnote and numbering impact

- Expect six to ten new sources. The shared list is numbered by first citation, so a new source first cited in Section 4 renumbers everything after it: handbook superscripts, Appendix B, the deck's endnote slides, slide source footers and bracketed numbers in speaker notes. Do one scripted renumbering pass at the end, then regenerate the deck's endnote slides from Appendix B.
- The ranges in the project instructions (1–43 main sections, 44–64 use cases) will change, and use case 3 adds a block at the end. John updates the project instructions; Claude updates the README.

## 7. Suggested order

1. Small fixes: restore the colon; the Headless 360 and AIforce naming; optionally, lead endnote 28 with EO 14412.
2. Oversight (item 2): Sections 4, 5, 6, 8, 9 and 10; slides 12, 13, 15, 19 and 20.
3. OT callout (item 3): Sections 5, 7 and 10; one new slide.
4. Michael's policies and decoys (item 4), after his walkthrough.
5. Use case 3, with his scenarios.
6. Renumber endnotes, rebuild the deck and update the README; John reviews and accepts.

As before, handbook edits go in as tracked changes with source comments, and deck changes go through the generator.

## 8. Open questions

**For Michael**
- The six predicates of Approval-to-Execution Binding, and how the separate attester works.
- Can both policies be named and cited in customer-facing material (a repository, a doc or a paper)? What does "P4A" stand for, and should it appear at all?
- The DOI for the decoy and honeytoken preprint.
- A public source for the refinery example.
- The scenario for use case 3, its systems of record, and the regulations that apply (for example NERC CIP, TSA pipeline security directives or ISA/IEC 62443).

**For John (answered September 29, 2026)**
- Use case 3 in this release or the next? This release, from public sources; Michael's scenarios later.
- Scorecard: add an "Oversight effectiveness" row, or replace the current one? Add the row.
- Comfortable citing academic papers and the EU AI Act for a CTO/CIO audience? Applied: Green, Sterz et al. and the EU AI Act are cited.
- Mention AIforce in the main text, or only update the Headless 360 naming? Applied: Headless 360 is described as the Headless Toolkit behind AIforce.

## Appendix: Michael's feedback, as received

> Hey John, read it end to end, this is really strong. Genuinely more rigorous than most "control plane" pieces out there: the architecture → orchestration → trust structure holds up, the sourcing is deep, and the "What to verify before you commit" section is the thing most of these skip — that's what makes it credible to a CTO instead of reading like a pitch. The runtime-enforcement framing ("enforced in the gateway path, not documented in a spreadsheet") and the "no consumer calls a model directly" design rule are exactly right, and you already nailed the coverage problem with the shadow-agent / bypass-route callouts. Nice work.
>
> Two things I'd add — both build on the LinkedIn post you saw, so they slot in naturally:
>
> 1. Human oversight = ability, not just assignment. Right now the scorecard counts oversight as "share of high-risk actions with approval or audit" — but that measures who's responsible, not whether they could actually intervene in time. That's the exact illusion the post was about (the refinery example — people were present, the conditions stopped them from acting). Worth a short bit distinguishing assigned oversight from demonstrated ability to intervene, plus what the safe default is when an approval expires or telemetry goes stale.
> 2. The physical/OT angle. The doc is all enterprise-IT today — for my energy/utility/O&G CTOs the gateway has to live inside a broader safety architecture with independent interlocks (the gateway isn't the last line of defense when an agent can command equipment). Natural fit for the use-case section you're building next, and I've got real scenarios there.
>
> Also — I've got two P4A gateway policies (Rust/WASM on Flex, CI-green, went through the same P4A review loop) that might be useful as concrete evidence for the reference-implementation and use-case sections:
>
> - Approval-to-Execution Binding — proves the executed MCP/A2A action is the one the approval actually approved, via six predicates including a freshness/expiry check (approval expired before execution, against the gateway's own clock) and a separate-attester requirement. It's basically the runtime for the oversight point in #1, and maps to EU AI Act Art. 14.
> - Cross-Session Aggregate-Risk Gate — reserve-then-authorize against a shared budget; refuses the individually-valid call that composes past an exposure limit no per-call gate ever sees (the "death by a thousand authorized cuts" case). Deepens your cost-control section. There's also a decoy/honeytoken family (published preprint + DOI) that backs the shadow-agent / bypass-route section.
>
> One nit, since you ran parts through AI: a couple of the sourced claims I couldn't find any public trace of and they have the hallmarks of AI-filled detail — I'd verify or strike before this goes anywhere customer-facing:
>
> - the Anthropic "Claude Mythos Preview" breaking AES / the HAWK PQC scheme "200–1,000× faster" (endnotes 31–32)
> - the June 22 2026 executive order "Securing the Nation Against Advanced Cryptographic Attacks" with the 2030/2031 deadlines (endnotes 27–30)
>
> Also double-check the Sept 2026 Dreamforce naming — "Trusted Enterprise AI Harness" / "AI Control Plane" and the Sept 11 date don't match what I can find (looks like the announcement was "AIforce" on Sept 15). The rest — Agent Fabric, Agent Broker GA June '26, MCP Bridge / LLM Governance GA, the NIST FIPS 203/204 dates, the Gartner 40% stat — all check out.
>
> Let me know if it'd help to walk you through the two policies for the reference-implementation and use-case sections — I can bring the energy/O&G scenarios too. Nice work again.
