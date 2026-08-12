from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]


def icon(path: Path, bg: str) -> None:
    img = Image.new("RGB", (512, 512), bg)
    d = ImageDraw.Draw(img)
    d.rectangle((96, 108, 416, 404), outline="#F3EFE4", width=14)
    d.line((132, 156, 380, 156), fill="#F3EFE4", width=8)
    d.line((132, 220, 380, 220), fill="#F3EFE4", width=8)
    d.line((132, 284, 316, 284), fill="#F3EFE4", width=8)
    d.line((164, 108, 164, 404), fill="#F3EFE4", width=8)
    d.polygon([(306, 346), (394, 258), (426, 290), (338, 378)], fill="#D9B45F")
    d.polygon([(338, 378), (318, 398), (306, 346)], fill="#A77A32")
    img.save(path)


def write_fixture(case: str, title: str, meta: dict) -> None:
    base = ROOT / "tests" / "fixtures" / case
    base.mkdir(parents=True, exist_ok=True)
    (base / "assignment.md").write_text(
        f"# {title}\n\n"
        "Synthetic architecture-studio assignment for Esquisse-kun alpha smoke testing.\n\n"
        f"- Use: {meta['use']}\n"
        f"- Site area: {meta.get('site_area', 'unknown')}\n"
        f"- Target floor area: {meta.get('floor_area', 'unknown')}\n"
        f"- Road width: {meta.get('road_width', 'unknown')}\n"
        "- Review focus: zoning, circulation, light, section, concept, and first-pass code screening.\n",
        encoding="utf-8",
    )
    (base / "ground_truth.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    assets = ROOT / "plugins" / "esquisse-kun" / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    icon(assets / "esquisse-kun-icon.png", "#23443E")
    icon(assets / "esquisse-kun-logo.png", "#2F5049")
    fixtures = {
        "T1": {"title": "Detached House", "use": "single-family house", "room_names": ["living", "kitchen", "bedroom", "bath"], "dimensions": ["6.0m grid"], "orientation": "north up", "floor_area": "118 sqm", "site_area": "180 sqm", "road_width": "4.0m", "deliberately_unknown_fields": ["highest height"]},
        "T2": {"title": "Courtyard House", "use": "courtyard house", "room_names": ["living", "atelier", "bedroom", "courtyard"], "dimensions": ["courtyard 4.0m x 5.0m"], "orientation": "north up", "floor_area": "132 sqm", "site_area": "210 sqm", "road_width": "5.5m", "deliberately_unknown_fields": ["north setback"]},
        "T3": {"title": "Small Apartment", "use": "small apartment", "room_names": ["unit A", "unit B", "common stair", "bicycle"], "dimensions": ["3 units"], "orientation": "east road", "floor_area": "240 sqm", "site_area": "160 sqm", "road_width": "6.0m", "deliberately_unknown_fields": ["corridor width", "stair riser"]},
        "T4": {"title": "Small Public Building", "use": "community library", "room_names": ["reading room", "workshop", "office", "storage"], "dimensions": ["two floors"], "orientation": "north up", "floor_area": "310 sqm", "site_area": "420 sqm", "road_width": "8.0m", "deliberately_unknown_fields": ["fire district", "district plan"]},
        "T5": {"title": "Low Quality Drawing", "use": "ambiguous studio project", "room_names": ["illegible room labels"], "dimensions": [], "orientation": None, "floor_area": None, "site_area": None, "road_width": None, "deliberately_unknown_fields": ["true north", "site area", "floor area", "road width", "building height", "boundary distances"]},
    }
    for key, meta in fixtures.items():
        meta["title"] = meta.pop("title")
        write_fixture(key, meta["title"], meta)
        pdf = ROOT / "tests" / "fixtures" / key / "plan.pdf"
        img = Image.new("RGB", (1000, 700), "white")
        d = ImageDraw.Draw(img)
        d.rectangle((80, 80, 920, 620), outline="black", width=4)
        d.rectangle((160, 150, 470, 390), outline="black", width=3)
        d.rectangle((500, 150, 840, 390), outline="black", width=3)
        d.rectangle((360, 420, 650, 560), outline="black", width=3)
        d.text((100, 40), f"{key} {meta['title']} synthetic plan", fill="black")
        d.text((180, 180), "main", fill="black")
        d.text((520, 180), "sub", fill="black")
        d.text((390, 450), "void / court", fill="black")
        if key == "T5":
            d.line((120, 120, 900, 590), fill="gray", width=9)
            d.text((700, 40), "north? dim?", fill="gray")
        img.save(pdf, "PDF", resolution=100.0)


if __name__ == "__main__":
    main()
