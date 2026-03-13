content = (
    "# Epilogue: The Protocol Goes Live\n\n"
    "*15:45, 13 March 2026. PowerShell 7.5.4. DoughForge repo root.*\n\n"
    "This book was built with the W-Anchor Protocol - a discipline for keeping\n"
    "AI assistants grounded to a single source of truth rather than drifting\n"
    "into plausible-sounding invention.\n\n"
    "The proof is not in the description. The proof is in the PowerShell window.\n\n"
    "---\n\n"
    "**Figure 1 - ANCHOR VERIFIED: all paths green, session anchored.**\n\n"
    "![W-Anchor Protocol live - path verification](../assets/images/w-anchor-live-1.png)\n\n"
    "---\n\n"
    "**Figure 2 - Committed, pushed, hooks installed. Protocol live on GitHub.**\n\n"
    "![W-Anchor Protocol live - git push confirmed](../assets/images/w-anchor-live-2.png)\n\n"
    "---\n\n"
    "Every output file in this repo is derived, never manually edited.\n"
    "Every session starts with:\n\n"
    "    cd C:\\Users\\peewe\\Documents\\DoughForge\n"
    "    .\\AutoAnchor.ps1\n\n"
    "*Built by Roger G. Lewis with Claude 4.6 Sonnet.*\n"
    "*The W-Anchor Protocol is MIT licensed.*\n"
    "*Repo: https://github.com/tonefreqhz/DoughForge*\n"
)

with open("publication/front_matter/epilogue_w_anchor.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Epilogue written.")
