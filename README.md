# Castela

> **Disposition: archive candidate.** Castela is a preserved, read-only 2024 prototype. Do not run or deploy it. Its dated external audit notes lack retained command outputs; current external ownership, endpoints, infrastructure, consumers, and distribution remain unverified.

Castela explored a Flask form that fetched an arbitrary web page and summarized its text with `facebook/bart-large-cnn`. It was committed once with part of a machine-specific Python virtual environment and never acquired a portable build, test, release, or deployment contract.

See [OWNERSHIP.md](OWNERSHIP.md) for the dated notes, evidence limits, security concerns, and recovery conditions.

## Current contract

- **Product owner:** none; historical source is held by the Gaulatti organization.
- **Delivery target:** none.
- **Release/deploy command:** none. The historical setup launcher now fails closed.
- **Health proof:** none; the historical DNS and live-surface claims have not been independently reverified.
- **Recovery:** preserve Git history. Any revival starts with a repository-owned proposal that names an owner and delivery target, removes the committed virtual environment, addresses server-side request forgery and workload bounds, adds tests, and establishes release/rollback proof.

GitHub archival is intentionally deferred until this notice is merged to `main`.
