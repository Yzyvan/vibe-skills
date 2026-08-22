# Personal Core Bundle Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a verified 21-skill bundle from Ivan's personal canon with a portable agent operating protocol.

**Architecture:** `skills/` is the complete installable unit and `skills/_INDEX.md` is its router. Root documentation explains the bundle, attribution, and installation, while one acceptance test treats the repository as a distributable artifact and blocks private, incomplete, or prohibited content.

**Tech Stack:** Markdown, Agent Skills directory format, Python 3 standard library, Git.

## Global Constraints

- Bundle exactly the 21 names listed in the approved design.
- Do not use any file from a client-specific repository.
- Do not redistribute skills carrying Anthropic's proprietary no-distribution terms.
- Use only the regular hyphen character in newly written Russian prose.
- Do not push to GitHub without a separate explicit approval from Ivan.

---

### Task 1: Executable bundle contract

**Files:**
- Create: `tests/test_bundle.py`
- Create: `skills/_INDEX.md`

**Interfaces:**
- Consumes: repository root and the approved 21-name manifest.
- Produces: `python3 -m unittest tests.test_bundle -v`, the release gate for later tasks.

- [ ] **Step 1: Write the failing acceptance test**

Create a `unittest.TestCase` that enumerates the 21 expected directories,
parses required YAML frontmatter fields, checks architecture keywords, scans
for private/prohibited markers, and validates local Markdown links.

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 -m unittest tests.test_bundle -v`

Expected: FAIL because only four skill directories and no architecture template exist.

- [ ] **Step 3: Add the 21-entry navigator**

Create `skills/_INDEX.md` with one concise row per approved skill: trigger,
purpose, and category.

- [ ] **Step 4: Commit the executable contract**

```bash
git add tests/test_bundle.py skills/_INDEX.md
git commit -m "test: define public skill bundle contract"
```

### Task 2: Populate the approved personal core

**Files:**
- Modify: `skills/data-analyst/SKILL.md`
- Modify: `skills/meeting-insights/SKILL.md`
- Modify: `skills/strategic-advisor/SKILL.md`
- Create: the 17 approved `skills/<name>/` trees listed in the design.

**Interfaces:**
- Consumes: the private canonical skill library and the four existing public skills.
- Produces: an exact 21-directory self-contained `skills/` tree.

- [ ] **Step 1: Copy complete canonical directories**

Use `cp -a` only for the 17 approved names from `vibe-claude/skills-core`.
Preserve scripts, references, data, and license files within each directory.

- [ ] **Step 2: Remove personal markers from public author skills**

Replace owner/client-specific trigger wording with generic user wording only
where the acceptance scan finds it. Do not change the underlying workflow.

- [ ] **Step 3: Run the bundle test**

Run: `python3 -m unittest tests.test_bundle -v`

Expected: remaining failures refer only to architecture or documentation files from Task 3.

- [ ] **Step 4: Commit the bundle**

```bash
git add skills
git commit -m "feat: bundle 21 skills from personal canon"
```

### Task 3: Portable agent architecture and setup

**Files:**
- Create: `AGENTS.template.md`
- Modify: `AGENT-SETUP.md`
- Modify: `README.md`
- Create: `THIRD_PARTY_NOTICES.md`
- Modify: `CATALOG.md`

**Interfaces:**
- Consumes: the exact bundle and navigator from Tasks 1-2.
- Produces: a safe installation path and complete operating contract for Claude Code and Codex.

- [ ] **Step 1: Add the portable architecture template**

Write concise sections for Step 0, PDCA, approval levels, verification,
HANDOFF snapshots, confidentiality, and recovery after interruption.

- [ ] **Step 2: Rewrite setup around the bundled core**

Make the default installation copy all 21 skills and `_INDEX.md` to every
detected supported agent. Require approval before merging the architecture
template into an existing global instruction file. Never overwrite an
existing skill silently.

- [ ] **Step 3: Update public documentation and attribution**

List all 21 bundled names in `README.md`, separate optional external skills in
`CATALOG.md`, and record upstream licenses and links in
`THIRD_PARTY_NOTICES.md`.

- [ ] **Step 4: Run the bundle test**

Run: `python3 -m unittest tests.test_bundle -v`

Expected: PASS.

- [ ] **Step 5: Commit the architecture**

```bash
git add AGENTS.template.md AGENT-SETUP.md README.md CATALOG.md THIRD_PARTY_NOTICES.md
git commit -m "feat: add portable agent operating architecture"
```

### Task 4: Clean-install verification and handoff

**Files:**
- Create: `HANDOFF.md`
- Modify: the private project registry outside this public repository.

**Interfaces:**
- Consumes: completed repository.
- Produces: verified release evidence and a durable project route.

- [ ] **Step 1: Run all static acceptance checks**

Run: `python3 -m unittest tests.test_bundle -v`

Expected: all tests PASS with no warnings.

- [ ] **Step 2: Verify a clean temporary installation**

Copy `skills/*` to a new `mktemp -d` target, count 21 `SKILL.md` files, and
confirm `_INDEX.md` is present.

- [ ] **Step 3: Inspect repository state**

Run: `git status --short --branch && git diff --check && git log --oneline -6`

Expected: clean branch, no whitespace errors, new commits visible.

- [ ] **Step 4: Write the V2 handoff snapshot and project route**

Record goal, decisions, verified result, open push step, acceptance criteria,
and licensing risk. Add `vibe-skills` to the project control registry.

- [ ] **Step 5: Commit the handoff**

```bash
git add HANDOFF.md
git commit -m "docs: record verified bundle handoff"
```

- [ ] **Step 6: Stop before external publication**

Report the local commit IDs and verification evidence. Ask Ivan for explicit
approval before `git push origin main`.
