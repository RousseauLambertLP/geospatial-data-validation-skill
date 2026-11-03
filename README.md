# Geospatial Data Validation Skill

A reusable AI skill for end-to-end validation of geospatial data, from source integrity and transformations to public distribution, ensuring data quality, consistency, interoperability, and compliance with applicable open standards.

## What it covers

- Source data structure, integrity, metadata and georeferencing
- Transformation correctness, including reprojection and resampling
- Public downloads and service output validation
- Independent source-to-delivery comparisons
- Evidence-backed validation reports and human approval

The skill is **format-neutral and domain-neutral**. Product-specific criteria and numerical tolerances belong in approved profiles.

## Contents

- [SKILL.md](SKILL.md): agent workflow and safety rules
- [references/policy.md](references/policy.md): validation policy and status definitions
- [references/checklist.md](references/checklist.md): generic validation checklist
- [references/report-template.md](references/report-template.md): reporting format
- [profiles/example-generic-dataset.yaml](profiles/example-generic-dataset.yaml): example profile (not approved for production)
- [scripts/check_raster.py](scripts/check_raster.py): read-only raster metadata inspection using GDAL Python bindings

## Usage with Codex and Claude Code

This repository keeps the portable `SKILL.md` and support files together. Install or link the skill directory into the skill discovery location used by your agent environment (for example, a Codex `.agents/skills/` directory or a Claude Code `.claude/skills/` directory). Keep the relative paths in this repository intact.

Ask the agent to validate a specific dataset and provide the authoritative source, published output, approved profile and intended transformations. If these are unavailable, the agent must report gaps rather than assert a release-ready result.

## Example raster inspection

Install the GDAL Python bindings for your environment, then run:

```bash
python scripts/check_raster.py /path/to/dataset.tif
```

This command inspects metadata only. It does **not** by itself establish dataset validity or end-to-end conformance.

## Status

**v0.2 draft** — starter skill and validation framework, not a certified validator. Integrate existing deterministic tests and approved datasets/profiles before using it as a publication gate.
