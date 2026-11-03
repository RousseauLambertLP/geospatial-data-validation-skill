# Skill design guidelines

## Before writing
- Define one repeatable agent behavior and a clear trigger.
- Search for existing skills, scripts and tools that already solve the problem.
- Prefer a reference for static knowledge, a script for deterministic computation, and MCP for external actions.
- A skill orchestrates procedures and decision-making; it is not a substitute for an executable test suite.

## Writing
- Use concise, imperative steps with explicit inputs and outputs.
- Describe how to handle unavailable tools, ambiguous requests and partial results.
- Use progressive disclosure: short SKILL.md; details in references.
- Keep dependencies optional when possible; declare versions if required.
- Make outputs verifiable and include provenance/evidence requirements.
- Avoid duplicating large standards; link to authoritative references when appropriate.

## Evaluation
- Positive scenario: intended task.
- Negative scenario: request should not invoke the skill.
- Missing dependency scenario: graceful fallback.
- Risk scenario: secrets, write access or destructive operation.
- Record observed behavior and human reviewer feedback before approval.
