# Validation policy

- Domain-neutral, format-neutral, read-only by default.
- Each check must identify its applicability, method, expected outcome, observed outcome, evidence and severity.
- Statuses: PASS (criterion met), WARN (non-blocking concern), FAIL (criterion violated), NOT_TESTED (insufficient access/evidence), NOT_APPLICABLE (irrelevant to dataset).
- No invented thresholds, data baselines or conformance claims.
- An approved dataset profile determines which failures block release. Unknown critical requirements imply NEEDS_REVIEW, not PASS.
- Reports are recommendations; an authorized human decides release.
