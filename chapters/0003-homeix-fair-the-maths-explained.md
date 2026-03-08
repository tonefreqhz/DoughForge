# Home@ix DoughForge â€” The Maths Explained

This paper builds a **forward-looking affordability regime indicator** (DoughForge) for UK housing. The maths is deliberately simple â€” it's accounting identities and z-score composites, not econometric estimation. Here's a structured walkthrough of every mathematical piece, from the supply identities through to the final DoughForge number.

------------------------------------------------------------------------

## ðŸ—ï¸ 1. The Supply & Need Identities

These aren't statistical models â€” they're **accounting frameworks** that express housing as a throughput system where each factor is a multiplier. If any one term collapses toward zero, the whole product collapses.

### Identity 1: Affordable Market Supply (AMS)

\$\$AMS = (HM \cdot P \cdot AR \cdot D \cdot T \cdot PVC) + HS\$\$

This is a **multiplicative chain** â€” deliverable affordable housing is the product of:

| **Term** | **Meaning** |
|----|----|
| \$\$HM\$\$ | Housebuilding market capacity (actual deliverable output) |
| \$\$P\$\$ | Affordable proportion of that delivery |
| \$\$AR\$\$ | Absorption rate (how fast homes sell without destabilising price) |
| \$\$D\$\$ | Diversity of tenure/product mix (widens take-up) |
| \$\$T\$\$ | Throughput efficiency (permission â†’ start â†’ completion) |
| \$\$PVC\$\$ | Planning value capture that works in practice |
| \$\$HS\$\$ | Existing affordable housing stock (additive, not multiplicative) |

The key insight: because the first six terms are **multiplied**, a bottleneck in *any one* (say absorption rate drops near zero during a credit crunch) kills the entire flow â€” even if land, planning, and capacity are fine.

### Identity 2: Affordable Housing Need (AN)

Start from the expanded form:

\$\$AN = HD + (HM \cdot P \cdot AR \cdot D \cdot T \cdot PVC \cdot F) + HS - AMS + NCC\$\$

Now substitute the AMS definition and simplify. Since \$\$AMS = (HM \cdot P \cdot AR \cdot D \cdot T \cdot PVC) + HS\$\$, the \$\$HS\$\$ terms cancel and the multiplicative block partially cancels:

\$\$AN = HD + (HM \cdot P \cdot AR \cdot D \cdot T \cdot PVC \cdot (F - 1)) + NCC\$\$

- **\$\$HD\$\$** = HomeMaker effective demand (real household need, not just "bankable demand this quarter")
- **\$\$F\$\$** = sequencing/fast-tracking factor. At \$\$F = 1\$\$ (baseline), the middle term vanishes â€” need equals demand plus the credit stabiliser. When \$\$F \> 1\$\$, fast-tracking adds supply; when \$\$F \< 1\$\$, delays subtract it.
- **\$\$NCC\$\$** = New Circuit of Credit Creation â€” a ring-fenced funding channel for affordable delivery that doesn't just bid up existing stock prices.

This is the paper's structural claim in equation form: *need persists when supply is tethered to private-market throughput, and only a decoupled credit circuit can break the dependency.*

------------------------------------------------------------------------

## ðŸ“Š 2. DoughForge â€” The Indicator (Step by Step)

DoughForge converts the qualitative diagnosis ("markets clear through rationing, not repricing") into a **single reproducible number** each quarter.

### Step 1: Compute Year-on-Year Growth Rates

For house prices \$\$P_t\$\$, mortgage stock \$\$MB_t\$\$, and turnover \$\$TO_t\$\$:

\$\$g_t^P = \frac{P_t - P\_{t-4}}{P\_{t-4}}\$\$

\$\$g_t^{MB} = \frac{MB_t - MB\_{t-4}}{MB\_{t-4}}\$\$

\$\$g_t^{TO} = \frac{TO_t - TO\_{t-4}}{TO\_{t-4}}\$\$

(The subscript \$\$t-4\$\$ means "same quarter last year" in quarterly data.)

### Step 2: Compute the Creditâ€“Price Wedge

\$\$W_t = g_t^P - g_t^{MB}\$\$

This is the **core diagnostic variable**. When \$\$W_t \> 0\$\$, house prices are growing faster than the mortgage stock that finances them â€” prices are *decoupling* from credit.

### Step 3: Optional New-Build Share Change

\$\$\Delta NB_t = NB_t - NB\_{t-4}\$\$

A simple year-on-year difference (not a growth rate) in the new-build share of transactions.

### Step 4: Baseline Normalisation (Z-Scores)

Rather than z-scoring against the full history (which would let crisis periods distort what "normal" looks like), it pools two "relatively normal" windows:

- **2003Q1â€“2007Q4**
- **2013Q1â€“2019Q4**

For any series \$\$X_t\$\$:

\$\$z(X_t) = \frac{X_t - \mu_X}{\sigma_X}\$\$

where \$\$\mu_X\$\$ and \$\$\sigma_X\$\$ are computed **only from the baseline quarters**.

### Step 5: DoughForge Composite

**Three-component version:**

\$\$DoughForge_t = 100 \cdot \Big( 0.55 \cdot z(W_t) - 0.35 \cdot z(g_t^{TO}) + 0.10 \cdot z(\Delta NB_t) \Big)\$\$

**Two-component fallback** (when new-build data is unavailable):

\$\$DoughForge_t = 100 \cdot \Big( 0.55 \cdot z(W_t) - 0.35 \cdot z(g_t^{TO}) \Big)\$\$

### Step 6: Direction-of-Flow

\$\$\Delta DoughForge_t = DoughForge_t - DoughForge\_{t-1}\$\$

------------------------------------------------------------------------

## ðŸŽ¯ 3. Interpretation Bands

| **DoughForge range** | **Regime reading** |
|----|----|
| \$\$DoughForge \ge 50\$\$ | Strong deterioration risk |
| \$\$20 \le DoughForge \< 50\$\$ | Mild deterioration bias |
| \$\$-20 \le DoughForge \< 20\$\$ | Neutral / noisy |
| \$\$-50 \le DoughForge \< -20\$\$ | Mild improvement bias |
| \$\$DoughForge \< -50\$\$ | Strong improvement (often itself stress-driven â€” e.g., post-crash credit collapse) |

------------------------------------------------------------------------

## ðŸ” 4. Backtesting Framework

### Crash-Start Definition

A **crash start** is defined algorithmically as: - A local price peak followed by a drawdown of at least \$\$X\\\$\$ within \$\$Y\$\$ quarters - With a minimum cooldown of \$\$C\$\$ quarters between events

### Warning Rules (Illustrative)

| **Rule** | **Condition** | **What it captures** |
|----|----|----|
| A | \$\$DoughForge \> 20\$\$ for 2 consecutive quarters | Sustained elevated stress |
| B | \$\$\Delta DoughForge \> 5\$\$ for 2 consecutive quarters | Sustained acceleration |
| C | \$\$DoughForge \> 0\$\$ and \$\$\Delta DoughForge \ge 0\$\$ | Broad worsening (looser trigger) |

### Evaluation Metrics

- **Lead time**
- **False-positive rate**

------------------------------------------------------------------------

## ðŸ’¡ 5. Key Takeaways on the Maths

1.  **Supply identities** use multiplication to encode the "weakest link" property.
2.  **DoughForge is a weighted z-score composite** with a baseline that excludes crisis windows.
3.  **No parameters are estimated** â€” fixed weights by design.
4.  **Baseline choice** is the most consequential methodological decision.

------------------------------------------------------------------------

<div id="DoughForge" class="section">

## DoughForge Paper

<div>








