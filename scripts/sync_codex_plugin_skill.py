from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "skills" / "esquisse-kun" / "SKILL.md"
PACKAGED = ROOT / "plugins" / "esquisse-kun" / "skills" / "esquisse-kun" / "SKILL.md"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        if CANONICAL.read_bytes() != PACKAGED.read_bytes():
            raise SystemExit("Packaged skill differs from canonical skill.")
        return 0
    PACKAGED.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(CANONICAL, PACKAGED)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
