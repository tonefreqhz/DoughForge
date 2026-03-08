---
title: "DoughForge"
subtitle: "The Reproducible Self-Publishing Desktop Kit"
author: "Roger G. Lewis"
series: "DoughForge Guides"
series_number: 1
date: "2026"
language: en-GB
rights: "© 2026 Roger G. Lewis"
description: "A practical, cheerful guide to building a repeatable
self-publishing workflow using Markdown, Pandoc, and Git — so you
stop losing days to drift and start shipping books."
---

# DoughForge: The Reproducible Self-Publishing Desktop Kit

### *A Cheerful Manual for Writers Who Have Lost an Afternoon to a Subtitle*

**By Roger G. Lewis**
*Author of The Conquest of Dough, The Strawberry Manifesto, and other
works that exist in more versions than strictly necessary*

> *"No passion in the world is equal to the passion to alter someone
> else's draft."*
> — H. G. Wells[^1]

[^1]: Wells said this about other people's drafts. He did not
anticipate the self-publishing era, in which the writer, the editor,
the typesetter, and the person who accidentally uploaded the wrong PDF
are all the same person.

---

*This YAML block is not decorative. It is the contract. Everything
downstream of it — the PDF, the EPUB, the DOCX, the store listing,
the cover — should say the same thing. If it does not, you have drift.
Drift is what this book is about. We will return to drift.*[^2]

[^2]: We will return to drift the way you return to a dentist.
Regularly, reluctantly, and with the dawning realisation that the
problem would have been smaller if you had come sooner.

---

## Foreword: From a Cheerful Realist

I have published eleven books through Draft2Digital since 2018. Two
more are in the pipeline. That means I have had enough *oh no* moments
to qualify as a minor weather system.[^3]

The recurring theme was never incompetence. It was **drift**.

Titles drift. Covers drift. Internal title pages drift. Versions drift.
And suddenly your "final" file has cousins — loud, contradictory
cousins who all claim to be the real one and have opinions about the
subtitle.

This kit is how you stop drift from running your publishing schedule.
It will not make you a developer. It will not demand you love tooling.
It just asks that you stop fearing it — and that you give your future
self a fighting chance.

The pamphlet you are holding is a small answer to one question: *which
file is the real one?*

Not glamorous. Just reliably boring — and boring, in publishing, is a
superpower.[^4]

[^3]: A minor weather system characterised by sudden drops in
confidence, localised confusion about filenames, and the occasional
catastrophic front where the cover says one thing and the title page
says another.

[^4]: Glamour is for book launches. Boring is for the six months
before the book launch when you are trying to remember which version
of Chapter 4 you actually sent to the formatter.

---

# Part One: The Kit

---

## Chapter 1: The Reproducible Self-Publishing Desktop Kit

### *Release Notes for Writers Who've Been Burned*

There is a line buried in early UNIX source code that reads:

> *"You are not expected to understand this."*

It was not a challenge. It meant: *this will not be on the exam.*

So naturally, it is on the exam.[^5]

Not because you need to become a compiler archaeologist, but because
modern publishing tools have the same bad habit as old systems code —
they quietly accumulate quirks, and then you lose an afternoon (or a
launch date) to something you were never warned about. The quirks do
not announce themselves. They wait. They are patient in the way that
only inanimate software can be patient, which is to say: completely,
and without mercy.

This pamphlet is a small act of civil engineering:

- **One canonical manuscript** — the single source of truth for your
  book
- **A repeatable build** — producing PDF, EPUB, and DOCX from that
  one source
- **A boring paper trail** — so nothing drifts without you noticing

You already know how to write. The frustrating part is everything
*around* the writing: the title that does not match, the cover that
shifted between Tuesday and Thursday, the EPUB that behaves perfectly
until a platform preview invents new physics, and the eternal haunting
question that follows you to bed:

*Which file is the real one?*

This pamphlet is a small answer. One canonical manuscript. One
repeatable build. Version history you can trust. Not glamorous. Just
reliably boring.

You do not have to love tooling. You just should not have to fear
it.[^6]

[^5]: The exam consists of one question: "Why does the store listing
say the subtitle is 'A Novel' when you changed it to 'A Memoir' in
March?" Full marks are awarded for correctly identifying which of your
seventeen saved versions is canonical. Partial credit is available for
crying.

[^6]: Fear of tooling is rational. The tools have earned it. This kit
is an attempt to make the tools slightly less terrifying by making
their behaviour slightly more predictable. It is the publishing
equivalent of a leash.

---

## Chapter 2: Origin Story

### *The Quirks That Ate Publication Day*

Every self-publisher has a story.

Mine involves a cover that said one subtitle, an internal title page
that said another, and a store listing that had apparently been updated
by a ghost with strong opinions about punctuation.[^7]

I have published eleven books. I have had this experience — in various
configurations — approximately eleven times. The details change. The
structure does not. It always begins with confidence (*I checked
everything*), proceeds through confusion (*but I definitely checked
it*), and arrives at the same destination: a file called
`final_REAL_v3_THISONE.pdf` that is not, in any meaningful sense,
final, real, or the one.

The common culprits are always the same:

**Cover title/subtitle does not match the internal title page.**
Looks fine in your head. Looks wrong to every reader. The cover says
*The Conquest of Dough: A History of Bread and Power*. The title page
says *The Conquest of Dough*. The store listing says *The Conquest of
Dought* because autocorrect had opinions.

**EPUB respects headings; DOCX decides to improvise.**
Pandoc is good. Platform converters are adventurous. Your carefully
structured heading hierarchy arrives at the other end looking like it
was formatted by someone who had heard of headings but never personally
encountered one.

**Scene breaks turn into mystery blank space — or, worse, mystery no
space.**
You put three asterisks. The converter put nothing. Or a line. Or a
small existential crisis rendered in whitespace.

**Previews look fine until the store conversion does its own thing.**
You checked it. You *definitely* checked it. The preview was perfect.
The live version has decided that your chapter titles should be in a
font that does not exist on any device manufactured after 2009.

**You fix one thing and accidentally upload a different file than the
one you just fixed.**
This one is the most demoralising. It is also the most preventable.
It is what this entire book is about.[^8]

The fix is not heroic. It is practical.

**Write down reality. Then make the tools obey it.**

That is what an Anchor file is for — a plain, boring contract that
says: *these paths are real, these commands work on this machine, this
is the source, and these are the outputs.* It does not prevent quirks.
It makes them findable. And findable is most of the battle.

[^7]: The ghost's preferred subtitle was "Revised Edition," which was
not accurate, not requested, and not removable without contacting
support. The ghost has since moved on to haunt other people's metadata.

[^8]: The entire book is about this one problem. The problem has many
faces. The solution has one face. It is a boring face. We are going to
look at it for several chapters.

---

> **Prompt Box: Check What's Real Before You Fix What Isn't**
>
> **Pitfall: Notepad + OneDrive + Markdown fences**
>
> If Notepad offers to "clear all and save new" or says it cannot find
> the file — **stop**. Verify you are editing the file you think you
> are. In synced folders like OneDrive, the file can change while
> Notepad has it open. This is not a bug. It is a feature that has
> been designed specifically to ruin your afternoon.[^9]
>
> Also: Markdown code fences are literal. If you open a fenced block
> with ` ``` ` and forget the closing, the rest of your document
> becomes code. Your PDF will look extraordinary. Not in a good way.
>
> **Two quick checks before every build:**
>
> 1. Confirm the manuscript file is real and non-empty.
> 2. Count your code fences — they come in pairs, like socks, and a
>    missing one causes similar levels of frustration.

[^9]: OneDrive is brilliant at many things. Knowing when you want it
to sync and when you want it to leave your file alone is not among
them. This is not a criticism. It is a weather report.

---

## Chapter 3: Inside the Publishing Pain Locker

### *Or: Why You Keep Losing Afternoons to Things That Should Take Five Minutes*

Publishing pain usually comes from one root cause.

**You stop knowing which file is the truth.**

This sounds simple. It is not simple. It is the kind of problem that
starts as a minor inconvenience on a Tuesday and becomes a full
structural crisis by Thursday, when you realise that the file you
uploaded to the store, the file on your desktop, and the file in your
email to the formatter are three different documents that have been
diverging quietly since March.[^10]

So we pick a truth. And we make everything else a rebuildable product
of that truth.

### The Ground Truth Rule

**One canonical manuscript. Everything else is generated.**

If an output looks wrong, you do not fix the output. You fix the
manuscript — or the build rules — and you rebuild. This is not
ideology. It is how you keep launch day boring. Boring launch days are
good launch days. Exciting launch days are the ones where you discover
the wrong file at 11pm.

**Edit these:**

- `publication/your_book.md` — the manuscript. The truth. The one.
- Images referenced by the manuscript (covers, diagrams, that one
  chart you made in Excel at 2am)
- Build scripts and templates you actually control

**Rebuild these — never edit directly:**

- `outputs/*.pdf`
- `outputs/*.epub`
- `outputs/*.docx`

If you can regenerate it, do not treat it like source. The moment you
start "just quickly fixing" a PDF directly, you have created a cousin.
The cousins will multiply. They will have children. The children will
have opinions about the subtitle.[^11]

### The Anchor Connection — No Mysticism, Just Receipts

Your `ANCHOR.md` file is the contract that keeps you honest. It
contains:

- The repo layout you expect
- The commands that should work
- The checks you run when reality starts drifting

It is not magic. It is a receipt. When you are tired and confused and
staring at four files with similar names, the Anchor file is the thing
you open to remember what is real.

When you are tired, *obvious* becomes expensive. Anchor files are
cheap insurance.[^12]

[^10]: March is when most publishing drift begins. This is not
scientifically established. It is experiential.

[^11]: The cousins are not malicious. They are just the natural result
of editing outputs instead of sources. They multiply because every
time you fix one, you create another. This is the publishing
equivalent of the Hydra, except the heads are all slightly different
versions of Chapter 4.

[^12]: The cheapest insurance is a text file. The most expensive
insurance is discovering, at upload time, that you have been editing
the wrong file for three weeks.

---

## Chapter 4: Git and the Kit

### *Version Control Without the Drama, or: Stop Selling Yourself Work You Already Did*

Git is not here to turn you into a developer.

Git is here to prevent these specific disasters:

- *"I fixed it yesterday. Where did it go?"*
- *"Which draft did I upload?"*
- *"I changed one tiny thing and now everything is different."*
- *"I need the previous subtitle back. The good one. The one from
  before."*[^13]

### The Writer-Friendly Git Minimum

You can get 90% of the value with three commands:

```bash
git add .
git commit -m "describe what you just did"
git log --oneline
