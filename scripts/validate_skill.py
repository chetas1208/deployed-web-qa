#!/usr/bin/env python3
"""Validate the repository's Codex skill package using only the standard library."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: Path) -> str:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def main() -> None:
    skill = read(ROOT / "SKILL.md")
    if not skill.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    if "\n---\n" not in skill[4:]:
        fail("SKILL.md frontmatter is not closed")
    frontmatter, body = skill[4:].split("\n---\n", 1)

    name = re.search(r"^name:\s*([a-z0-9][a-z0-9-]*)\s*$", frontmatter, re.MULTILINE)
    description = re.search(r"^description:\s*(.+?)\s*$", frontmatter, re.MULTILINE)
    if not name:
        fail("frontmatter must contain a lowercase hyphenated name")
    if name.group(1) != ROOT.name:
        fail(f"frontmatter name {name.group(1)!r} must match directory {ROOT.name!r}")
    if not description or len(description.group(1).strip()) < 40:
        fail("frontmatter description is missing or too short")
    if "TODO" in skill or "[TODO" in skill:
        fail("skill contains unfinished TODO placeholders")
    if len(body.strip()) < 500:
        fail("skill body is unexpectedly short")

    metadata = read(ROOT / "agents" / "openai.yaml")
    for required in ("display_name:", "short_description:", "default_prompt:"):
        if required not in metadata:
            fail(f"agents/openai.yaml is missing {required}")
    if "$deployed-web-qa" not in metadata:
        fail("default_prompt must mention $deployed-web-qa")

    readme = read(ROOT / "README.md")
    for heading in ("# Deployed Web QA", "## Install", "## Safety model", "## Report shape"):
        if heading not in readme:
            fail(f"README.md is missing {heading}")

    print("Skill package is valid")


if __name__ == "__main__":
    main()
