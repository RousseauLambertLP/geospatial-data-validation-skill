#!/usr/bin/env python3
"""Validate basic portable skill structure using only Python's standard library."""
from pathlib import Path
import argparse
import re
import sys

NAME = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")

def validate(root: Path):
    errors = []
    warnings = []
    skill = root / "SKILL.md"
    if not skill.is_file():
        return ["Missing SKILL.md"], warnings
    content = skill.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", content, re.S)
    if not match:
        return ["Missing YAML frontmatter delimited by ---"], warnings
    fm = match.group(1)
    values = {}
    for line in fm.splitlines():
        m = re.match(r"^(name|description):\s*(.*)$", line)
        if m:
            values[m.group(1)] = m.group(2).strip().strip('"\'')
    if not NAME.fullmatch(values.get("name", "")):
        errors.append("Frontmatter name must be lowercase hyphenated text")
    if not values.get("description"):
        errors.append("Frontmatter description is required")
    if len(content.splitlines()) < 12:
        warnings.append("SKILL.md is unusually short; review completeness")
    for marker in ("## Workflow", "## Safety"):
        if marker.lower() not in content.lower():
            warnings.append(f"Recommended section absent: {marker}")
    for p in root.rglob("*"):
        if not p.is_file() or ".git" in p.parts:
            continue
        if p.name.lower() in (".env", "id_rsa") or p.suffix.lower() in (".pem", ".key"):
            errors.append(f"Potential secret file: {p.relative_to(root)}")
    return errors, warnings

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    errors, warnings = validate(args.directory)
    for msg in errors:
        print("ERROR:", msg)
    for msg in warnings:
        print("WARN:", msg)
    if not errors:
        print("PASS: basic structural checks")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
