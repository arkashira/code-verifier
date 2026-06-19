# PRD – Code‑Verifier

**Product:** Code‑Verifier  
**Owner:** Senior Product/Engineering Lead  
**Target Release:** Q4 2026 (Beta)  
**Repo:** `arkashira/code-verifier`  

---  

## 1. Problem Statement  

Developers increasingly rely on AI code‑generation (e.g., Copilot, Claude, GPT‑4) to accelerate productivity. Existing tools prioritize speed and token‑efficiency, often delivering syntactically correct but semantically flawed snippets. The downstream cost—debugging, security reviews, and flaky tests—eats into the time‑savings and erodes trust.  

**Key pain points**

| Pain | Impact |
|------|--------|
| **Incorrect business logic** – generated code compiles but fails functional requirements. | Increases bug‑fix effort by 30‑50 %. |
| **Missing edge‑case handling** – AI skips null checks, overflow guards, etc. | Leads to production incidents, especially in safety‑critical domains. |
| **No automated verification** – developers must manually write tests after generation. | Slows iteration and reduces adoption of AI assistance. |
| **Security/Compliance gaps** – generated code may contain unsafe patterns (e.g., SQL injection). | Increases audit workload and legal risk. |

The market lacks a **high‑accuracy AI code‑generation engine that couples generation with automated verification** (unit tests, static analysis, security linting) to guarantee correctness before the snippet is presented to the developer.

---

## 2. Target Users  

| Persona | Description | Primary Value |
|---------|-------------|---------------|
| **Full‑stack Engineer** | Writes feature code daily, uses AI for boilerplate and scaffolding. | Faster, trustworthy snippets; fewer post‑generation fixes. |
| **DevOps / SRE** | Automates infrastructure as code (IaC) and scripts. | Guarantees generated scripts pass lint & security checks. |
| **Security Engineer** | Reviews code for vulnerabilities. | Early detection of unsafe patterns via built‑in analysis. |
| **Product Manager (technical)** | Needs rapid prototyping without sacrificing reliability. | Confidence that prototypes are functionally correct. |

---

## 3. Goals & Success Metrics  

| Goal | Metric | Target (by Q4 2026) |
|------|--------|---------------------|
| **Correctness‑first generation** | % of generated snippets that pass automated verification on first try | ≥ 85 % |
| **Developer productivity** | Avg. time from prompt to verified snippet | ≤ 45 seconds |
| **Adoption** | Active daily users (DAU) on beta | ≥ 1,500 |
| **Safety** | Critical security findings per 10k generated snippets | ≤ 1 |
| **Revenue validation** | Paying pilot conversions (out of 100 beta orgs) | ≥ 20 % |

---

## 4. Key Features (Prioritized)

| Priority | Feature | Description | Acceptance Criteria |
|----------|---------|-------------|----------------------|
| **P1** | **Prompt‑to‑Verified Code Pipeline** | End‑to‑end flow: user prompt → LLM generation → automated unit test synthesis → static analysis → security lint → result returned only if all checks pass. | - 100 % of returned snippets have passed all checks.<br>- Pipeline latency ≤ 45 s for typical prompts (≤ 200 tokens). |
| **P1** | **Test‑First Generation Mode** | Generates unit tests *before* code, then uses them as constraints for the LLM (guided generation). | - Generated tests compile and cover ≥ 80 % of generated code lines.<br>- Failure rate of generated code vs its own tests ≤ 5 %. |
| **P2** | **Pluggable Verification Stack** | Modular adapters for: <br>• `pytest` (Python) <br>• `jest` (JS/TS) <br>• `golangci-lint` (Go) <br>• `bandit` (Python security) <br>• Custom org‑specific linters. | - At least three language stacks supported out‑of‑the‑box.<br>- Org can add a new verifier via a simple JSON config. |
| **P2** | **Confidence Scoring UI** | UI badge showing “Verification Score” (0‑100) derived from test pass rate, static analysis warnings, and security findings. | - Score updates in real‑time as verification runs.<br>- Score ≥ 90 displayed as “High Confidence”. |
| **P3** | **Rollback / Suggest‑Edit Loop** | If verification fails, the system automatically suggests minimal edits (e.g., add null check) and re‑runs verification. | - 80 % of failing cases resolved automatically without user edit. |
| **P3** | **Telemetry & Explainability Dashboard** | Shows per‑prompt metrics: generation time, verification steps, failures, and root‑cause hints. | - Dashboard accessible to org admins; data retention 30 days. |
| **P4** | **IDE Plug‑ins** | VSCode & JetBrains extensions that invoke Code‑Verifier inline. | - Extension installable via marketplace; basic functionality matches web UI. |

---

## 5. Scope  

### In‑Scope
- Core generation pipeline using the **vLLM** inference engine (already verified in repo).
- Automated test synthesis leveraging the **SGLang** structured generation framework.
- Integration of open‑source static analysis tools (e.g., `pylint`, `eslint`, `golangci-lint`).
- Security linting via **Bandit** (Python) and **Semgrep** (multi‑lang) as first‑class verifiers.
- Web UI for prompt entry, result display, confidence score, and edit loop.
- Telemetry collection stored in the company BRAIN (pgvector) for continuous improvement.

### Out‑of‑Scope (Phase 1)
- Full‑language coverage beyond Python, JavaScript/TypeScript, and Go.
- Enterprise SSO / RBAC integration (will be added in Phase 2).
- Offline/edge deployment (requires separate model serving infra).
- Custom model fine‑tuning (use existing base models via vLLM).

---

## 6. Assumptions & Dependencies  

| Assumption | Rationale |
|------------|-----------|
| Access to high‑throughput GPU nodes for vLLM inference (already provisioned in Axentx infra). | Needed to meet latency targets. |
| Existing datasets (`auto`, `messages`, `instr‑resp`) contain sufficient code‑related pairs for fine‑tuning test‑generation prompts. | Leverages current data assets. |
| Security teams approve use of Bandit & Semgrep in production. | Aligns with compliance. |
| Users will accept a slight latency increase (≈ 30 s) for higher correctness. | Trade‑off validated by market research. |

---

## 7. Risks & Mitigations  

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Verification bottleneck** – static analysis may dominate latency. | Missed SLA. | Parallelize verifiers; cache results for identical snippets; early exit on critical failures. |
| **False‑positive security findings** – could frustrate users. | Adoption drop. | Tune rule sets; allow “suppress” flag with justification logged. |
| **Model hallucination despite verification** – tests may be too weak. | Undetected bugs. | Use test‑first mode; enforce coverage thresholds; add mutation testing in future. |
| **Data privacy** – prompts may contain proprietary code. | Legal risk. | Run inference in isolated VPC; do not log raw prompts, only hashed metadata. |
| **Scope creep** – adding many languages early. | Delayed launch. | Strictly enforce Phase 1 language list; defer others to roadmap. |

---

## 8. Milestones  

| Milestone | Date | Deliverable |
|-----------|------|-------------|
| **M1 – Foundations** | 2026‑07‑15 | vLLM integration, basic prompt UI, generation endpoint. |
| **M2 – Verification Stack** | 2026‑08‑20 | Test synthesis, static analysis, security lint pipelines for Python & JS. |
| **M3 – Confidence Scoring & Edit Loop** | 2026‑09‑10 | UI badge, automatic fix suggestions, rollback logic. |
| **M4 – Beta Release** | 2026‑10‑01 | Public beta (invite‑only), telemetry dashboard, 3 language support. |
| **M5 – Feedback & Iteration** | 2026‑11‑15 | Incorporate beta feedback, improve latency, add Go verifier. |
| **M6 – GA Launch** | 2026‑12‑15 | Full product release, documentation, pricing page. |

---

## 9. Open Questions  

1. **Pricing model:** per‑generated‑snippet vs. subscription tier? (To be decided by BD after validation.)  
2. **Org‑level custom rule ingestion:** format and UI for security teams? (Design sprint Q4 2026.)  
3. **Evaluation dataset for correctness:** need a benchmark suite to track the 85 % target.  

---  

*Prepared by the Code‑Verifier product team, aligned with Axentx’s revenue‑validated product development flow.*
