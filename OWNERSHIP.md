# Castela ownership and disposition audit

Historical audit notes dated: 2026-09-07

Default branch and audited commit: `main` at `a843cfe21a8e85afe9b9fb31ee6431c6c67a7bf9`

## Decision

**Disposition: archive after this audit lands on the default branch.**

This disposition retires the preserved prototype and disables its launcher.
Source and history remain available as recovery material; the GitHub archive
control is a separate post-merge step so this notice is reviewable first.
No supported product owner or delivery target is declared by this repository.
That does not establish that external deployments or consumers are absent.

## Historical audit notes and evidence limits

The table preserves the observations recorded on 2026-09-07. The underlying
GitHub, portfolio-search, DNS, AWS, and registry command outputs were not
retained with this PR. Those external observations are unverified historical
claims, not proof of current absence or of account-wide coverage. The
2026-10-19 review checked source and the fail-closed launcher locally; it did
not repeat the external audit or start the application. Archival must wait for
the final control-plane refresh described below.

| Surface | Recorded method | Recorded result (external claims unverified) |
| --- | --- | --- |
| Git source | GitHub metadata, branch, commit, tag, and tree APIs | Public, unarchived repository with one unprotected `main` branch, one commit dated 2024-08-15, no tags, no description, and no homepage. |
| Source contract | Inspected every default-branch source path | A Flask page accepts a URL, fetches it, and passes the page text to `facebook/bart-large-cnn`. There is no README, package metadata, container definition, production server, or deployment configuration. |
| Portability | Inspected tracked modes, symlinks, and script shebangs | Part of a virtual environment is committed under `castela/`; its Python symlink and generated scripts point to paths that do not exist in a fresh checkout. |
| Actions and schedules | GitHub Actions workflow and run APIs | No workflow and no run exists. |
| Releases and deployments | GitHub releases, deployments, and environments APIs | No release, deployment, or environment exists. |
| Pages and webhooks | GitHub Pages and hooks APIs | No Pages site and no webhook exists. |
| Repository credentials | GitHub Actions secret and variable APIs | No Actions secret or variable name exists. No credential value was requested or read. |
| Rules and security | Branch-protection and vulnerability-alert APIs | `main` is unprotected and vulnerability alerts are disabled. |
| Portfolio consumers | Exact local searches under `/Users/gaulatti/source` and authenticated GitHub code searches across Gaulatti and Fifthbell | No import, package reference, documentation reference, domain, image, or infrastructure identifier was found. |
| DNS and HTTP | DNS and HTTPS checks for `castela.gaulatti.com` and `castela.fifthbell.com` | Neither hostname resolves, so there is no HTTP surface at either expected portfolio domain. |
| AWS infrastructure | Read-only CloudFormation search across all enabled regions plus default-region Lambda, API Gateway, ECR, and S3 inventories; global CloudFront and Route53 checks | No matching stack, runtime resource, bucket, repository, distribution alias, or DNS record was found in the configured account. |
| Registries | PyPI JSON API and GitHub repository release inventory | PyPI has no `castela` project and GitHub has no release. The current token cannot enumerate account-wide GitHub Packages, so that account-level boundary remains unverified. |
| Runtime safety | Static review of `app.py` | The server fetches an arbitrary user-supplied URL without scheme/host restrictions, timeout, response-size bounds, or network egress controls, then sends unbounded text to a large local model. It must not be exposed as a service without SSRF and resource-exhaustion controls. |

## Before and after

Before this audit, the repository had no README or ownership contract and its executable `Makefile` shell script created an environment, installed large dependencies, and started the development server.

After this audit:

- the README records the archive disposition and recovery conditions;
- `OWNERSHIP.md` preserves the dated notes and explicitly identifies missing evidence;
- the old launcher exits nonzero before installation, model download, or server startup;
- a standard-library test guards the disposition and disabled launcher;
- application source, committed environment artifacts, and Git history remain unchanged.

## Validation

| Check | Result |
| --- | --- |
| `bash -n Makefile` | Passed. |
| `python3` AST parsing of `app.py` | Passed in the 2026-10-19 review without importing the application; no application source changed. |
| `python3 -m unittest discover -v` | Passes the archive-contract tests added by this audit. The original repository had no tests. |
| `./Makefile` | Exits nonzero before any environment, network, package, model, or server action. |

## Residual unknowns

- The historical notes describe only a configured AWS account; no retained output establishes even that scope. Current cloud ownership and deployments are unknown. Another account or unnamed host could contain a copy.
- The historical notes report insufficient account-wide package-read scope. Current package ownership and the current token's scope were not checked.
- No inventory for external model registries, private servers, or developer workstations was available.

These unknowns establish neither current ownership nor its absence. The
post-merge archive follow-up requires a fresh control-plane inventory with
retained evidence and must stop if live ownership or a recovery dependency
appears. Merging these source changes does not archive the repository.

## Recovery contract

Recovery begins from Git history on a new branch. A named owner must define the intended users, data handling, model license/provenance, egress policy, bounded fetch and inference behavior, deploy target, secret ownership, health proof, and rollback. The committed virtual environment must be removed in a separately reviewed change and dependencies must be rebuilt from a supported Python version with reproducible checksums.

There is no production rollback for archival because no production surface was verified. If ownership evidence later appears, unarchive the repository and revert the audit commit before beginning recovery work.
