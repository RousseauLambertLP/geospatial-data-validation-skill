# Portability notes

The shared core is a skill directory with a `SKILL.md` containing YAML frontmatter and Markdown instructions. Supported discovery locations and runtime capabilities differ by agent and installation.

- Keep the skill directory self-contained with relative paths.
- Avoid assuming access to shell, network, browser, GitHub or MCP servers.
- Document required and optional dependencies, and provide a fallback for missing capabilities.
- Put platform-specific integration instructions in separate files if needed.
- Validate skill discovery and behavior independently in Codex and Claude Code.
- Do not claim that identical SKILL.md files guarantee identical execution.
