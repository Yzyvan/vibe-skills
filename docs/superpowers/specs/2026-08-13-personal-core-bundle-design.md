# Personal Core Bundle Design

## Goal

Turn `vibe-skills` into a self-contained public starter kit built from Ivan's
saved personal canon: 21 distributable skills plus a compact agent operating
protocol for Claude Code and Codex.

## Bundle boundary

The repository contains exactly these 21 skills:

1. `slide-craft`
2. `data-analyst`
3. `meeting-insights`
4. `strategic-advisor`
5. `using-superpowers`
6. `brainstorming`
7. `verification-before-completion`
8. `content-engine`
9. `brand-voice`
10. `agent-harness-construction`
11. `loop-design-check`
12. `safety-guard`
13. `grilling`
14. `handoff`
15. `teach`
16. `wizard`
17. `to-questionnaire`
18. `impeccable`
19. `ui-ux-pro-max`
20. `emil-design-eng`
21. `review-animations`

The first four are already in this repository. The remaining 17 are copied
from Ivan's canonical `vibe-claude/skills-core` tree, preserving each complete
skill directory. No files from `agent-sveta` or other client repositories are
used.

Skills whose licenses prohibit redistribution, including the saved Anthropic
office-file skills, are not copied. The catalog may continue to point to their
official installation source.

## Agent architecture

The kit adds a portable `AGENTS.template.md` and updates `AGENT-SETUP.md`.
Together they establish:

- Step 0: inspect `skills/_INDEX.md`, name selected skills, read them fully;
- PDCA: state goal and acceptance criteria, perform the smallest safe action,
  verify, then report the remaining risk and next step;
- initiative levels: reversible local work is allowed, external or destructive
  actions require explicit approval;
- evidence before completion;
- a compact `HANDOFF.md` snapshot for meaningful multi-session work;
- protection of secrets, personal data, and existing user files.

The setup flow copies the 21 directories to the detected Claude Code and/or
Codex skill directory, installs the navigator, and asks before changing an
existing global instruction file.

## Documentation and attribution

`README.md` becomes the human-facing overview and lists the 21 bundled skills
by purpose. `THIRD_PARTY_NOTICES.md` records upstream authors, repositories,
and licenses. Existing catalog documents remain available as an optional
extended arsenal, clearly separated from the installed core.

## Verification

A standard-library Python acceptance test verifies:

- exactly 21 direct child skill directories;
- every skill has a readable `SKILL.md` with `name` and `description`;
- all expected names are present and no unexpected name appears;
- required architecture files and Step 0/PDCA/HANDOFF/approval language exist;
- no references to Ivan, Svetlana, private server paths, or client repositories;
- prohibited proprietary license text is absent;
- relative Markdown links inside the bundle resolve where applicable.

The final check also performs a clean-copy installation into a temporary
directory and reruns the manifest checks there.

## Acceptance criteria

- The repository passes the acceptance test from a clean checkout.
- The bundle contains exactly the agreed 21 skills.
- No Svetlana-specific or private material is present.
- No prohibited proprietary skill is redistributed.
- A new agent can install the kit and receive the complete operating protocol.
- Changes are committed locally. Pushing to GitHub remains a separate explicit
  owner action.
