# breakeven.md  

## 1. Unit Economics (per **active** user, per month)

| Cost Component | Assumptions | Monthly Cost (USD) |
|----------------|-------------|--------------------|
| **Compute** (GPU‑accelerated inference for code generation & verification) | 0.5 GPU‑hour @ $0.10 per GPU‑hour (spot) | **$0.05** |
| **Storage** (persistent user snippets, test suites, verification logs) | 5 GB @ $0.002/GB | **$0.01** |
| **Bandwidth** (API calls, test data upload/download) | 2 GB outbound @ $0.01/GB | **$0.02** |
| **Total Variable Cost / user** | – | **$0.08** |

> *Variable cost is the marginal expense of supporting one additional active user. Fixed overhead (team salaries, CI/CD, monitoring, office, etc.) is accounted for separately.*

---

## 2. Pricing Tiers  

| Tier | Monthly Price (USD) | Core Features | Target Segment |
|------|---------------------|----------------|----------------|
| **Starter** | **$15** | • 5 k LOC generation per month  <br>• 10 automated test suites <br>• Basic verification (syntax + unit‑test pass) <br>• Community support | Solo developers, hobbyists |
| **Professional** | **$45** | • 25 k LOC generation <br>• Unlimited test suites <br>• Deep verification (type‑checking, static analysis, security lint) <br>• Priority queue (lower latency) <br>• Email support | Small teams / startups |
| **Enterprise** | **$120** | • 100 k LOC generation <br>• Custom verification policies (regulatory, internal standards) <br>• Dedicated GPU pool (fastest response) <br>• SSO & audit logs <br>• 24/7 phone & Slack support <br>• SLA 99.9% uptime | Mid‑size & large engineering orgs |

*All tiers include the $0.08 variable cost per active user automatically; it is sub‑tracted when calculating contribution margin.*

---

## 3. Customer Acquisition Cost (CAC)

| Source | Estimated CAC (USD) |
|--------|---------------------|
| Paid developer‑focused ads (e.g., StackOverflow, GitHub Sponsors) | $250 |
| Content & SEO (white‑papers, webinars) | $180 |
| Partnerships / marketplace listings | $320 |
| **Range (overall)** | **$180 – $320** |

*We assume a blended CAC of **$250** for the breakeven model.*

---

## 4. Lifetime Value (LTV)

*Assumptions*  

- **Monthly churn** = 5 % (average across tiers) → average customer lifespan = 1 / 0.05 = **20 months**  
- **Weighted ARPU** (average revenue per user) =  
  \[
  \frac{(0.6 \times 15) + (0.3 \times 45) + (0.1 \times 120)}{1} = \$30
  \]  
  (60 % Starter, 30 % Professional, 10 % Enterprise – realistic early‑stage mix)  

- **Variable cost per user** = $0.08  

**Contribution margin per user** = ARPU – Variable Cost = $30 – $0.08 ≈ **$29.92**  

**LTV** = Contribution margin × Lifespan  
\[
LTV = 29.92 \times 20 \approx \mathbf{\$598}
\]

Rounded to **$600** for planning.

---

## 5. Break‑Even Users (to cover **fixed monthly overhead**)

| Fixed Monthly Overhead (USD) |  $20,000* |
|------------------------------|-----------|
| Net contribution per user (average) | $29.92 |
| **Break‑Even Users** = Fixed / Net per user | **≈ 670 users** |

\*Includes salaries (founders, devs, QA, ops), office, tooling licences, and a modest marketing budget.

---

## 6. Path to **$10 K MRR**

We target a mix that mirrors the weighted ARPU above (60 % Starter, 30 % Professional, 10 % Enterprise).

| Tier | Required Users | Monthly Revenue |
|------|----------------|-----------------|
| Starter ($15) | **400** | $6,000 |
| Professional ($45) | **80** | $3,600 |
| Enterprise ($120) | **4** | $480 |
| **Total** | **484** | **$10,080** |

*Alternative single‑tier routes (for quick pilots):*  

- **All Professional:** 10 k / $45 ≈ **223** users  
- **All Enterprise:** 10 k / $120 ≈ **84** users  

The mixed‑tier approach is more realistic for early adoption because it captures both hobbyists and small teams while still delivering a modest enterprise foothold.

---

## 7. Summary of Key Numbers  

| Metric | Value |
|--------|-------|
| Variable cost / active user | **$0.08 / mo** |
| Pricing tiers | $15 / $45 / $120 |
| CAC (blended) | **$250** |
| LTV (net contribution) | **≈ $600** |
| Fixed monthly overhead | **$20 k** |
| Break‑even active users | **≈ 670** |
| Users needed for $10 k MRR | **≈ 484** (mixed tier) |

These figures give a concrete financial runway for **code‑verifier** and define the growth milestones the go‑to‑market team should hit to move from launch to sustainable profitability.