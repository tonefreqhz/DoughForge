\# 3) Versioning with Git: stop selling yourself work you already did



Git is not here to turn you into a developer. It’s here to prevent these disasters:



\- “I fixed it yesterday. Where did it go?”

\- “Which draft did I upload?”

\- “I changed one tiny thing and now everything is different.”

\- “I need the previous subtitle back. The good one.”



\## The writer-friendly Git minimum



You can get 90% of the value with three commands:



```powershell

git status -sb

git add .\\publication\\pamphlet\_issue\_1.md

git commit -m "Explain what changed in one sentence"






