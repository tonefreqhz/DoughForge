# **Home@ix DoughForge:** A Forward Indicator of UK Housing Affordability Regimes Using Creditâ€“Price Decoupling and Market Depth

**Author:** Home@ix (Working Paper / Draft)

**Date:** 25 February 2026

</div>

<div class="section abstract" aria-label="Abstract">

## Abstract

UK housing affordability is usually discussed as a price level or a price-to-income ratio. That framing is necessary but incomplete because UK housing markets often do not clear primarily through price adjustment. In stressed regimes, markets clear through quantities and composition: turnover collapses, chains fail, mortgage-dependent households are rationed out, and observed prices can appear sticky or misleading. This paper introduces Home@ix DoughForge: a quarterly indicator designed as a 2â€“3 year forward regime signal for affordability understood as access and allocation, not only price burden. DoughForge is intentionally reduced-form and reproducible. It integrates a creditâ€“price wedge (prices outrunning mortgage-stock growth), a market-depth term (turnover dynamics) capturing thin-market clearing, and an optional composition term (new-build share dynamics). To avoid defining â€œnormalâ€ using crisis regimes and structural breaks, DoughForge is normalised to pooled baseline windows excluding the Global Financial Crisis aftermath and Covid-era disruptions. DoughForge is paired with a direction-of-flow statistic and can be evaluated via event-based backtesting (drawdown-defined crash starts). Together, the index and backtests form an operational toolkit for monitoring affordability regime risk.

</div>

<div class="section">

## Executive Summary

UK housing affordability is typically treated as a static burden ratio. Yet housing is not a frictionless market. When credit tightens or uncertainty rises, the UK housing market frequently clears via reduced participation rather than orderly repricing: transactions fall, turnover collapses, and access deteriorates even when price ratios appear stable.

This paper introduces **Home@ix DoughForge**, a reproducible quarterly indicator designed to act as a **2â€“3 year forward regime signal** for affordability understood as **access and allocation**. DoughForge integrates:

- a **creditâ€“price wedge** capturing decoupling between house-price growth and mortgage-stock growth;
- a **market-depth / turnover term** capturing thin-market (quantity-clearing) stress; and
- an **optional composition term** based on new-build share dynamics.

To avoid contaminating baseline moments with crisis regimes and structural breaks, DoughForge is normalised using pooled baseline windows:

- **Baseline windows:** 2003Q1â€“2007Q4 and 2013Q1â€“2019Q4
- **Excluded:** 2008â€“2012 (GFC and aftermath) and 2020+ (Covid and subsequent regime breaks)

DoughForge is accompanied by a direction-of-flow measure and can be assessed as an early-warning tool using objective event definitions (e.g., crash starts defined by drawdowns from local peaks).

</div>

<div class="section">

## Introduction: Affordability as Access, Allocation, and Market Clearing

Standard affordability measures (e.g., price-to-income ratios) treat affordability as a price-only object. But UK housing often fails to clear under stress through price adjustment. Instead, the system shifts toward thin-market clearing:

- transactions decline sharply;
- the transacting population becomes more selected (composition shifts);
- access deteriorates even if headline price ratios appear stable.

This paper therefore treats affordability as a **regime outcome** shaped by credit creation, market depth, and institutional constraints, and introduces an indicator designed to detect when the system is moving into a regime where affordability is likely to deteriorate over the next 2â€“3 years.

</div>

<div class="section">

## From Descriptive Diagnosis to a Forward-Looking Tool

Home@ix begins from an integrated diagnosis: mortgage-credit dominance in bank balance sheets, endogenous money creation via bank lending, and housingâ€™s role as both a necessity and collateral asset. Moving from diagnosis to a forward-looking tool requires operationalising how stressed regimes appear in observable data.

### Why â€œforward-lookingâ€ is operationally meaningful here

A forward-looking affordability signal must capture two patterns that commonly precede later deterioration:

- **Creditâ€“price decoupling:** price growth outruns mortgage-stock growth.
- **Thin-market clearing:** market depth collapses (turnover declines), indicating rationing and throughput failure.

DoughForge integrates these mechanisms into a single auditable index with an explicit baseline definition.

</div>

<div class="section">

## Data and Reproducible Construction

DoughForge is computed from quarterly series produced by the Home@ix feature set.

### Inputs (quarterly)

Key variables:

- House prices (level): `avg_house_price_gbp`
- Mortgage stock (level, Â£m): `mb_total_gbp_m`
- Turnover (market depth): `turnover_pct_q` (transactions scaled by dwelling stock)
- Optional composition proxy: `newbuild_share_of_transactions`
- Time index: `period` (quarter), and `geo` for region selection (e.g., EW)

### Derived series

Define year-on-year (YoY) growth rates:

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

## Baseline Normalisation (Core Proviso)

To avoid defining â€œnormalâ€ using crisis regimes and structural breaks, z-scores are computed from pooled baseline windows:

- 2003Q1â€“2007Q4
- 2013Q1â€“2019Q4

Exclusions:

- 2008â€“2012 (Global Financial Crisis and aftermath)
- 2020+ (Covid and subsequent regime breaks)

For any series \\X_t\\, define:

<div class="eq">

\$\$ z(X_t) = \frac{X_t - \mu_X}{\sigma_X} \$\$

</div>

where \$\$\mu_X\$\$ and \$\$\sigma_X\$\$ are computed using baseline quarters only.

</div>

<div class="section">

## The Home@ix DoughForge Indicator

### DoughForge definition

Default (three-component) specification:

<div class="eq">

\$\$ DoughForge_t = 100 \cdot \Big( 0.55 \cdot z(W_t) - 0.35 \cdot z(g_t^{TO}) + 0.10 \cdot z(\Delta NB_t) \Big) \$\$

</div>

If the new-build term is not available, the final term is omitted:

<div class="eq">

\$\$ DoughForge_t = 100 \cdot \Big( 0.55 \cdot z(W_t) - 0.35 \cdot z(g_t^{TO}) \Big) \$\$

</div>

### Direction-of-flow

Define the direction-of-flow statistic:

<div class="eq">

\$\$ \Delta DoughForge_t = DoughForge_t - DoughForge\_{t-1} \$\$

</div>

This is used for monitoring whether affordability pressure is accelerating or easing.

### Interpretation bands (practical)

A simple interpretive scheme:

- \$\$DoughForge \ge 50\$\$: strong deterioration regime risk
- \$\$20 \le DoughForge \< 50\$\$: mild deterioration bias
- \$\$-20 \le DoughForge \< 20\$\$: neutral/noisy
- \$\$-50 \le DoughForge \< -20\$\$: mild improvement bias
- \$\$DoughForge \< -50\$\$: strong improvement regime (often stress-driven)

</div>

<div class="section">

## Using DoughForge for Forward-Looking Evaluation (Event Backtesting)

DoughForge can be evaluated using objective events and simple warning rules.

### Crash-start events (rule-based)

A â€œcrash startâ€ may be defined as a local price peak followed by a drawdown of at least \$\$X\\\$\$ within \$\$Y\$\$ quarters, with a minimum separation (cooldown) of \$\$C\$\$ quarters to avoid double-counting clustered peaks.

### Illustrative warning rules

Examples:

- A: sustained level stress: \$\$DoughForge \> 20\$\$ for 2 quarters
- B: sustained acceleration: \$\$\Delta DoughForge \> 5\$\$ for 2 quarters
- C: broad stress-worsening: \$\$DoughForge \> 0\$\$ and \$\$\Delta DoughForge \ge 0\$\$

### Metrics

- Lead time (quarters) from the most recent signal to each crash start.
- False-positive proxy: share of signal quarters not followed by any crash start within a forward window (e.g., 8 quarters).

</div>

<div class="section">

## Outputs and Visualisations (Reproducible)

The DoughForge build produces:

- a DoughForge level figure (headline chart),
- a component contributions figure (mechanism chart),
- an animated direction-of-flow GIF emphasising \$\$\Delta DoughForge_t\$\$,
- and a tidy CSV export of intermediate series for auditability.

### Figure placeholders

Replace the filenames with the paths to the generated assets.

<figure>
<img src="assets/DoughForge_assets/fig_DoughForge_level.png" style="max-width:100%; height:auto;" alt="Home@ix DoughForge (EW): Level" />
<figcaption><strong>Figure 1.</strong> Home@ix DoughForge (EW): Level. Baseline windows: 2003Q1â€“2007Q4 and 2013Q1â€“2019Q4; excludes 2008â€“2012 and 2020+.</figcaption>
</figure>

<figure>
<img src="assets/DoughForge_assets/fig_DoughForge_contributions.png" style="max-width:100%; height:auto;" alt="Home@ix DoughForge (EW): Component contributions" />
<figcaption><strong>Figure 2.</strong> Home@ix DoughForge (EW): Component contributions. DoughForge is the sum of wedge, turnover, and optional new-build terms.</figcaption>
</figure>

</div>

<div class="section">

## Limitations and Extensions

DoughForge is a reduced-form indicator derived from aggregate market series. It does not directly encode distributional constraints (income heterogeneity, cash-buyer share, arrears microdata) or direct developer pacing series (e.g., sales per outlet per week) unless explicitly added. These are natural extensions; the baseline DoughForge specification is intentionally reproducible and captures two dominant UK mechanisms: creditâ€“price decoupling and thin-market clearing.

</div>

<div class="section">

## Conclusion

UK housing affordability is not only a price level problem; it is also an allocation and throughput problem. Home@ix DoughForge provides a transparent, reproducible way to detect when the system is shifting into a regime where affordability is likely to deteriorate over a 2â€“3 year horizon via creditâ€“price decoupling and/or collapsing market depth. Combined with direction-of-flow and event backtesting, DoughForge is positioned as an operational forward-looking tool: a single â€œNumberâ€ grounded in auditable data and interpretable mechanisms.

</div>

<div class="section">

## Reproducibility Note

The figures referenced in Section 8 are produced by the DoughForge build scripts in the Home@ix workflow. The output directory should contain:

- `DoughForge_quarterly_audit.csv`
- `fig_DoughForge_level.png`
- `fig_DoughForge_contributions.png`
- `anim_DoughForge_direction_of_flow.gif`

</div>

</div>

------------------------------------------------------------------------








