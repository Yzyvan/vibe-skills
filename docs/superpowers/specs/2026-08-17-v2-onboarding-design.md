# V2 onboarding design

## Goal

Give a new Codex user one public link and one Markdown instruction that safely configures a laptop, installs the shared skills, applies the V2 operating rules, and verifies the result without overwriting existing configuration.

## Audience and scope

- The primary reader is a non-programmer using Codex on a personal Windows, macOS, or Linux laptop.
- The public repository stays generic and contains no private client, employee, server, or proprietary BPMN material.
- The package keeps the existing 21-skill manifest. V2 changes the operating architecture and onboarding, not the skill count.
- Access to private project repositories is a later, separate GitHub invitation. The public installer must not assume it exists.

## Architecture

The repository has three public layers:

1. `CODEX-SETUP-V2.md` is the single file a new user gives to Codex. It tells the agent to detect the operating system, inspect the current machine, install safely, configure the agent rules, check GitHub readiness, and produce evidence.
2. `AGENT-SETUP.md` contains the reusable installation procedure. Existing files are compared and preserved. No secrets, client data, access changes, or remote writes happen automatically.
3. `AGENTS.template.md` contains the V2 operating contract: skill-first routing, visible PDCA, one-request execution, deduplication, checkpoints, HANDOFF V2, confirmed lessons, data durability, and three initiative levels.

Automated tests treat these documents as a contract. A release is valid only when all required V2 concepts are present, private markers are absent, relative links resolve, and the existing 21-skill manifest is unchanged.

## Data and GitHub boundaries

- Durable work lives both in a local project folder and in a user-controlled private GitHub repository when appropriate.
- Push, publication, repository invitations, access changes, deletion, payments, and third-party messages always require explicit user approval.
- Secrets stay outside Git and are covered by `.gitignore`.
- Raw client or personal data is not placed in the public skills repository.
- Setup checks Git availability, identity, authentication, repository state, and two-factor authentication guidance. It does not create accounts or repositories without approval.

## Failure handling

- If Codex is missing, Git is missing, GitHub authentication is absent, or a destination file conflicts, stop only that step and report the exact action the user must take.
- Never overwrite an existing `AGENTS.md`, `CLAUDE.md`, or skill directory silently.
- Installation must be repeatable. A second run compares state and skips matching files instead of duplicating them.
- Verification reports installed skill count, `_INDEX.md`, V2 rule coverage, Git/GitHub readiness, local persistence, remote persistence, conflicts, and unverified items.

## Acceptance criteria

- One reusable Markdown file is sufficient to start setup on Windows, macOS, or Linux.
- The public repository still contains exactly 21 distributable skills.
- Tests fail if PDCA V2, deduplication, HANDOFF V2, checkpoint timing, data durability, or approval boundaries disappear.
- Setup never overwrites existing configuration or sends data externally without approval.
- README links directly to the V2 onboarding file.
- A clean test run and a fresh clone inspection provide release evidence.
