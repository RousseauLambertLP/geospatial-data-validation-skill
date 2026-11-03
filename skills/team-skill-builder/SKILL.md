---
name: team-skill-builder
description: Create, review, evaluate and maintain portable, reusable AI agent skills with consistent team conventions, deterministic checks and human review.
---

# Team Skill Builder

Use this skill when a teammate asks to create, improve, review or standardize an AI agent skill.

## Goals
- Produce focused, maintainable, vendor-neutral skills usable by Claude Code and Codex where supported.
- Reuse existing team knowledge and avoid duplicating skills, scripts or MCP tools.
- Keep secrets and organization-specific confidential information out of published skills.

## Workflow
1. **Discover**: inspect the repository and existing skills before creating a new one. Identify overlaps.
2. **Classify**: decide whether the request needs a skill (repeatable agent procedure), a reference document (knowledge), a script (deterministic operation), or an MCP tool (external capability). Explain the choice.
3. **Scope**: determine audience, trigger, inputs, outputs, exclusions, required tools, failure conditions and acceptance criteria. Ask only for essential missing information.
4. **Design**: create a short `SKILL.md` with valid YAML frontmatter (`name`, `description`) and imperative, testable instructions. Put long reference material in `references/` and optional executable checks in `scripts/`.
5. **Portability**: do not hardcode machine paths, vendor-specific features or tool names unless explicitly required. Document optional integrations and fallback behavior. Never assume MCP access.
6. **Safety**: minimize permissions; default to read-only actions; never embed credentials, tokens, personal data or proprietary material without authorization. Explicitly require confirmation for destructive or external writes.
7. **Evaluate**: add at least one positive scenario, one negative/out-of-scope scenario and one missing-tool scenario. Describe expected behavior, not just expected prose.
8. **Validate**: run `scripts/validate_skill.py` on the new skill when Python is available. Review `references/quality-checklist.md` manually. Fix failures.
9. **Deliver**: provide a summary of files, dependencies, evaluations run, limitations and unresolved decisions. If requested and authorized, prepare a branch or pull request; never claim it was created unless confirmed.

## Output structure
```text
skill-name/
  SKILL.md
  README.md                   # optional
  references/                 # only if needed
  scripts/                    # only if needed
  evaluations/
    scenarios.yaml
```

## Quality gates
- Frontmatter has a lowercase hyphenated name and meaningful description.
- Instructions define when to use the skill, workflow, limitations and failure behavior.
- Examples and evaluation cases are realistic and non-sensitive.
- Paths are relative; external dependencies and permissions are declared.
- Passing a syntax check does not prove the skill is effective. Human review remains mandatory.

## References
- `references/design-guidelines.md`
- `references/quality-checklist.md`
- `references/portability.md`
- `templates/SKILL.template.md`
- `evaluations/scenarios.yaml`
