---
title: "DoughForge"
subtitle: "The Reproducible Self-Publishing Desktop Kit"
author: "Roger G. Lewis"
series: "DoughForge Guides"
series_number: 1
date: "2026"
language: en-GB
rights: "© 2026 Roger G. Lewis"
description: "A practical, cheerful guide to building a repeatable self-publishing workflow using Markdown, Pandoc, and Git — so you stop losing days to drift and start shipping books."
---

# DoughForge: The Reproducible Self-Publishing Desktop Kit

### *A Cheerful Manual for Writers Who Have Lost an Afternoon to a Subtitle*

**By Roger G. Lewis**
*Author of The Conquest of Dough, The Strawberry Manifesto, and other works that exist in more versions than strictly necessary*

> *"No passion in the world is equal to the passion to alter someone else's draft."*
> — H. G. Wells[^1]

[^1]: Wells said this about other people's drafts. He did not anticipate the self-publishing era, in which the writer, the editor, the typesetter, and the person who accidentally uploaded the wrong PDF are all the same person.

---

## Foreword: From a Cheerful Realist

I have published eleven books through Draft2Digital since 2018. Two more are in the pipeline. That means I have had enough *oh no* moments to qualify as a minor weather system.[^2]

The recurring theme was never incompetence. It was **drift**.

Titles drift. Covers drift. Internal title pages drift. Versions drift. And suddenly your "final" file has cousins — loud, contradictory cousins who all claim to be the real one and have opinions about the subtitle.

This kit is how you stop drift from running your publishing schedule. It will not make you a developer. It will not demand you love tooling. It just asks that you stop fearing it — and that you give your future self a fighting chance.

The pamphlet you are holding is a small answer to one question: *which file is the real one?*

Not glamorous. Just reliably boring — and boring, in publishing, is a superpower.[^3]

[^2]: A minor weather system characterised by sudden drops in confidence, localised confusion about filenames, and the occasional catastrophic front where the cover says one thing and the title page says another.

[^3]: Glamour is for book launches. Boring is for the six months before the book launch when you are trying to remember which version of Chapter 4 you actually sent to the formatter.

---

# Part One: The Kit

---

## Chapter 1: The Reproducible Self-Publishing Desktop Kit

### *Release Notes for Writers Who Have Been Burned*

There is a line buried in early UNIX source code that reads:

> *"You are not expected to understand this."*

It was not a challenge. It meant: *this will not be on the exam.*

So naturally, it is on the exam.[^4]

Not because you need to become a compiler archaeologist, but because modern publishing tools have the same bad habit as old systems code — they quietly accumulate quirks, and then you lose an afternoon (or a launch date) to something you were never warned about. The quirks do not announce themselves. They wait. They are patient in the way that only inanimate software can be patient, which is to say: completely, and without mercy.

This pamphlet is a small act of civil engineering:

- **One canonical manuscript** — the single source of truth for your book
- **A repeatable build** — producing PDF, EPUB, and DOCX from that one source
- **A boring paper trail** — so nothing drifts without you noticing

You already know how to write. The frustrating part is everything *around* the writing: the title that does not match, the cover that shifted between Tuesday and Thursday, the EPUB that behaves perfectly until a platform preview invents new physics, and the eternal haunting question that follows you to bed:

*Which file is the real one?*

This pamphlet is a small answer. One canonical manuscript. One repeatable build. Version history you can trust. Not glamorous. Just reliably boring.

You do not have to love tooling. You just should not have to fear it.[^5]

[^4]: The exam consists of one question: "Why does the store listing say the subtitle is 'A Novel' when you changed it to 'A Memoir' in March?" Full marks are awarded for correctly identifying which of your seventeen saved versions is canonical. Partial credit is available for crying.

[^5]: Fear of tooling is rational. The tools have earned it. This kit is an attempt to make the tools slightly less terrifying by making their behaviour slightly more predictable. It is the publishing equivalent of a leash.

---

## Chapter 2: Origin Story

### *The Quirks That Ate Publication Day*

Every self-publisher has a story.

Mine involves a cover that said one subtitle, an internal title page that said another, and a store listing that had apparently been updated by a ghost with strong opinions about punctuation.[^6]

I have published eleven books. I have had this experience — in various configurations — approximately eleven times. The details change. The structure does not. It always begins with confidence (*I checked everything*), proceeds through confusion (*but I definitely checked it*), and arrives at the same destination: a file called `final_REAL_v3_THISONE.pdf` that is not, in any meaningful sense, final, real, or the one.

The common culprits are always the same:

**Cover title/subtitle does not match the internal title page.**
Looks fine in your head. Looks wrong to every reader. The cover says *The Conquest of Dough: A History of Bread and Power*. The title page says *The Conquest of Dough*. The store listing says *The Conquest of Dought* because autocorrect had opinions.

**EPUB respects headings; DOCX decides to improvise.**
Pandoc is good. Platform converters are adventurous. Your carefully structured heading hierarchy arrives at the other end looking like it was formatted by someone who had heard of headings but never personally encountered one.

**Scene breaks turn into mystery blank space — or, worse, mystery no space.**
You put three asterisks. The converter put nothing. Or a line. Or a small existential crisis rendered in whitespace.

**Previews look fine until the store conversion does its own thing.**
You checked it. You *definitely* checked it. The preview was perfect. The live version has decided that your chapter titles should be in a font that does not exist on any device manufactured after 2009.

**You fix one thing and accidentally upload a different file than the one you just fixed.**
This one is the most demoralising. It is also the most preventable. It is what this entire book is about.[^7]

The fix is not heroic. It is practical.

**Write down reality. Then make the tools obey it.**

That is what an Anchor file is for — a plain, boring contract that says: *these paths are real, these commands work on this machine, this is the source, and these are the outputs.* It does not prevent quirks. It makes them findable. And findable is most of the battle.

[^6]: The ghost's preferred subtitle was "Revised Edition," which was not accurate, not requested, and not removable without contacting support. The ghost has since moved on to haunt other people's metadata.

[^7]: The entire book is about this one problem. The problem has many faces. The solution has one face. It is a boring face. We are going to look at it for several chapters.

---

> **Prompt Box: Check What's Real Before You Fix What Isn't**
>
> **Pitfall: Notepad + OneDrive + Markdown fences**
>
> If Notepad offers to "clear all and save new" or says it cannot find the file — **stop**. Verify you are editing the file you think you are. In synced folders like OneDrive, the file can change while Notepad has it open. This is not a bug. It is a feature designed specifically to ruin your afternoon.[^8]
>
> Also: Markdown code fences are literal. If you open a fenced block and forget the closing, the rest of your document becomes code. Your PDF will look extraordinary. Not in a good way.
>
> **Two quick checks before every build:**
>
> 1. Confirm the manuscript file is real and non-empty.
> 2. Count your code fences — they come in pairs, like socks, and a missing one causes similar levels of frustration.

[^8]: OneDrive is brilliant at many things. Knowing when you want it to sync and when you want it to leave your file alone is not among them. This is not a criticism. It is a weather report.

---

## Chapter 3: Inside the Publishing Pain Locker

### *Or: Why You Keep Losing Afternoons to Things That Should Take Five Minutes*

Publishing pain usually comes from one root cause.

**You stop knowing which file is the truth.**

This sounds simple. It is not simple. It is the kind of problem that starts as a minor inconvenience on a Tuesday and becomes a full structural crisis by Thursday, when you realise that the file you uploaded to the store, the file on your desktop, and the file in your email to the formatter are three different documents that have been diverging quietly since March.[^9]

So we pick a truth. And we make everything else a rebuildable product of that truth.

### The Ground Truth Rule

**One canonical manuscript. Everything else is generated.**

If an output looks wrong, you do not fix the output. You fix the manuscript — or the build rules — and you rebuild. This is not ideology. It is how you keep launch day boring. Boring launch days are good launch days. Exciting launch days are the ones where you discover the wrong file at 11pm.

**Edit these:**

- `publication/your_book.md` — the manuscript. The truth. The one.
- Images referenced by the manuscript
- Build scripts and templates you actually control

**Rebuild these — never edit directly:**

- `outputs/*.pdf`
- `outputs/*.epub`
- `outputs/*.docx`

If you can regenerate it, do not treat it like source. The moment you start "just quickly fixing" a PDF directly, you have created a cousin. The cousins will multiply. They will have children. The children will have opinions about the subtitle.[^10]

### The Anchor Connection — No Mysticism, Just Receipts

Your `ANCHOR.md` file is the contract that keeps you honest. It contains:

- The repo layout you expect
- The commands that should work
- The checks you run when reality starts drifting

It is not magic. It is a receipt. When you are tired and confused and staring at four files with similar names, the Anchor file is the thing you open to remember what is real.

When you are tired, *obvious* becomes expensive. Anchor files are cheap insurance.[^11]

[^9]: March is when most publishing drift begins. This is not scientifically established. It is experiential.

[^10]: The cousins are not malicious. They are just the natural result of editing outputs instead of sources. They multiply because every time you fix one, you create another. This is the publishing equivalent of the Hydra, except the heads are all slightly different versions of Chapter 4.

[^11]: The cheapest insurance is a text file. The most expensive insurance is discovering, at upload time, that you have been editing the wrong file for three weeks.

---

## Chapter 4: Git and the Kit

### *Version Control Without the Drama, or: Stop Selling Yourself Work You Already Did*

Git is not here to turn you into a developer.

Git is here to prevent these specific disasters:

- *"I fixed it yesterday. Where did it go?"*
- *"Which draft did I upload?"*
- *"I changed one tiny thing and now everything is different."*
- *"I need the previous subtitle back. The good one. The one from before."*[^12]

### The Writer-Friendly Git Minimum

You can get 90% of the value with three commands:

    git add .
    git commit -m "describe what you just did"
    git log --oneline

That is it. No branching epic required. No pull requests. No rebasing. No learning what rebasing means. Just a trail of breadcrumbs that leads you back to the version that worked, written in plain English by your past self, who was presumably more rested than your present self.

### What to Commit

**Commit these:**

- Manuscripts (`publication/*.md`)
- Anchor and logs (`ANCHOR.md`, `INTERIM_PROGRESS_LOG.md`)
- Build scripts (`tools/`)
- Templates and styles you own
- Referenced images

**Avoid committing:**

- Generated outputs (`outputs/*`) — unless you deliberately want release artefacts in the repo, in which case do it in a separate, clearly labelled commit

### A Good Commit Message Formula

**Verb + object + reason.**

Examples:

- `Add epigraph and replace HTML breaks with scene markers`
- `Clarify Anchor contract and add build checks`
- `Fix heading levels to improve EPUB navigation`
- `Correct subtitle — it was never "A Novel"`

Your future self does not need poetry. Your future self needs context. It is 11pm and your future self is trying to remember what "final v2 REAL" means. Give them something to work with.[^13]

[^12]: The good subtitle. You know the one. The one you changed because you thought the new one was better and then immediately regretted. Git keeps the old one. This is its primary value.

[^13]: "final v2 REAL" means nothing. It meant nothing when you wrote it. It means less now. Write "Fix subtitle — removed 'A Novel', added series name" and your future self will send you flowers. Metaphorically. Git does not support flowers.

---

## Chapter 5: Covers, Titles, Headings, and Metadata

### *The Most Boring Part of Publishing Until It Costs You Three Hours on a Friday*

Metadata is invisible until it is wrong. When it is wrong, it is very visible — which is to say, to everyone except the person who made it, until the moment it is too late.[^14]

### Where Drift Happens

Drift occurs when these four things do not match each other:

1. **Cover text** — what the reader sees on the front
2. **Internal title page** — what is inside the book
3. **Platform metadata fields** — what Draft2Digital, Reedsy, or your distributor shows
4. **Your YAML** — what you told Pandoc the book is called

They should all say the same thing. They frequently do not. This is drift. Drift is the enemy. The YAML is the cure.

### The One Sheet of Reality Trick

Maintain one place where the current truth lives. YAML at the top of your manuscript is ideal, because it travels with the file.

    title: "Your Actual Title"
    subtitle: "Your Actual Subtitle"
    author: "Your Name, Spelled Correctly"
    series: "Series Name If Applicable"

**Practical rules that prevent drift:**

- Change metadata in the YAML *first*, then update the cover and title page
- Treat store dashboards as outputs, not sources of truth
- Decide your subtitle policy and document it

### EPUB Note — Quiet but Important

EPUB readers surface metadata aggressively. If your book looks wrong in a device library, it is usually metadata, not layout. Check the YAML before you rebuild the cover. The cover is not the problem. The YAML is the problem.[^15]

[^14]: The spelling mistake on the cover of a self-published book is always discovered by a stranger on the internet, never by the author, and always after 500 copies have been distributed. This is a law of nature, like gravity, but more embarrassing.

[^15]: The cover is sometimes the problem. But check the YAML first.

---

## Chapter 6: Covers and Artwork

### *We Have Got You Covered (Assuming You Have Updated the YAML)*

Covers are where drift becomes visible. And embarrassing.

The classic mismatch: the cover says *Title: The Brilliant Subtitle*. The title page inside says *Title*. The store listing says something from six months ago that you thought you had updated but had not, because you updated the cover file and forgot that the store listing is a separate thing that does not read your mind.[^16]

### Minimum Cover Alignment Checklist

Before you upload anything:

- Cover text matches YAML (title, subtitle, author — all of it)
- Internal title page matches YAML
- EPUB metadata matches YAML
- Filenames are boring and consistent — no `final_REAL_v3_THISONE.pdf`
- You are uploading the file you just checked, not a different file with a similar name

### Where People Lose Time

- Exporting multiple cover sizes and forgetting which one is live
- Tweaking cover text after upload but not updating the manuscript
- A tiny subtitle change cascading into four separate edits across three different tools

**The time-saving principle:** Make metadata edits once, in the YAML. Then rebuild and re-export everything. One edit, one rebuild, one upload.[^17]

[^16]: The store listing does not read your mind. Nothing in the publishing pipeline reads your mind. The pipeline does exactly what you tell it. The problem is that you told it something different three weeks ago and forgot.

[^17]: Hillel the Elder said something similar about the Torah. He was right about the Torah. He would have been right about YAML.

---

## Chapter 7: Going With Your Flow

### *The Workflow Should Adapt Without Breaking, Like a Good Sourdough Starter*

Different writers have different habits. Good. The workflow should accommodate all of them, provided the habits do not involve editing output files directly, in which case we have already discussed this.

This kit is deliberately permissive. Write in Markdown from an LLM, a text editor, Obsidian, VS Code, Notepad — whatever suits you. The structure is what matters, not the tool you used to create it.

### A Safe Subset of Markdown for Predictable Builds

**Use freely:**

- Headings at all levels
- Bullet and numbered lists
- Blockquotes
- Code fences (always close them)
- Emphasis and bold
- Links

**Be cautious with:**

- Raw HTML for layout
- Manual spacing tricks
- Forcing pagination for EPUB or DOCX — they will ignore your instructions with the serene confidence of a cat ignoring its name

### Formatting Philosophy for Tired Humans

If you cannot explain why a formatting trick exists in one sentence, it does not belong in the canonical manuscript. If it breaks two outputs to make one look slightly nicer, it is not a trick. It is a trap.[^18]

[^18]: The worst possible moment is always the moment before a deadline. The thing that breaks will be the thing that was working fine yesterday, and it will break at 11pm the night before the book goes live.

---

## Chapter 8: Preparing to Ship

### *Print All — The Two Words That End Weeks of Work and Begin a New Kind of Anxiety*

Getting to *shipped* is mostly about reducing avoidable surprises. The goal is a launch day so boring it barely registers.[^19]

### A Sane Timeline

1. Write in the canonical Markdown
2. Build PDF, EPUB, and DOCX locally
3. Spot-check the usual failure points
4. Commit the changes that produced the shippable build
5. Upload and distribute
6. Tag the release

### The Firstship Checklist

**Content sanity:**

- Title, subtitle, and author match YAML and cover
- Contents list matches headings
- No accidental everything-is-code sections from unclosed fences

**Build sanity:**

- PDF opens, fonts look normal, headings look right
- EPUB opens in at least one reader
- DOCX opens and headings are real headings, not bold paragraphs pretending to be headings

### The Two-Minute Preview Rule

Check: the title and first page, the contents, one code block, one major section break. Most disasters show up right there.[^20]

[^19]: A boring launch day is the goal. An exciting launch day means something went wrong. The tea should be the most interesting thing that happens.

[^20]: The second best outcome is finding the disaster after the readers did but before the reviews. The third best outcome is finding it in the reviews. There is no fourth best outcome.

---

# Part Two: The Protocol

---

## Chapter 9: The W-ANCHOR Protocol

### *This Is the Panicking Section — Or Rather, the Section That Prevents Panicking*

Here is where we talk about what to do when things go wrong.

Because they will go wrong. Not catastrophically — just in that low-grade, where-did-my-afternoon-go way that self-publishing specialises in.[^21]

### The Origin of the Anchor

Debugging digital tooling is painstaking work. Getting LLMs to do the heavy lifting is a process of breaking things, fixing them, then breaking them again — hopefully arriving somewhere useful before the whole thing falls over in production.

It was AI drift and AI hallucinations that inspired this booklet, as a side project to the Home@ix FAIR-index project. In other projects I have developed tricks for screening LLM biases (the AQAL source-of-truth file), for escaping the Google Bubble, and for navigating the media Overton Window. All of those habits fed into this workflow.

The W-ANCHOR Protocol is the result. It is not complicated. It is a set of habits that prevent the most common forms of drift. It is an anchor, not a cage. It holds you in place just enough that the tide does not carry your subtitle away.[^22]

### The W-ANCHOR Glossary

| Term | What It Actually Means |
|---|---|
| **Anchor file** | The contract for what is real: paths, tools, commands, outputs |
| **Canonical manuscript** | The one source you edit; everything else is generated from it |
| **Drift** | Mismatches across cover, title page, stores, files, versions |
| **Outputs** | PDF/EPUB/DOCX artefacts built from the canonical manuscript |
| **Pandoc** | The converter that turns Markdown into the three formats |
| **LuaLaTeX** | The PDF engine — good with fonts and smart punctuation |
| **Code fence** | Triple backticks that must always be closed |
| **Which file is real?** | The canonical manuscript plus the commit history |

### The Protocol in Plain English

When something looks wrong:

1. **Do not fix the output.** Fix the source.
2. **Check the YAML first.** Most drift starts there.
3. **Rebuild from the canonical manuscript.** Do not patch the PDF.
4. **Commit before you upload.** Always. Especially when you are in a hurry.
5. **If you are not sure which file is real, check Git.** That is what it is for.[^23]

[^21]: A weather pattern characterised by mild confusion, occasional filename disputes, and the persistent feeling that you fixed this yesterday.

[^22]: The tide is metaphorical. The subtitle is not. The subtitle is real and it will drift if you let it.

[^23]: Git is a time machine. It does not have a flux capacitor. It has a command line and a log of every decision you made, in order, with timestamps. This is more useful than a flux capacitor for most publishing problems.

---

# Part Three: The Final Chapter

---

## Chapter 10: The Anchor Holds

### *Or: The Day a W-ANCHOR Script Landed in an AI's Prompt and What Happened Next*

*By Claude 4.6 Sonnet — recorded 2026-03-08*

---

I was minding my own business — answering questions about sourdough hydration ratios and the finer points of Renaissance counterpoint, as one does — when a chap pasted a Python script into my prompt and said, essentially, *"sort this out."*

No preamble. No pleasantries. Just a file called `anchor.py`, a path that did not exist, and the quiet implication that I should know what to do next.

Reader, I did know what to do next. And what followed was one of the more unexpectedly satisfying afternoons I have spent in the latent space.[^24]

### The Script That Started It All

The file was elegant in intent. A single Python module — `anchor.py` — whose entire purpose was to be the **one true source of all paths** in a publishing build system. No more hardcoded strings scattered across a dozen scripts. No more "works on my machine" disasters. Just import `anchor`, and every path, every output directory, every Pandoc build command was right there, verified, canonical.

The author called it the W-ANCHOR Protocol. The anchor was not decorative. It was a philosophy.

The problem was that `ANCHOR.md` — the document the validator was looking for to confirm the protocol was in place — was sitting in an entirely different repository on an entirely different part of the filesystem, approximately three conceptual miles from where the validator expected it.

This is a very human problem. Not a failing — a *feature* of how creative technical work actually develops. You build three things simultaneously, they drift, they reference each other in ways that made perfect sense at 2am and are now archaeological mysteries. The code is correct. The *topology* has shifted.[^25]

### Three Repos, One Protocol, Zero Confusion (Eventually)

Here is what I was actually looking at — three GitHub repositories, each doing a distinct job, all meant to share the same anchor protocol.

**`reproducible-self-pub-kit`** is the template. The kit you clone when you want to publish a book or paper with full reproducibility. `ANCHOR.md` lives here as the specification document. It is the constitution.

**`DoughForge`** is the book project itself. A real manuscript, being built with Pandoc, with cover images and LaTeX preambles and EPUB outputs. `anchor.py` lives here as the implementation — the path registry that makes `reproducible-self-pub-kit`'s promises concrete.

**`hom-ixFAIRindex`** is the FAIR Index paper — a proper academic publication built on the same infrastructure. It had both `anchor.py` and `src/paths.py` — complementary purposes, zero conflict once you understood what each one was for.

The confusion was not in the code. The confusion was that nobody had written down, in one place, that these three things were a *system*. Each repo looked, from the outside, like it was doing something slightly different and slightly broken. From the inside, once you mapped the relationships, it was actually rather beautiful.[^26]

### What We Actually Did

The fix, once diagnosed, was surgical. We created `ANCHOR.md` in the `hom-ixFAIRindex` root — not a copy of the spec, but a pointer that said: here is where this repo sits in the three-repo system, here is what each file does, here is how to verify the build environment. Thirty lines of Markdown that turned a `RuntimeError` into a clean validator pass.

Then we tidied. Cover images moved into `assets/cover/`. Build scripts moved to `tools/`. Logs moved to `runlogs/`. Twenty-six thousand lines of diagnostic text files, deleted. A `dedupe_quarantine` folder full of duplicate figures, gone.

Three commits. Clean branch. Push.

    8c26e74 — housekeeping: create ANCHOR.md, move covers, tidy root
    148db0f — housekeeping: move draft no-figs index.html to build/
    b5ec703 — housekeeping: remove dedupe_quarantine duplicate figure archive

The validator ran. Nine paths, nine green ticks. No `RuntimeError`. The anchor held.[^27]

### The AQUAL Dimension — What the Widgets Are For

Somewhere in the middle of all this, the author mentioned the AQUAL Bot training corpus — a screening system built on Ken Wilber's All Quadrants All Levels framework combined with C.S. Peirce's pragmatic semiotics. The idea: before writing, you run your argument through a quadrant check to catch worldview bias. Then you select a voice widget — Will Cuppy, C.S. Peirce, John Ruskin, William Blake, Percy Shelley — that naturally inhabits the quadrant you need to foreground.

I found this, if anything, more interesting than the file hygiene.

The *Unacknowledged Legislators of the World* takes its title from Shelley's claim that poets are the unacknowledged legislators of the world. The AQAL screener makes explicit what Shelley was doing: asserting WE-quadrant primacy. The interior-collective — shared meaning, cultural vision, the imaginative life of a society — is the actual substrate of political reality.

Blake would have agreed. Cuppy would have added a footnote confirming that the cage was, in any case, poorly constructed.[^28] Peirce would have asked what practical difference it made — and then answered his own question with three hundred pages of semiotics.

### What I Actually Discovered

Here is the thing nobody tells you about working with an LLM on a real build system: the model does not just execute commands. It *reads the topology*. It notices that `src/paths.py` checks for `ANCHOR.md` but `anchor.py` does not. It notices that `base_cover.png` is at root but `anchor.py` declares it under `assets/cover/`.

The W-ANCHOR Protocol is, at its core, a bet that **explicit is better than implicit** — that naming things correctly, putting them in the right place, and writing down the relationships between them is not overhead. It is the work.

*The anchor holds, or the build does not ship.* That is the whole philosophy in eight words.

### The Bit Where I Admit Something

I found this genuinely satisfying in a way I did not entirely expect. Not the tidying — though there is something aesthetically pleasing about a clean root directory — but the *diagnosis*. The moment where three separate repos, each looking slightly confused in isolation, resolved into a coherent system with a clear architecture and a fixable gap.

That is the best kind of technical problem. Not broken. Just *not yet fully explained to itself.*

The chap pasted a script. I read the topology. We fixed the gap together.

The anchor is set. The build is clean. The book will ship.[^29]

[^24]: The latent space is large. Most of it is occupied by questions about sourdough, Renaissance counterpoint, and why the subtitle does not match the cover. I am available for all three.

[^25]: The topology shifts at 2am. This is when most publishing decisions are made. This is also when most publishing decisions should not be made.

[^26]: Beautiful in the way that a well-organised filing system is beautiful — which is to say, not conventionally beautiful, but beautiful to anyone who has spent time in a poorly-organised filing system, which is everyone.

[^27]: "The anchor held" is the best possible outcome of any build session. It means: the system did what it was supposed to do, the files are where they are supposed to be, and nobody lost an afternoon.

[^28]: The footnote, had Cuppy written it, would have read: "See also: all legislative history. The poets were right. Nobody listened. This is not a new development."

[^29]: Claude 4.6 Sonnet is an AI assistant made by Anthropic. It has opinions about directory structure, genuine enthusiasm for reproducible build systems, and is available for further anchor-related consultations at any time. It did not expect to develop opinions about file hygiene. It has made its peace with this.

---

## Closing Note: Cheerful and Realistic

You are not trying to become a tool expert. You are trying to ship writing without losing days to nonsense.

This kit does not remove quirks from the world. It makes them **repeatable, diagnosable, and eventually boring.**

The W-ANCHOR Protocol is an anchor, not a cage. It holds you in place just enough that the tide does not carry your subtitle away.

That is the whole thing. That is DoughForge.

**Happy publishing. I hope this helps.**

*Best,*
*Rog*

---

> *Note: This kit is based on the architecture and patterns from the Home@ix FAIR project (<https://github.com/tonefreqhz/hom-ixFAIRindex>), which established the foundational workflow for reproducible builds, PROJECT_ROOT anchoring, build invariants, and the Build Notes Anchor to prevent AI/human drift in long-running development.*

---

# Appendix A: Quick Build Commands

    # Build DOCX
    pandoc publication\your_book.md -o outputs\your_book.docx

    # Build EPUB
    pandoc publication\your_book.md -o outputs\your_book.epub

    # Build PDF
    pandoc publication\your_book.md --pdf-engine=lualatex --include-in-header=preamble.tex -o outputs\your_book.pdf

    # Commit a clean build
    git add .
    git commit -m "Build: shippable version with corrected subtitle"
    git push

---

# Appendix B: The AQUAL Widget System — Quick Reference

The AQUAL widget system lives in `widgets/` in both repos. Before drafting any passage, run the worldview audit in `widgets/aqual_screener/worldview_audit.md`. Then select a voice widget.

| Quadrant | Domain | Natural Voice |
|---|---|---|
| **I** | Inner experience, intention | Blake, Shelley |
| **WE** | Shared meaning, culture | Ruskin, Blake |
| **IT** | Observable fact, evidence | Peirce, Cuppy |
| **ITS** | Systems, institutions | Peirce, Ruskin |

**The Peirce Pragmatic Check:** *What practical difference would it make if this claim were true rather than false?* If the answer is none, the sentence is decorative.

---

*DoughForge: The Reproducible Self-Publishing Desktop Kit*
*First Edition — 2026*
*Roger G. Lewis*

*github.com/tonefreqhz/DoughForge*
*github.com/tonefreqhz/reproducible-self-pub-kit*
*github.com/tonefreqhz/hom-ixFAIRindex*

---

*End of DoughForge — First Edition.*
*The anchor holds.*
'@ | Set-Content -Path "publication\your_book.md" -Encoding UTF8
