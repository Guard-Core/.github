# Governance

The Guard Core organization holds the Guard Core engines, their framework adapters, the Guard Agent telemetry agents, the MCP server and the public tracker of the hosted app. I maintain all of it alone; [MAINTAINERS.md](MAINTAINERS.md) lists who I am and how to check it. Each repository has its own GOVERNANCE.md with the same rules.

## Decisions

I make the final call on every change: features, releases, security fixes and repository access. A proposal starts as an issue, so the reasoning is public before any code is written.

## How a change lands

1. Every change to a library is a pull request to its default branch.
2. The branch rulesets require signed commits, linear history, passing status checks and two approvals, one of them from a code owner. As the only maintainer I cannot get those approvals, so I merge my own pull requests with admin rights. That skips the approval count only: I never merge with a failing check.
3. A pull request closes an open issue (`Closes #N`), or carries the `no-issue` label when it is a small fix with nothing to discuss.

## Releases

Versions follow semantic versioning. The engines (Python, TypeScript, Rust, Go, PHP, JVM) share one version number and release together; the agents share another; adapters version on their own, because each one follows its framework. Releases are cut from tags and recorded in each CHANGELOG.md.

## Security

Vulnerabilities go through [SECURITY.md](SECURITY.md), never through public issues.

## New maintainers

Contributors with a record of reviewed and merged work can be invited as maintainers. A new maintainer is added to MAINTAINERS.md and CODEOWNERS in a pull request.

## Conduct

The [Code of Conduct](CODE_OF_CONDUCT.md) applies to every space of the organization.
