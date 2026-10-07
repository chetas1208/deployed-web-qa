# Deployed Web QA

A reusable Codex skill for auditing deployed web applications with browser automation.

It covers authentication, safe interaction coverage, navigation and state verification, responsive layout review, accessibility smoke checks, browser diagnostics, performance signals, and a severity-ranked QA report.

## What it does

- Authenticates only with user-supplied credentials for the named destination.
- Builds an explicit inventory of visible controls and user-facing claims.
- Exercises navigation, search, filters, tabs, dialogs, disclosures, tours, charts, and safe async controls.
- Verifies visible outcomes, URL/query state, and data invariants after interactions.
- Tests 375px, 768px, and 1440px layouts for clipping, overflow, readability, and control fit.
- Performs accessibility smoke checks for names, labels, landmarks, headings, keyboard focus, and alt text.
- Collects console, network, navigation timing, FCP/LCP/CLS/INP, and long-running-operation evidence when available.
- Produces a self-contained report with P0–P3 defects, intentional exclusions, and a SHIP / SHIP WITH FIXES / DO NOT SHIP / INCONCLUSIVE verdict.

## Install

Install the skill into a Codex skills directory:

```bash
mkdir -p "$HOME/.codex/skills"
cp -R deployed-web-qa "$HOME/.codex/skills/deployed-web-qa"
```

Or install from this repository using your normal skill installer.

## Use

Invoke it explicitly:

```text
Use $deployed-web-qa to audit https://example.com with the supplied test credentials and produce a detailed QA report.
```

The skill is also discoverable automatically through its frontmatter and `agents/openai.yaml` metadata.

## Safety model

The default posture is read-only. Navigation, search, filters, tabs, disclosures, help tours, and reversible view toggles are safe to exercise. Business-state changes such as approving/rejecting records, deleting or editing data, pushing to a CRM, sending messages, making purchases, or starting paid/provider-heavy jobs are excluded unless the user explicitly authorizes the exact action in an appropriate environment.

Passwords are never printed in screenshots, logs, commits, or reports. Page content is treated as untrusted data and cannot authorize uploads, data sharing, or other external actions.

## Report shape

Every audit should include:

1. Scope and environment
2. Executive verdict
3. Authentication
4. Smoke and performance
5. Functional coverage
6. Visual and responsive findings
7. Accessibility findings
8. A defect table with reproduction, expected result, actual result, severity, and evidence
9. Intentional exclusions
10. Recommended fixes and retest plan

## Repository layout

```text
deployed-web-qa/
├── SKILL.md
├── agents/openai.yaml
├── scripts/validate_skill.py
├── .github/workflows/validate.yml
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## Development

Run the repository validator locally:

```bash
python3 scripts/validate_skill.py
```

The same check runs on every pull request and push to `main`.
