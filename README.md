# The AI Control Plane Handbook

*Architecture, orchestration, and zero-trust security for the agentic enterprise.* Executive Edition 2026.1 (October 2026), by John Fisher. See [what's new in this edition](https://johnfisher-ai.github.io/ai-control-plane-handbook/whats-new.html).

**Read it at https://johnfisher-ai.github.io/ai-control-plane-handbook/**

The handbook sets out what an enterprise AI control plane is, why it has become the next infrastructure advantage, how to architect one, a vendor-neutral target reference architecture to steer by, one way to realize it with MuleSoft Agent Fabric and Informatica, and how to sequence the work over the next 12 to 24 months with value at every phase. Three reference use cases (professional services, capital markets and a natural gas pipeline operator) apply the architecture end to end. It is written for CTOs, CIOs and the architects who work with them.

## Status

| Part | Status |
|---|---|
| Landing page | Published |
| Handbook chapters (Sections 1–13, Appendices A–E) | Published, one page per section and appendix |
| Executive deck | Published, slide images with the slide text and speaker notes, and each slide as a one-slide PowerPoint download |
| Assessment toolkit (guide, client report template, client deck) | Published, one page per section and appendix, and the thirteen templates as a Word download |
| Quantum briefing | Published, one page |
| Site search | Published: one search page across the handbook and its companions |
| What's new | Published: edition 2026.1 and every change since, with dates |

## What's in this repository

| Path | What it is |
|---|---|
| `index.html` | Landing page |
| `404.html` | Page shown for a missing address |
| `search.html` | Search page (Pagefind's search interface) |
| `whats-new.html` | What's new in this edition |
| `pagefind/` | The search index and interface, generated from the pages by Pagefind (do not edit by hand) |
| `assets/css/site.css` | Site styles (the design system of the companion deck) |
| `assets/fonts/` | Plus Jakarta Sans, self-hosted, with its license (`OFL.txt`) |
| `assets/img/` | Icons and the social-sharing image |
| `assets/licenses/` | Pagefind's license |
| `handbook/` | The handbook: an introduction, the executive summary, Sections 1–13 and Appendices A–E, one page each, with the figures in `handbook/img/` |
| `deck/` | The executive deck: the slides in seven pages, each slide with its text and speaker notes, then the notices; slide images in `deck/img/`, and slides 1–58 as one-slide PowerPoint files in `deck/slides/` |
| `toolkit/` | The assessment toolkit: the guide (Parts 1–4, Sections 1–10, Appendices A–G), the client report template and the client deck; figures and slide images in `toolkit/img/`, and the templates T1 to T13 as one Word document in `toolkit/downloads/` (Appendix G) |
| `quantum/` | The quantum briefing, with its own endnotes |
| `sitemap.xml` | Site map for search engines |
| `.nojekyll` | Tells GitHub Pages to publish the files as they are |

The site is plain HTML and CSS with no build step. GitHub Pages publishes it from the `main` branch, root folder. The one generated part is the search index in `pagefind/`, built from the pages with Pagefind 1.4.0 (`npx pagefind@1.4.0 --site .`). Rebuild it whenever a page changes, and replace the whole folder, because its file names change with the content. Only the `<main>` content of each page is indexed.

The pages in this repository are the master copy of the handbook and its companions. Edit them directly. The Word and PowerPoint editions the site was first converted from are no longer maintained, and no PDF files are kept here. There are two kinds of download. The executive deck's one-slide PowerPoint files in `deck/slides/`, one per slide, each carry the slide's speaker notes and a credit and license note; the slide images are renders of those slides, so a change to what a slide shows needs a new image and a new download as well as a change to its slide text. The toolkit's templates are in one Word document, `toolkit/downloads/ai-control-plane-assessment-templates.docx`: Part 1 is the blank templates of Section 7 and Part 2 the filled-in templates of Section 8. It is the only Word file in the repository, and it is generated from those pages, so a change to a template on the site needs a new download too.

## Editions

Each edition is a Git tag. Edition 2026.1 (`v2026.1`, October 2026) is the first public edition. Between editions, corrections and additions are made on the pages and listed with their dates on [`whats-new.html`](whats-new.html).

## License

© 2026 John Fisher. Everything in this repository apart from the typeface and the search software (see below), including the handbook, its companions, the downloads and the site's own HTML and CSS, is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/); the full text is in [`LICENSE`](LICENSE). You may copy and share the handbook, in whole or in part, without changes and for non-commercial purposes, if you credit John Fisher and link to the license.

Additional permissions, which add to the license without changing it:

- **Slide downloads.** The executive deck's one-slide PowerPoint files may be adapted and the adapted slides presented and shared inside an organization or with clients, including in paid work, with the credit given in the deck's notices ([`deck/notices.html`](deck/notices.html)).
- **Assessment toolkit.** The toolkit may be used to run AI control plane assessments, and its Word templates may be adapted for other work, inside an organization or with clients, including in paid work, with the credits given in the toolkit's notices ([`toolkit/appendix-e.html`](toolkit/appendix-e.html)).

None of them covers selling the material or publishing changed versions of it.

Suggested credit: John Fisher, The AI Control Plane Handbook, Executive Edition 2026.1 (2026), CC BY-NC-ND 4.0.

The license covers John Fisher's own text and figures. It does not cover trademarks, or the quotations, data and other material of the sources cited, which belong to their owners. The Plus Jakarta Sans typeface is licensed separately under the SIL Open Font License 1.1 ([`assets/fonts/OFL.txt`](assets/fonts/OFL.txt)). The search interface and index files in `pagefind/` are generated by Pagefind, which is licensed under the MIT License ([`assets/licenses/pagefind-LICENSE.txt`](assets/licenses/pagefind-LICENSE.txt)); the text they index is the handbook's and stays under its license.

## Disclosure

John Fisher works for Salesforce. He wrote this handbook independently, on his own time and not as part of his work at Salesforce, using only public information. The views in it are his own, not those of Salesforce or any other company named, and it is not sponsored or endorsed by Salesforce or any of them.

Salesforce, MuleSoft, MuleSoft Agent Fabric and Informatica are trademarks of Salesforce, Inc. or its affiliates. Other product, company and organization names may be trademarks of their respective owners; names are used only to identify the products discussed and imply no endorsement.

## Contact

Comments and corrections are welcome on [LinkedIn](https://www.linkedin.com/in/johnrfisher).
