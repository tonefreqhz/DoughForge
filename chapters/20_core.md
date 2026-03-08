\# 2) Ground Truth: one manuscript, many outputs



Publishing pain usually comes from one root cause:



You stop knowing which file is the truth.



So we pick a truth and make everything else a rebuildable product of that truth.



\## The Ground Truth rule



One canonical manuscript (this Markdown file).  

Everything else is generated: PDF, EPUB, DOCX, cover embeds, metadata exports.  

If an output looks wrong, you do not fix the output. You fix the manuscript (or the build rules) and rebuild.  



This isn’t ideology. It’s how you keep launch day boring.



\## What counts as “canonical” (and what doesn’t)



\*\*Canonical (edit these):\*\*



\- `publication/pamphlet\_issue\_1.md`

\- any images referenced by the manuscript (covers, diagrams)

\- build scripts/templates you actually control (if used)



\*\*Artifacts (rebuild these):\*\*



\- `outputs/\*.pdf`

\- `outputs/\*.epub`

\- `outputs/\*.docx`



If you can regenerate it, don’t treat it like source.



\## The Anchor connection (no mysticism, just receipts)



Your `ANCHOR.md` is the contract that keeps you honest:



\- the repo layout you expect

\- the commands that should work

\- the checks you run when reality starts drifting



When you’re tired, “obvious” becomes “expensive.” Anchor files are cheap insurance.




