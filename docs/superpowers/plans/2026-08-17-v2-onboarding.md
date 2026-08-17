# V2 Onboarding Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a cross-platform Codex onboarding file and upgrade the shared agent operating contract to V2 without changing the 21-skill bundle.

**Architecture:** `CODEX-SETUP-V2.md` is the user-facing bootstrap instruction, `AGENT-SETUP.md` is the reusable installation procedure, and `AGENTS.template.md` is the operating contract installed into a workspace. Python contract tests verify required behavior and keep private material out of the public package.

**Tech Stack:** Markdown, Python `unittest`, Git.

## Global Constraints

- Keep exactly 21 distributable skills.
- Support Windows, macOS, and Linux laptops.
- Preserve existing configuration and never overwrite conflicts silently.
- Require explicit approval for push, publication, messages, access changes, deletion, and payments.
- Keep secrets and raw client data out of Git and out of the public repository.
- Do not include private BPMN logic, people, clients, VPS paths, or credentials.

---

### Task 1: Define the V2 contract in tests

**Files:**
- Modify: `tests/test_bundle.py`
- Test: `tests/test_bundle.py`

**Interfaces:**
- Consumes: public Markdown files in the repository root.
- Produces: contract assertions for V2 architecture and laptop onboarding.

- [ ] **Step 1: Write failing tests**

Add assertions requiring `CODEX-SETUP-V2.md`, cross-platform coverage, exact verification outputs, one-request execution, blocking-question batching, deduplication, 25/45-minute checkpoints, HANDOFF V2 limits, confirmed-lesson rules, local plus GitHub durability, and explicit approval boundaries.

- [ ] **Step 2: Verify RED**

Run: `python3 -m unittest tests.test_bundle -v`

Expected: failures because `CODEX-SETUP-V2.md` and the new V2 clauses do not exist.

- [ ] **Step 3: Keep the failure evidence**

Confirm failures name missing files or required phrases, not syntax errors in the test.

### Task 2: Implement the V2 operating contract

**Files:**
- Modify: `AGENTS.template.md`
- Modify: `AGENT-SETUP.md`
- Create: `CODEX-SETUP-V2.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: V2 requirements asserted by Task 1.
- Produces: one bootstrap file, one safe installer procedure, and one reusable agent contract.

- [ ] **Step 1: Expand `AGENTS.template.md`**

Add the single managed run, one approval, loop budget, 25/45-minute checkpoints, HANDOFF V2 snapshot, confirmed lesson deduplication, persistence, and restart behavior while keeping the existing skill-first, PDCA, and initiative-level rules.

- [ ] **Step 2: Expand `AGENT-SETUP.md`**

Add OS detection, dependency and GitHub readiness checks, conflict-safe installation, local and remote persistence checks, two-factor authentication guidance, and a fixed completion report.

- [ ] **Step 3: Create `CODEX-SETUP-V2.md`**

Write a self-contained instruction that a user can attach or paste into Codex. It must direct Codex to read the repository procedure, operate inside the laptop workspace, ask one batched question only for true blockers, and stop before external or destructive actions.

- [ ] **Step 4: Link onboarding from `README.md`**

Place the V2 onboarding link before manual commands so a non-programmer sees the recommended path first.

- [ ] **Step 5: Verify GREEN**

Run: `python3 -m unittest tests.test_bundle -v`

Expected: all tests pass.

### Task 3: Verify distribution and publish

**Files:**
- Modify: `HANDOFF.md`
- Modify: `JOURNAL.md`

**Interfaces:**
- Consumes: completed public package from Task 2.
- Produces: verified repository state, current V2 handoff, and a public GitHub revision.

- [ ] **Step 1: Run full checks**

Run `python3 -m unittest tests.test_bundle -v`, `git diff --check`, count direct `SKILL.md` files, scan distributable files for private markers, and inspect a clean archive or clone.

- [ ] **Step 2: Update state**

Move the previous handoff snapshot into `JOURNAL.md`, replace `HANDOFF.md` with a V2 snapshot under 120 lines and 12 KB, and include fresh verification evidence.

- [ ] **Step 3: Commit intentionally**

Stage only the onboarding, architecture, tests, README, plan, handoff, and journal changes. Commit with a concise V2 onboarding message.

- [ ] **Step 4: Publish**

Push the verified commit to `Yzyvan/vibe-skills` under the explicit publication authorization in the user request.

- [ ] **Step 5: Verify remote**

Read the public GitHub repository without authentication and confirm the onboarding file and commit are visible.

### Task 4: Deliver the onboarding package

**Files:**
- Read: `CODEX-SETUP-V2.md`

**Interfaces:**
- Consumes: the verified public file and GitHub URL.
- Produces: one allowed Telegram file delivery with a concise caption.

- [ ] **Step 1: Deliver through the approved queue**

Use `aegis-send-file` with the already allowed presentation-group alias, the local Markdown file, the public repository URL, and no private BPMN material.

- [ ] **Step 2: Verify delivery**

Wait for the queue result and record the job and message evidence.

- [ ] **Step 3: Report the remaining blocker**

Ask for the teammate's exact GitHub username before sending a private-repository invitation. Do not guess the account.
