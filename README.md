# Castela

> **Disposition: archive.** Castela is a preserved, read-only 2024 prototype. The 2026-09-07 audit found no live owner, endpoint, infrastructure, consumer, or distribution channel. Do not run or deploy it.

Castela explored a Flask form that fetched an arbitrary web page and summarized its text with `facebook/bart-large-cnn`. It was committed once with part of a machine-specific Python virtual environment and never acquired a portable build, test, release, or deployment contract.

See [OWNERSHIP.md](OWNERSHIP.md) for the evidence, security concerns, residual unknowns, and recovery conditions.

## Current contract

- **Product owner:** none; historical source is held by the Gaulatti organization.
- **Delivery target:** none.
- **Release/deploy command:** none. The historical setup launcher now fails closed.
- **Health proof:** none; the expected Gaulatti and Fifthbell hostnames do not resolve and no matching live surface was found.
- **Recovery:** preserve Git history. Any revival starts with a repository-owned proposal that names an owner and delivery target, removes the committed virtual environment, addresses server-side request forgery and workload bounds, adds tests, and establishes release/rollback proof.

GitHub archival is intentionally deferred until this notice is merged to `main`.
