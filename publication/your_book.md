\# DoughForge: The Reproducible Self-Publishing Desktop Kit



\*\*By Roger G. Lewis\*\*



\*"No passion in the world is equal to the passion to alter someone else's draft."\*  

— H. G. Wells



---



\## Frontmatter / YAML Metadata Block



\*(For Reedsy/Pandoc — paste at top of your .md file before converting)\*



```yaml

---

title: "DoughForge"

subtitle: "The Reproducible Self-Publishing Desktop Kit"

author: "Roger G. Lewis"

series: "DoughForge Guides"

series\_number: 1

date: "2026"

language: en-GB

rights: "© 2026 Roger G. Lewis"

description: "A practical, cheerful guide to building a repeatable self-publishing workflow using Markdown, Pandoc, and Git — so you stop losing days to drift and start shipping books."

---

```



---



\## Foreword: From a Cheerful Realist



I've published eleven books through Draft2Digital since 2018. Two more are in the pipeline. That means I've had enough \*oh no\* moments to qualify as a minor weather system.



The recurring theme was never incompetence. It was \*\*drift\*\*.



Titles drift. Covers drift. Internal title pages drift. Versions drift. And suddenly your "final" file has cousins — loud, contradictory cousins who all claim to be the real one.



This kit is how you stop drift from running your publishing schedule. It won't make you a developer. It won't demand you love tooling. It just asks that you stop fearing it — and that you give your future self a fighting chance.



---



\## Chapter 1: The Reproducible Self-Publishing Desktop Kit



\### Introduction: Release Notes for Writers Who've Been Burned



There's a line buried in early UNIX source code that reads:



> \*"You are not expected to understand this."\*



It wasn't a challenge. It meant: \*this won't be on the exam.\*



So naturally, it's on the exam.



Not because you need to become a compiler archaeologist, but because modern publishing tools have the same bad habit as old systems code — they quietly accumulate quirks, and then you lose an afternoon (or a launch date) to something you were never warned about.



This pamphlet is a small act of civil engineering:



\- \*\*One canonical manuscript\*\* — the single source of truth for your book

\- \*\*A repeatable build\*\* — producing PDF, EPUB, and DOCX from that one source

\- \*\*A boring paper trail\*\* — so nothing drifts without you noticing



You already know how to write. The frustrating part is everything \*around\* the writing: the title that doesn't match, the cover that shifted, the EPUB that behaves perfectly until a platform preview invents new physics, and the eternal haunting question:



\*Which file is the real one?\*



This pamphlet is a small answer to that question. Not glamorous. Just reliably boring — and boring, in publishing, is a superpower.



---



\## Chapter 2: Origin Story — The Quirks That Ate Publication Day



Every self-publisher has a story. Mine involves a cover that said one subtitle, an internal title page that said another, and a store listing that had apparently been updated by a ghost.



The common culprits are always the same:



\- \*\*Cover title/subtitle doesn't match the internal title page.\*\* Looks fine in your head; looks wrong to every reader.

\- \*\*EPUB respects headings; DOCX decides to improvise.\*\* Pandoc is good. Platform converters are adventurous.

\- \*\*Scene breaks turn into mystery blank space\*\* — or, worse, mystery \*no\* space.

\- \*\*Previews look fine until the store conversion does its own thing.\*\* You checked it. You \*definitely\* checked it.

\- \*\*You fix one thing and accidentally upload a different file than the one you just fixed.\*\* This one is the most demoralising.



The fix isn't heroic. It's practical: \*\*write down reality, then make the tools obey it.\*\*



That's what an Anchor file is for — a plain, boring contract that says: \*these paths are real, these commands work on this machine, this is the source, and these are the outputs.\*



---



\### Prompt Box: Check What's Real Before You Fix What Isn't



> \*\*Pitfall: Notepad + OneDrive + Markdown fences\*\*

>

> If Notepad offers to "clear all and save new" or says it can't find the file — \*\*stop\*\*. Verify you're editing the file you think you are. In synced folders like OneDrive, the file can change while Notepad has it open.

>

> Also: Markdown code fences are literal. If you open a fenced block with ` ``` ` and forget the closing, the rest of your document becomes code. Your PDF will look extraordinary. Not in a good way.

>

> \*\*Two quick checks:\*\*

> 1. Confirm the manuscript file is real and non-empty before building.

> 2. Count your code fences — they should come in pairs.



---



\## Chapter 3: Inside the Publishing Pain Locker



Publishing pain usually comes from one root cause: \*\*you stop knowing which file is the truth.\*\*



So we pick a truth. And we make everything else a rebuildable product of that truth.



\### The Ground Truth Rule



One canonical manuscript. Everything else is generated.



If an output looks wrong, you do not fix the output. You fix the manuscript — or the build rules — and you rebuild. This isn't ideology. It's how you keep launch day boring.



\### What Counts as Canonical (and What Doesn't)



\*\*Edit these:\*\*

\- `publication/your\_book.md` — the manuscript

\- Images referenced by the manuscript (covers, diagrams)

\- Build scripts and templates you actually control



\*\*Rebuild these — never edit directly:\*\*

\- `outputs/\*.pdf`

\- `outputs/\*.epub`

\- `outputs/\*.docx`



If you can regenerate it, don't treat it like source. The moment you start "just quickly fixing" a PDF directly, you've created a cousin. The cousins will multiply.



\### The Anchor Connection — No Mysticism, Just Receipts



Your `ANCHOR.md` file is the contract that keeps you honest:



\- The repo layout you expect

\- The commands that should work

\- The checks you run when reality starts drifting



When you're tired, \*obvious\* becomes expensive. Anchor files are cheap insurance.



---



\## Chapter 4: Git and the Kit — Version Control Without the Drama



Git is not here to turn you into a developer. It's here to prevent these specific disasters:



\- \*"I fixed it yesterday. Where did it go?"\*

\- \*"Which draft did I upload?"\*

\- \*"I changed one tiny thing and now everything is different."\*

\- \*"I need the previous subtitle back. The good one."\*



\### The Writer-Friendly Git Minimum



You can get 90% of the value with three commands:



```bash

git add .

git commit -m "describe what you just did"

git log --oneline

```



That's it. No branching epic required. No pull requests. No rebasing. Just a trail of breadcrumbs that leads you back to the version that worked.



\### What to Commit



\*\*Commit these:\*\*

\- Manuscripts (`publication/\*.md`)

\- Anchor and logs (`ANCHOR.md`, `INTERIM\_PROGRESS\_LOG.md`)

\- Build scripts (`tools/`)

\- Templates and styles you own

\- Referenced images



\*\*Avoid committing:\*\*

\- Generated outputs (`outputs/\*`) — unless you deliberately want release artefacts in the repo, in which case do it in a separate, clearly labelled commit



\### A Good Commit Message Formula



Use: \*\*verb + object + reason\*\*



Examples:

\- `Add epigraph and replace HTML breaks with scene markers`

\- `Clarify Anchor contract and add build checks`

\- `Fix heading levels to improve EPUB navigation`



Your future self doesn't need poetry. They need context. Give them context.



---



\## Chapter 5: Covers, Titles, Headings, and Metadata



Metadata is the most boring part of publishing — until it costs you three hours on a Friday afternoon.



\### Where Drift Happens



Drift occurs when these four things don't match each other:



1\. \*\*Cover text\*\* — what the reader sees on the front

2\. \*\*Internal title page\*\* — what's inside the book

3\. \*\*Platform metadata fields\*\* — what Draft2Digital, Reedsy, or your distributor shows

4\. \*\*Your YAML\*\* — what you told Pandoc the book is called



\### The One Sheet of Reality Trick



Maintain one place where the current truth lives. YAML at the top of your manuscript is ideal, because it travels with the file. Your YAML block should contain:



```yaml

title: "Your Actual Title"

subtitle: "Your Actual Subtitle"

author: "Your Name, Spelled Correctly"

series: "Series Name If Applicable"

```



\*\*Practical rules that prevent drift:\*\*



\- Change metadata in the YAML \*first\*, then update the cover and title page

\- Treat store dashboards as outputs, not sources of truth — the dashboard reflects what you uploaded, not what's correct

\- Decide your public title policy and stick to it: subtitle everywhere, or cover-only? Document the decision



\### EPUB Note — Quiet but Important



EPUB readers and library apps surface metadata aggressively. If your book looks wrong in a device library, it's usually metadata — not layout. Check the YAML before you rebuild the cover.



---



\## Chapter 6: Covers and Artwork — We've Got You Covered



Covers are where drift becomes visible. And embarrassing.



The classic mismatch: the cover says \*Title: The Brilliant Subtitle\*. The title page inside says \*Title\*. The store listing says something from six months ago that you thought you'd updated.



\### Minimum Cover Alignment Checklist



Before you upload anything, verify:



\- \[ ] Cover text matches YAML (title, subtitle, author — all of it)

\- \[ ] Internal title page matches YAML (or you've intentionally omitted the subtitle and documented that choice)

\- \[ ] EPUB metadata matches YAML

\- \[ ] Filenames are boring and consistent — no `final\_REAL\_v3\_THISONE.pdf`



\### Where People Lose Time



\- Exporting multiple cover sizes and forgetting which one is live

\- Tweaking cover text after upload but not updating the manuscript

\- A tiny subtitle change cascading into four separate edits across three different tools



\*\*The time-saving principle:\*\* Make metadata edits once, in the YAML. Then rebuild and re-export everything. One edit, one rebuild, one upload.



---



\## Chapter 7: Going With Your Flow



Different writers have different habits. Good. The workflow should adapt without breaking.



This kit is deliberately permissive. Write in Markdown from an LLM, a text editor, Obsidian, VS Code, Notepad — whatever suits you. The structure is what matters, not the tool you used to create it.



\### A Safe Subset of Markdown for Predictable Builds



\*\*Use freely:\*\*

\- `#` / `##` / `###` headings

\- Bullet and numbered lists

\- Blockquotes (`>`)

\- Code fences (triple backticks — always close them)

\- Emphasis (\*italic\*, \*\*bold\*\*)

\- Links



\*\*Be cautious with:\*\*

\- Raw HTML for layout — it varies by output format

\- Manual spacing tricks (multiple blank lines render differently in different converters)

\- Forcing pagination for EPUB or DOCX — they don't have pages in the same way a PDF does



\### Formatting Philosophy for Tired Humans



If you can't explain why a formatting trick exists in one sentence, it doesn't belong in the canonical manuscript. If it's there to make one output look slightly nicer and it breaks two others, it's not a trick — it's a trap.



---



\## Chapter 8: Preparing to Ship — Print All



Getting to \*shipped\* is mostly about reducing avoidable surprises. The goal is a launch day so boring it barely registers.



\### A Sane Timeline (Pamphlet Edition)



1\. Write in the canonical Markdown

2\. Build PDF, EPUB, and DOCX locally

3\. Spot-check the usual failure points (see checklist below)

4\. Commit the changes that produced the shippable build

5\. Upload and distribute

6\. Tag the release (optional, but your future self will thank you)



\### The Firstship Checklist — Fast, Not Fancy



\*\*Content sanity:\*\*

\- \[ ] Title, subtitle, and author match YAML and cover

\- \[ ] Contents list matches headings (or is clearly manual and you've documented that)

\- \[ ] No accidental \*everything is code\* sections from unclosed fences



\*\*Build sanity:\*\*

\- \[ ] PDF opens, fonts look normal, headings look right

\- \[ ] EPUB opens in at least one reader (Calibre is fine)

\- \[ ] DOCX opens and headings are \*real headings\*, not bold paragraphs



\*\*Common output gotchas:\*\*

\- \[ ] Scene breaks are consistent — pick one style and stick to it

\- \[ ] Images render and are correctly sized

\- \[ ] Smart punctuation renders cleanly (XeLaTeX usually behaves; DOCX sometimes doesn't)



\### The Two-Minute Preview Rule



If you only have two minutes, check:



1\. The title and first page

2\. The contents or navigation

3\. One code block

4\. One major section break



Most disasters show up right there. If those four things look right, you're probably fine.



---



\## Chapter 9: The W-ANCHOR Protocol — This Is the Panicking Section



Here's where we talk about what to do when things go wrong. Because they will go wrong. Not catastrophically — just in that low-grade, where-did-my-afternoon-go way that self-publishing specialises in.



\### The Origin of the Anchor



Debugging digital tooling is painstaking work. Getting LLMs to do the heavy lifting is a process of breaking things, fixing them, then breaking them again — hopefully arriving somewhere useful before the whole thing falls over in production.



It was AI drift and AI hallucinations that inspired me to write this booklet, as a side project to the Home@ix FAIR-index project. In other projects I've developed tricks for screening LLM biases (the AQAL source-of-truth file), for escaping the Google Bubble, and for navigating the media Overton Window. All of those habits fed into this workflow — which is my own workflow, ported into a tool that's still adaptable for your style.



\### The W-ANCHOR Glossary — For When You've Forgotten What Everything Means



| Term | What It Actually Means |

|---|---|

| \*\*Anchor file\*\* | The contract for what's real: paths, tools, commands, outputs |

| \*\*Canonical manuscript\*\* | The one source you edit; everything else is generated from it |

| \*\*Drift\*\* | Mismatches across cover, title page, stores, files, versions |

| \*\*Outputs\*\* | PDF/EPUB/DOCX artefacts built from the canonical manuscript |

| \*\*Pandoc\*\* | The converter that turns Markdown into the three formats |

| \*\*XeLaTeX\*\* | The PDF engine — good with fonts and smart punctuation |

| \*\*Code fence\*\* | Triple backticks that must always be closed |

| \*\*Which file is real?\*\* | The canonical manuscript + the commit history |



\### The Protocol in Plain English



When something looks wrong:



1\. \*\*Don't fix the output.\*\* Fix the source.

2\. \*\*Check the YAML first.\*\* Most drift starts there.

3\. \*\*Rebuild from the canonical manuscript.\*\* Don't patch the PDF.

4\. \*\*Commit before you upload.\*\* Always.

5\. \*\*If you're not sure which file is real, check Git.\*\* That's what it's for.



---



\## Closing Note: Cheerful and Realistic



You're not trying to become a tool expert. You're trying to ship writing without losing days to nonsense.



This kit doesn't remove quirks from the world. It makes them \*\*repeatable, diagnosable, and eventually boring.\*\*



The W-ANCHOR Protocol is an anchor, not a cage. It holds you in place just enough that the tide doesn't carry your subtitle away.



If you want to stop W-ANCHORing, lose your cherry by forking this! \[cherry]\[rocket]



---



> \*Note: This Reproducible Self-Pub Kit is based on the architecture and patterns from the Home@ix FAIR project (see \[https://github.com/tonefreqhz/hom-ixFAIRindex](https://github.com/tonefreqhz/hom-ixFAIRindex)), which established the foundational workflow for reproducible builds, PROJECT\_ROOT anchoring, build invariants, and the Build Notes Anchor to prevent AI/human drift in long-running development.\*



---



\*\*Happy publishing. I hope this helps.\*\*



\*Best,\*  

\*Rog\*



---



\## Appendix: Quick Build Commands



```bash

\# Build PDF

pandoc publication/your\_book.md \\

&nbsp; --pdf-engine=xelatex \\

&nbsp; -o outputs/your\_book.pdf



\# Build EPUB

pandoc publication/your\_book.md \\

&nbsp; --epub-cover-image=covers/cover.jpg \\

&nbsp; -o outputs/your\_book.epub



\# Build DOCX

pandoc publication/your\_book.md \\

&nbsp; -o outputs/your\_book.docx



\# Commit a clean build

git add .

git commit -m "Build: shippable version with corrected subtitle"

```



---



\*DoughForge: The Reproducible Self-Publishing Desktop Kit\*  

\*First Edition — 2026\*  

\*Roger G. Lewis\*  

\*\[https://github.com/tonefreqhz/hom-ixFAIRindex](https://github.com/tonefreqhz/hom-ixFAIRindex)\*

