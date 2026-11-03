# Team Skill Builder (v0.1)

A portable meta-skill for creating, reviewing and maintaining reusable AI agent skills across a team.

## Use cases
- Create a new skill from a repeated workflow.
- Review an existing skill for clarity, security, maintainability and portability.
- Decide whether a request should be a skill, script, reference or MCP integration.
- Prepare evidence and evaluations for team review.

## Layout
- `SKILL.md` — instructions for the agent
- `references/` — design, portability and review guidance
- `templates/` — starter template
- `evaluations/` — example evaluation scenarios
- `scripts/validate_skill.py` — Python standard-library structural validator

## Run validation
```bash
python skills/team-skill-builder/scripts/validate_skill.py skills/team-skill-builder
```

For another skill:
```bash
python skills/team-skill-builder/scripts/validate_skill.py path/to/skill
```

The script checks basic structure only. It does not run agent evaluations or guarantee compatibility with every runtime.

## Codex / Claude Code
Copy or link this skill directory into the skills location recognized by your agent (commonly `.agents/skills/` for Codex and `.claude/skills/` for Claude Code). Keep the directory structure intact. Test discovery and invocation in each environment.

## Status
Initial team draft. Review the conventions and adapt the evaluation scenarios before broad adoption.
