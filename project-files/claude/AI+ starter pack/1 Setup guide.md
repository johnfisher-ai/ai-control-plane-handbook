# AI+ starter pack 1 of 4: setup guide

Prepared on October 15, 2026, in the AI Control Plane project, to set up the AI+ hub in its own GitHub repository and its own Claude project. Follow the steps in order; each says how long it takes and what you will see.

| File | What to do with it |
|---|---|
| 1 Setup guide (this file) | Follow it once. Upload it to the new project's knowledge too, for reference (Step 3) |
| 2 Project instructions | Paste into the new project's instructions (Step 3) |
| 3 Handoff | Upload to the new project's knowledge (Step 3); the first session reads it first |
| 4 Sites and repositories | Upload to the new project's knowledge (Step 3); fill in the gaps later through a session |

## Naming: recommendations

| What | Recommended name | Why |
|---|---|---|
| Site name | **AI+**, and **AI+ by John Fisher** wherever it stands alone (page titles, the LinkedIn newsletter, search results) | Decided in the plan (D1). "AI+" alone is already used by a research journal and a Substack, so your name makes it findable and clearly yours |
| Tagline | AI, plus the data science, math, statistics and Python behind it | Decided in the plan |
| GitHub repository | `johnfisher-ai.github.io`, exactly | Only this name serves the root address, https://johnfisher-ai.github.io/. Your handbook and your seven other sites keep their addresses beneath it |
| Repository description | AI+ by John Fisher: articles, handbooks, guides and labs on AI, data science, statistics and Python | Shown on GitHub and in search results |
| Repository topics | `ai`, `data-science`, `statistics`, `machine-learning`, `python`, `ai-governance` | The same words as the site's topic pages |
| Folder on your Mac | `~/Projects/johnfisher-ai.github.io` | Beside `~/Projects/ai-control-plane-handbook`. GitHub Desktop names the folder after the repository |
| Claude project | **JRF AI+ Hub** | Matches your "JRF The AI Control Plane White Paper" project. Project names are private, so the initials are fine here |
| Claude project description | AI+ hub site, articles, guides and labs, and the LinkedIn series | |
| Page titles | `<page title> · AI+ by John Fisher` | The same separator as the handbook's pages, so the two sites read as one family |
| Addresses | `/articles/<slug>/`, `/guides/<slug>/`, `/topics/<slug>/`, `/audience/<role>/`, `/handbooks/`, `/about/` | From the plan. Once published, an address never changes, because LinkedIn posts point at it for years |
| Topic slugs | `ai`, `ai-control-plane`, `data-science`, `statistics`, `machine-learning`, `python` | From the plan |
| Article slugs | The article's claim in 3 to 6 words, lowercase with hyphens, for example `/articles/adoption-is-outrunning-governance/` | Readable in a LinkedIn preview. No dates or numbers, so an update never moves an article |
| Future handbook repositories | `<subject>-handbook`, for example `data-science-handbook` and `statistics-handbook` | The same pattern as `ai-control-plane-handbook`: descriptive, no initials, no product names |
| Your existing repositories | Keep their current names | Renaming a repository changes its site address, and GitHub does not redirect the old one, so links already shared would break. Display names on the pages can change freely |
| LinkedIn newsletter (later) | AI+ by John Fisher | From the plan. Check that the name is free first |

## Before you start: three decisions (10 minutes)

You can make these now or let the first session walk you through them. Each has a recommendation.

1. **A custom domain, yes or no.**
   - Recommendation: decide before the first LinkedIn post. If yes, buy a domain with your name in it. The plan suggested `johnfisher.ai` or `johnfisherai.com`; neither has been checked.
   - A domain set on the hub also moves your project sites under it, the handbook included (for example `johnfisher.ai/ai-control-plane-handbook/`). GitHub redirects the old github.io addresses, and the handbook project then updates the addresses written into its pages.
   - If no, everything works at github.io, and you can add a domain later with the same redirects. Appendix A has the steps.
2. **How the site is built.**
   - Recommendation: Quarto, as the plan proposed. It gives the article card grid with filters, search, RSS feeds, and pages that run Python for the statistics, data science and Python articles.
   - Claude renders the site in its workspace and writes the finished pages into the `docs/` folder. You push them as usual, and GitHub Pages serves them as they are.
   - Why not GitHub Actions for now: Claude cannot see Actions logs or push fixes, so a failed build would sit with you. With finished pages, what you push is what goes live, already checked. Actions can come later if you want articles to publish themselves on a set date.
   - Fallback: plain HTML and Pagefind search, as on the handbook site. The first session checks that Quarto runs before you commit to it.
3. **License for articles and guides.**
   - Recommendation from the plan: CC BY 4.0 for articles and guide articles, as your Visual Handbook and Python, Visually already use, and MIT for code. The AI Control Plane handbook stays CC BY-NC-ND 4.0.
   - Alternative: CC BY-NC-ND 4.0 for everything, as you chose for the handbook. Consider it at least for the AI control plane articles, which are drawn from the handbook.

## Step 1. Create the repository on GitHub (5 minutes)

1. Sign in to github.com as `johnfisher-ai`.
2. Click **+** at the top right, then **New repository**.
3. Owner: `johnfisher-ai`. Repository name: `johnfisher-ai.github.io`, exactly; any other spelling makes an ordinary project site instead of the root site.
4. Description: the one in the naming table. Visibility: **Public**.
5. Tick **Add a README file**, so GitHub Desktop has something to clone; Claude replaces it later. Leave **.gitignore** and **license** set to None: the first session adds them.
6. Click **Create repository**.
7. On the repository page, click the gear beside **About**. Add the description, the website `https://johnfisher-ai.github.io/` and the topics from the naming table, then save.
8. **Settings → General → Features:** untick **Wiki** and **Projects**, as you did for the handbook.

Leave GitHub Pages off for now; Step 6 turns it on.

## Step 2. Clone it with GitHub Desktop (2 minutes)

1. In GitHub Desktop: **File → Clone Repository → GitHub.com**, then choose `johnfisher-ai/johnfisher-ai.github.io`.
2. Local path: `~/Projects/johnfisher-ai.github.io`. Click **Clone**.
3. Check that commits use your GitHub no-reply email (**GitHub Desktop → Settings → Git**), as for the handbook.

## Step 3. Create the Claude project (10 minutes)

**First, save the four files to your Mac.** In the chat where you received this pack, open each of the four file cards and download it. They land in your Downloads folder.

**Then create the project on claude.ai** (in a browser, or the Chat side of the desktop app):

1. Go to claude.ai/projects, or click **Projects** in the left sidebar.
2. Click **+ New Project** at the top right.
3. Name: **JRF AI+ Hub**. Description: the one in the naming table. Create the project.
4. **Instructions:**
   - On the project's page, click **Set project instructions**.
   - Open `2 Project instructions.md` from Downloads in TextEdit, copy the text between the two `---` lines, and paste it into the box.
5. **The naming rule:**
   - In another tab, open the **JRF The AI Control Plane White Paper** project and its instructions, and copy the paragraph that begins "Naming rule:".
   - Back in the new project, select `[Paste the naming rule here]` and paste over it. Click **Save instructions**.
   - The pack leaves the banned word out on purpose, because the rule bans it from every document, this one included.
6. **Files:**
   - On the right side of the project's page is the project knowledge panel. Click its **+** button and upload, from Downloads, `1 Setup guide.md`, `3 Handoff.md` and `4 Sites and repositories.md`.
   - Leave out file 2: its text is already in the instructions.
   - Check that the three files are listed in the panel.
7. **Later changes to file 4:** don't upload it again. Ask a session in the project to update it ("Update the Sites and repositories file: Aethos is at …"); sessions in a project can rewrite its files.

## Step 4. Start the first session in Cowork (5 minutes)

1. In the Claude desktop app, start a new Cowork task the way you start tasks in the AI Control Plane project, and pick **JRF AI+ Hub** as its project, with your computer selected.
2. Connect the folder `~/Projects/johnfisher-ai.github.io`.
   - Don't connect the handbook folder. Handbook changes happen in the AI Control Plane project; the hub reads the handbook from its public site.
   - To work on one of your other sites later, connect that site's folder for that session only.
3. Paste this as the first message:

> Read the project files, starting with the handoff. Then: (1) go through the three setup decisions with me (domain, how the site is built, article license); (2) check that Quarto runs in your workspace; (3) propose the site skeleton (home, Articles, Handbooks shelf, Guides & Labs, About, search and RSS) and a punch list for the first milestone. Don't write files until I agree.

## Step 5. Review, commit and push (each round)

Claude writes files into your folder and tells you what changed. In GitHub Desktop, review the changed files, write the summary Claude suggests, then **Commit to main** and **Push origin**, as with the handbook.

## Step 6. Turn on GitHub Pages (after the first push, 5 minutes)

1. In the repository: **Settings → Pages**.
2. Under **Build and deployment**, set Source to **Deploy from a branch**. Set Branch to **main** and the folder the session names: **/docs** for Quarto, or **/ (root)** for plain HTML. Click **Save**.
3. After a minute or two the site is live at https://johnfisher-ai.github.io/. Check that **Enforce HTTPS** is ticked.
4. Open one of your other sites, for example https://johnfisher-ai.github.io/Python-Visual-Guides/, to confirm it still loads. It should: project sites keep their addresses under the user site.
5. Tell the session it is live. It tests the live site in the desktop app's browser.

## Step 7. Link the family together (later)

- **The handbook:** once the hub is live, ask the AI Control Plane project to add a link to AI+ on the handbook's pages. If you add a domain, it also updates the addresses written into the handbook's pages, its sitemap and its README.
- **The Handbooks shelf:** the hub links to each handbook's own site and never copies its pages.
- **Your other sites:** the plan's shared top bar (D12) goes into each site's own repository, one site at a time, from the new project with that site's folder connected.

## Step 8. LinkedIn (when the first articles are ready)

- Add the hub to your profile's **Featured** section, and make **Follow** your profile's main button, as the plan suggests.
- Before posting an article link, check its preview in LinkedIn's Post Inspector, as you did for the handbook.

## Appendix A. Custom domain (only if you decide yes)

1. Buy the domain from a registrar.
2. **Verify it with GitHub first**, which protects it from takeover: your GitHub account's **Settings → Pages → Add a domain**, then add the TXT record GitHub shows at your registrar.
3. **At your registrar's DNS:**
   - For the bare domain, add A records for 185.199.108.153, 185.199.109.153, 185.199.110.153 and 185.199.111.153, and AAAA records for 2606:50c0:8000::153, 2606:50c0:8001::153, 2606:50c0:8002::153 and 2606:50c0:8003::153.
   - Add a CNAME record for `www` pointing to `johnfisher-ai.github.io`.
   - Check these values against GitHub's "Managing a custom domain for your GitHub Pages site" page before you enter them.
4. **In the hub repository:** **Settings → Pages → Custom domain**, enter the domain and save. When the DNS check passes, tick **Enforce HTTPS**. The session adds the matching `CNAME` file to the site.
5. **Test the redirects:** https://johnfisher-ai.github.io/ai-control-plane-handbook/ should now redirect to the handbook under your domain.
6. **In the AI Control Plane project:** ask for the handbook's addresses to be updated (page canonicals, social-card addresses, sitemap and README).
