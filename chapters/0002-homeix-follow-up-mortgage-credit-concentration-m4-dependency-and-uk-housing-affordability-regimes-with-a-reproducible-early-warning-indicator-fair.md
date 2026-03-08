# **Home@ix Follow-up:** Mortgage-Credit Concentration, M4 Dependency, and UK Housing Affordability Regimes â€” With a Reproducible Early-Warning Indicator (DoughForge)

**Author:** Home@ix (Working Paper / Draft)

**Date:** 25 February 2026

</div>

<div class="section abstract" aria-label="Abstract">

## Abstract

The UK housing affordability crisis is commonly presented as a price-to-income problem. That framing is incomplete in regimes where housing markets do not clear through price adjustment. Under stress, clearing occurs through quantities and composition: turnover falls, chains fail, mortgage-dependent households are rationed out, and the observed price level becomes a lagging and selected statistic.

This paper connects four reinforcing dimensions: (i) credit impairment risk in commercial banks under mortgage-credit concentration, (ii) mortgage lending over-reliance and collateral feedback, (iii) structural dependency of broad money growth on mortgage credit creation, and (iv) affordability deterioration as an access-and-allocation outcome. It then operationalises the diagnosis using **Home@ix DoughForge**, a transparent quarterly indicator designed as a **2â€“3 year forward regime signal** for affordability understood as throughput and access. DoughForge combines a creditâ€“price decoupling wedge with a market-depth (turnover) term, optionally augmented by composition proxies.

</div>

<div class="section">

## Executive Summary

UK housing stress is not only about â€œhigh prices.â€ It is also about **who can transact** and **how the market clears**. When mortgage credit tightens or uncertainty rises, the UK market often clears via **reduced participation** rather than orderly repricing: transactions fall, turnover collapses, and cash-rich buyers gain share.

<div class="callout">

**Core claim:** mortgage-credit concentration in banks links financial stability and affordability. When mortgage flows weaken, deposit creation weakens; when deposit growth weakens, the real economy tightens; when the economy tightens, arrears risks rise; and when arrears risks rise, credit supply tightens further. Affordability deteriorates via allocation and throughput failure.

</div>

### Key findings (sense-checked, definitions required in final)

- **Mortgage concentration is systemic:** residential mortgages comprise a large share of UK bank private-sector lending stock, increasing transmission from housing shocks to bank balance sheets.
- **Broad money is mortgage-sensitive:** when mortgage lending slows, broad money growth can undershoot nominal activity trends, reinforcing tight conditions.
- **Near-term supply is throughput-constrained:** major housebuilders pace sales within a narrow absorption band (sales per outlet per week), limiting market clearing via volume.
- **Affordability is an allocation problem in stress:** turnover collapses and buyer composition shifts (cash share rises), so the market â€œclearsâ€ by rationing access rather than by repricing alone.
- **DoughForge provides an operational monitor:** DoughForge detects creditâ€“price decoupling and thinning market depth, giving a forward-looking regime signal consistent with the diagnosis.

</div>

<div class="section">

## 1. The Integrated Mechanism: Why These Four Dimensions Move Together

The four dimensionsâ€”bank credit quality, mortgage concentration, broad money dynamics, and affordabilityâ€”are often analysed separately. In practice, they form a coupled system with feedback loops.

### 1.1 System sketch (feedback loops)

- **Mortgage concentration loop:** house prices and employment shocks affect arrears and loss expectations, which tighten underwriting and reduce credit availability.
- **Endogenous money loop:** mortgage lending creates deposits; weakening mortgage flows reduce broad money growth, which can tighten spending conditions and worsen employment.
- **Thin-market loop:** tighter credit reduces the set of eligible buyers; turnover falls; observed prices become â€œstickierâ€ and more selected; access worsens even if the price index moves slowly.
- **Developer pacing loop:** when demand weakens, builders protect margins by controlling release pace; volume cannot rise enough to clear via supply in the near term.

This paper treats â€œaffordabilityâ€ as the regime outcome of these loops, not as a single ratio.

</div>

<div class="section">

## 2. Credit Impairment: Surface Health vs Structural Fragility

Headline arrears and delinquency can look stable even as systemic vulnerability rises, because compositional selection improves the observed pool of borrowers while stress accumulates in marginal cohorts (recent high-LTV buyers, BTL, renters-in-distress feeding landlord stress).

### 2.1 Why low arrears can be misleading

- **Selection effects:** improved observed arrears may partly reflect that the stressed tail stops transacting or is screened out of new lending.
- **Threshold reporting:** â€œserious arrearsâ€ definitions can miss earlier-stage stress that predicts later acceleration.
- **BTL as leading indicator:** landlord cashflows are more directly exposed to rate changes and tenant stress; BTL arrears can precede broader deterioration.

### 2.2 Debt servicing: risk rises continuously

If arrears probability increases roughly linearly beyond a low-stress floor, then stability depends on distribution shifts, not just tail events. Small rightward shifts in the debt-servicing distribution can move a meaningful share of households into elevated stress.

</div>

<div class="section">

## 3. Mortgage Lending Concentration and M4 Dependency

In an endogenous money system, bank lending and deposit creation are linked. If mortgage lending dominates bank balance sheets, then housing-credit cycles imprint onto broad money dynamics and can propagate to the real economy.

### 3.1 What â€œM4 dependencyâ€ means operationally

- **Mechanism:** new mortgage lending creates deposits; weak mortgage origination can weaken deposit growth.
- **Interpretation:** slowing broad money growth is not mechanically â€œbad,â€ but it becomes a stress signal when it coincides with tight credit, weak turnover, and rising delinquency risk.
- **Empirical caution:** velocity and portfolio shifts matter; M4 is best used as a regime indicator alongside housing-credit and turnover measures.

</div>

<div class="section">

## 4. Housing Affordability as Market Clearing: Access, Allocation, Throughput

In stressed regimes, housing markets can fail to clear via prices and instead clear via participation constraints: fewer mortgage-dependent buyers qualify, chains break more often, and turnover collapses.

### 4.1 Compositional clearing

- **Turnover collapse:** when transactions fall relative to stock, the market becomes thin; observed prices reflect a narrower set of buyers and properties.
- **Buyer-type rationing:** higher cash shares can coexist with sticky prices because cash demand clears the marginal flow even as mortgaged households are excluded.
- **Distributional harm:** renters and younger cohorts experience the binding constraint (access), even when average ratios look stable.

### 4.2 The absorption-rate constraint (near term)

New-build supply often cannot surge quickly enough to restore clearing through volume because developers pace sales (per outlet per week) to optimise margins and manage risk. This creates a throughput constraint that is institutional/incentive-driven, not purely physical.

</div>

<div class="section">

## 5. From Diagnosis to Tooling: The Home@ix DoughForge Indicator

The diagnosis implies two observable precursors to allocation stress that are available in aggregate data: **creditâ€“price decoupling** and **thin-market clearing**. DoughForge is a reduced-form index that combines both.

### 5.1 Inputs (quarterly)

- House prices (level): `avg_house_price_gbp`
- Mortgage stock (level, Â£m): `mb_total_gbp_m`
- Turnover (market depth): `turnover_pct_q`
- Optional: new-build share: `newbuild_share_of_transactions`
- Quarter index: `period`; geography: `geo` (e.g., EW)

### 5.2 Derived series

Define year-on-year growth rates:

<div class="eq">

\$\$ g_t^P = YoY(P_t) \$\$

</div>

<div class="eq">

\$\$ g_t^{MB} = YoY(MB_t) \$\$

</div>

<div class="eq">

\$\$ g_t^{TO} = YoY(TO_t) \$\$

</div>

Define the creditâ€“price wedge:

<div class="eq">

\$\$ W_t = g_t^P - g_t^{MB} \$\$

</div>

Optional new-build share change (YoY):

<div class="eq">

\$\$ \Delta NB_t = NB_t - NB\_{t-4} \$\$

</div>

</div>

<div class="section">

## 6. Baseline Normalisation (Core Proviso)

To avoid defining â€œnormalâ€ using crisis regimes and structural breaks, z-scores are computed from pooled baseline windows:

- **Baseline windows:** 2003Q1â€“2007Q4 and 2013Q1â€“2019Q4
- **Excluded:** 2008â€“2012 (GFC and aftermath) and 2020+ (Covid and subsequent regime breaks)

For any series \$\$X_t\$\$, define:

<div class="eq">

\$\$ z(X_t) = \frac{X_t - \mu_X}{\sigma_X} \$\$

</div>

where \$\$\mu_X\$\$ and \$\$\sigma_X\$\$ are computed using baseline quarters only.

</div>

<div class="section">

## 7. DoughForge Definition, Interpretation, and Monitoring

DoughForge is scaled for interpretability and designed to be auditable. Weights are intentionally simple and can be stress-tested.

### 7.1 DoughForge definition

Default (three-component) specification:

<div class="eq">

\$\$ DoughForge_t = 100 \cdot \Big( 0.55 \cdot z(W_t) - 0.35 \cdot z(g_t^{TO}) + 0.10 \cdot z(\Delta NB_t) \Big) \$\$

</div>

If the new-build term is not available:

<div class="eq">

\$\$ DoughForge_t = 100 \cdot \Big( 0.55 \cdot z(W_t) - 0.35 \cdot z(g_t^{TO}) \Big) \$\$

</div>

### 7.2 Direction-of-flow

<div class="eq">

\$\$ \Delta DoughForge_t = DoughForge_t - DoughForge\_{t-1} \$\$

</div>

The level indicates regime pressure; the first difference indicates acceleration or easing.

### 7.3 Practical interpretation bands

- \$\$DoughForge \ge 50\$\$: strong deterioration regime risk
- \$\$20 \le DoughForge \< 50\$\$: mild deterioration bias
- \$\$-20 \le DoughForge \< 20\$\$: neutral/noisy
- \$\$-50 \le DoughForge \< -20\$\$: mild improvement bias
- \$\$DoughForge \< -50\$\$: strong improvement regime (often stress-driven)

</div>

<div class="section">

## 8. Evaluation: Event-Based Backtesting (Crash-Start Definitions)

DoughForge can be evaluated as an early-warning tool using objective event definitions rather than narrative dating.

### 8.1 Crash-start events (rule-based)

A â€œcrash startâ€ may be defined as a local price peak followed by a drawdown of at least \$\$X\\\$\$ within \$\$Y\$\$ quarters, with a minimum separation (cooldown) of \$\$C\$\$ quarters to avoid double-counting clustered peaks.

### 8.2 Illustrative warning rules

- A: sustained level stress: \$\$DoughForge \> 20\$\$ for 2 quarters
- B: sustained acceleration: \$\$\Delta DoughForge \> 5\$\$ for 2 quarters
- C: broad stress-worsening: \$\$DoughForge \> 0\$\$ and \$\$\Delta DoughForge \ge 0\$\$

### 8.3 Metrics

- Lead time (quarters) from the most recent signal to each crash start
- False-positive proxy: share of signal quarters not followed by any crash start within a forward window (e.g., 8 quarters)

</div>

<div class="section">

## 9. Outputs and Visualisations (Reproducible)

This draft renders the latest DoughForge assets directly from the Home@ix output folders. All paths below are **relative to the server root** (the folder you run `py -m http.server` in).

### 9.1 DoughForge headline level

<figure>
<img src="assets/figures/fig_DoughForge_level.png" alt="Home@ix DoughForge: Level (outputs/figures)" />
<figcaption><strong>Figure 1.</strong> Home@ix DoughForge (level). Source: <code>assets/figures/fig_DoughForge_level.png</code></figcaption>
</figure>

<figure>
<img src="assets/DoughForge_assets/fig_DoughForge_level.png" alt="Home@ix DoughForge: Level (outputs/DoughForge_assets)" />
<figcaption><strong>Figure 1b.</strong> Home@ix DoughForge (level). Source: <code>assets/DoughForge_assets/fig_DoughForge_level.png</code></figcaption>
</figure>

------------------------------------------------------------------------

### 9.2 Component contributions

<figure>
<img src="assets/figures/fig_DoughForge_contrib.png" alt="Home@ix DoughForge: Contributions (outputs/figures)" />
<figcaption><strong>Figure 2.</strong> DoughForge component contributions. Source: <code>assets/figures/fig_DoughForge_contrib.png</code></figcaption>
</figure>

<figure>
<img src="assets/DoughForge_assets/fig_DoughForge_contributions.png" alt="Home@ix DoughForge: Contributions (outputs/DoughForge_assets)" />
<figcaption><strong>Figure 2b.</strong> DoughForge component contributions. Source: <code>assets/DoughForge_assets/fig_DoughForge_contributions.png</code></figcaption>
</figure>

------------------------------------------------------------------------

### 9.3 Direction-of-flow (animated GIFs)

<figure>
<img src="assets/figures/anim_DoughForge_flow.gif" alt="DoughForge direction-of-flow animation (outputs/figures)" />
<figcaption><strong>Figure 3.</strong> Direction-of-flow animation. Source: <code>assets/figures/anim_DoughForge_flow.gif</code></figcaption>
</figure>

<figure>
<img src="assets/DoughForge_assets/anim_DoughForge_direction_of_flow.gif" alt="DoughForge direction-of-flow animation (outputs/DoughForge_assets)" />
<figcaption><strong>Figure 3b.</strong> Direction-of-flow animation. Source: <code>assets/DoughForge_assets/anim_DoughForge_direction_of_flow.gif</code></figcaption>
</figure>

------------------------------------------------------------------------

### 9.4 Backtest / evaluation figures

<figure>
<img src="assets/draft_paper_assets/fig_price_and_DoughForge_with_crisis_starts.png" alt="Price and DoughForge with crash starts" />
<figcaption><strong>Figure 4.</strong> Prices and DoughForge with crash-start annotations. Source: <code>assets/draft_paper_assets/fig_price_and_DoughForge_with_crisis_starts.png</code></figcaption>
</figure>

<figure>
<img src="assets/draft_paper_assets/fig_avg_leadtime_by_signal.png" alt="Average lead time by signal rule" />
<figcaption><strong>Figure 5.</strong> Average lead time by signal rule. Source: <code>assets/draft_paper_assets/fig_avg_leadtime_by_signal.png</code></figcaption>
</figure>

If any image fails to load, your Python server console will log a 404 showing the exact path requested.

</div>

<div class="section">

## 10. Policy and Structural Reform (Implications of the Regime View)

Standard levers (rate cuts, planning reform, time-limited subsidies) can influence symptoms without breaking the feedback loops. If affordability deterioration is driven by allocation and throughput failure under mortgage-credit dominance, then structural reform must address credit channel design and tenure/ownership pathways.

| **Problem loop** | **Symptom-focused lever** | **Structural lever (examples)** |
|----|----|----|
| Mortgage-credit dominance ties stability to housing | Macroprudential tweaks, temporary guarantees | Ring-fenced affordable housing credit; alternative tenure finance |
| Thin-market clearing excludes mortgaged households | Stamp duty holidays, small buyer grants | Shared equity/co-op models; community land trusts |
| Developer pacing constrains near-term throughput | Planning speed, incentives to build | Counter-cyclical delivery vehicles; public options for build-to-live |

</div>

<div class="section">

## 11. Limitations and Extensions

DoughForge is intentionally reduced-form. It captures two dominant mechanisms but does not directly encode: arrears microdata, cash-buyer share, investor/renter distress transmission, or explicit developer pacing series. These are natural extensions that can be layered as satellite indicators.

</div>

<div class="section">

## 12. Conclusion

UK housing affordability is not only a price level story; it is a regime story about who can transact and how the market clears when credit tightens. Mortgage-credit concentration links affordability outcomes to financial stability dynamics, and broad money conditions can amplify stress. Home@ix DoughForge translates this diagnosis into an operational, reproducible monitor of regime risk by combining creditâ€“price decoupling with market depth.

</div>

<div class="section">

## Reproducibility Note

Expected output directory contents (adjust to your workflow):

- `assets/DoughForge_assets/DoughForge_quarterly_audit.csv`
- `assets/figures/fig_DoughForge_level.png`
- `assets/figures/fig_DoughForge_contrib.png`
- `assets/figures/anim_DoughForge_flow.gif`
- `assets/DoughForge_assets/fig_DoughForge_level.png`
- `assets/DoughForge_assets/fig_DoughForge_contributions.png`
- `assets/DoughForge_assets/anim_DoughForge_direction_of_flow.gif`
- `assets/draft_paper_assets/fig_price_and_DoughForge_with_crisis_starts.png`
- `assets/draft_paper_assets/fig_avg_leadtime_by_signal.png`

</div>

</div>

------------------------------------------------------------------------

<div id="DoughForge-preface" class="section">

## DoughForge â€” Professional summary (LinkedIn-style)

This section is a distilled, non-technical bridge into the DoughForge working paper. It is written for housing policy, finance, and economics audiences.

<div class="box">

**Thesis:** The UK housing crisis isnâ€™t only about prices. In stressed regimes, markets can â€œclearâ€ through **exclusion**, not repricing.

When turnover collapses and mortgage-dependent households are screened out, the reported price index becomes a *selected statistic* generated by a thinner, wealthier transacting set.

</div>

### The coupled system (four loops)

1.  **Bank credit quality and mortgage concentration**
2.  **Mortgage lending and broad money dynamics** (deposit creation / M4 channel)
3.  **Supply delivery constraints** and developer pacing within absorption bands
4.  **Affordability** understood as access-and-allocation, not only burden ratios

### Why â€œlow arrearsâ€ can be a false comfort

Headline arrears can look stable even as vulnerability rises, because the observed borrower pool can improve via **compositional selection** (marginal cohorts stop transacting or are screened out of new lending). Buy-to-let arrears can behave as a leading indicator when landlord cashflows tighten.

### Introducing DoughForge (a forward regime signal)

DoughForge is a quarterly indicator designed as a **2â€“3 year forward regime signal** for affordability as access/allocation. It combines:

- **Creditâ€“price decoupling** (a creditâ€“price wedge)
- **Market depth** (turnover dynamics relative to stock)
- *Optional:* new-build share dynamics as a composition proxy

<div class="box">

**Transparent form (as used in this project):**

\$\$DoughForge = 100 \times (0.55 \times \text{creditâ€“price wedge} - 0.35 \times \text{turnover growth} + 0.10 \times \Delta\text{new-build share})\$\$

Components are z-scored against pooled baseline windows (2003â€“2007 and 2013â€“2019) to avoid structural-break periods.

</div>

### Interpretation bands

| DoughForge level | Regime signal                            |
|------------|------------------------------------------|
| â‰¥ 50       | Strong deterioration risk                |
| 20 to 50   | Mild deterioration bias                  |
| âˆ’20 to 20  | Neutral / noisy                          |
| âˆ’50 to âˆ’20 | Mild improvement bias                    |
| \< âˆ’50     | Strong improvement (often stress-driven) |

### Policy implication (what gets missed)

If affordability deterioration is driven by **allocation and throughput failure under mortgage-credit dominance**, then symptom levers alone (temporary subsidies, short-run tax changes) can lag the regime shift.

| Problem loop | Symptom lever | Structural lever |
|----|----|----|
| Mortgage-credit dominance ties stability to housing | Macroprudential tweaks, temporary guarantees | Ring-fenced affordable housing credit; alternative tenure finance |
| Thin-market clearing excludes mortgaged households | Buyer grants, transaction stimulus | Shared equity, co-op models, community land trusts |
| Developer pacing constrains near-term throughput | Planning speed incentives | Counter-cyclical delivery vehicles; public build-to-live options |

<div class="box">

**Bridge:** The DoughForge paper that follows formalises the measurement, definitions, and reproducible build for this indicator.

</div>

</div>

------------------------------------------------------------------------








