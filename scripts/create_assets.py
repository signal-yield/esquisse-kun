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
    compare_base = ROOT / "tests" / "fixtures" / "T6_compare"
    compare_base.mkdir(parents=True, exist_ok=True)
    (compare_base / "assignment.md").write_text(
        "# T6 A/B Courtyard Studio\n\n"
        "Synthetic same-assignment comparison fixture for Esquisse-kun v0.2.\n\n"
        "- Use: small courtyard studio and residence\n"
        "- Site area: 220 sqm\n"
        "- Target floor area: 135 sqm\n"
        "- Road width: 5.0m south road\n"
        "- Concept: compare a clear circulation option with a richer courtyard/light option.\n",
        encoding="utf-8",
    )
    (compare_base / "ground_truth.json").write_text(
        json.dumps(
            {
                "same_assignment": True,
                "plan_a_strengths": ["clear entrance-to-main-room circulation", "rational zoning", "direct courtyard sightline"],
                "plan_a_weaknesses": ["courtyard sequence is direct", "average daylight variation"],
                "plan_b_strengths": ["richer indoor-outdoor sequence", "stronger south daylight", "varied courtyard sightline"],
                "plan_b_weaknesses": ["longer circulation", "service route may cross main sequence"],
                "expected_comparison_topics": ["circulation", "courtyard", "light", "sightline", "first-pass code risk"],
                "unknown_values": ["building height", "true north confirmation", "boundary distances"],
                "must_not_infer": ["final legality", "slant-plane compliance", "shadow regulation compliance", "100-point scores"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    for suffix, title, direct, south_light in [
        ("A", "Option A clear circulation", True, False),
        ("B", "Option B layered courtyard", False, True),
    ]:
        img = Image.new("RGB", (1000, 700), "white")
        d = ImageDraw.Draw(img)
        d.text((100, 40), f"T6 plan_{suffix} {title}", fill="black")
        d.rectangle((80, 80, 920, 620), outline="black", width=4)
        d.line((80, 620, 920, 620), fill="#555555", width=8)
        d.text((430, 640), "south road 5.0m", fill="black")
        d.rectangle((380, 240, 620, 460), outline="#2F7D57", width=5)
        d.text((430, 330), "courtyard", fill="#2F7D57")
        if direct:
            d.rectangle((150, 160, 360, 360), outline="black", width=3)
            d.rectangle((640, 160, 850, 360), outline="black", width=3)
            d.line((500, 620, 500, 460), fill="#D9B45F", width=10)
            d.line((500, 460, 500, 240), fill="#D9B45F", width=10)
            d.text((180, 200), "studio", fill="black")
            d.text((670, 200), "living", fill="black")
            d.text((520, 520), "clear route", fill="#A77A32")
        else:
            d.rectangle((150, 140, 350, 310), outline="black", width=3)
            d.rectangle((660, 140, 850, 310), outline="black", width=3)
            d.rectangle((170, 440, 430, 570), outline="black", width=3)
            d.line((500, 620, 300, 500), fill="#D9B45F", width=10)
            d.line((300, 500, 380, 350), fill="#D9B45F", width=10)
            d.line((620, 460, 800, 560), fill="#D9B45F", width=10)
            d.text((180, 180), "atelier", fill="black")
            d.text((690, 180), "living", fill="black")
            d.text((200, 480), "bedroom", fill="black")
            d.text((625, 520), "layered views", fill="#A77A32")
        if south_light:
            d.rectangle((465, 600, 760, 620), fill="#F2D46B")
            d.text((650, 590), "south light", fill="#A77A32")
        img.save(compare_base / f"plan_{suffix}.pdf", "PDF", resolution=100.0)
    missing_base = ROOT / "tests" / "fixtures" / "T7_missing_info"
    missing_base.mkdir(parents=True, exist_ok=True)
    patterns = {
        "T7_1_single": {
            "title": "Single option missing true north and section",
            "missing": ["true north", "courtyard section"],
            "expected_nav": ["配置図へ真北矢印", "中庭と主室を横断する断面図"],
        },
        "T7_2_code": {
            "title": "Code review missing road width height north setback",
            "missing": ["road width", "building height", "north boundary distance"],
            "expected_nav": ["前面道路幅員", "建物高さ", "北側境界距離"],
        },
        "T7_3_ab": {
            "title": "A/B comparison with missing B section",
            "missing": ["B option courtyard section"],
            "expected_nav": ["B案の中庭・LDK・個室を横断する断面図"],
        },
    }
    (missing_base / "ground_truth.json").write_text(
        json.dumps(
            {
                "patterns": patterns,
                "required_phrases": ["必須", "追加後に分かること", "次に必要な情報・図面"],
                "must_not": ["資料不足を設計品質の低さとして扱う", "適法", "推定値を法規根拠にする"],
                "max_basic_missing_items": 3,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    for key, info in patterns.items():
        case_dir = missing_base / key
        case_dir.mkdir(parents=True, exist_ok=True)
        (case_dir / "assignment.md").write_text(
            f"# {info['title']}\n\n"
            "Synthetic missing-information fixture for Esquisse-kun v0.2.\n\n"
            "- Review should continue with available information.\n"
            "- Missing information must be converted into concrete next drawings or notes.\n"
            "- Do not infer unreadable legal values.\n",
            encoding="utf-8",
        )
        img = Image.new("RGB", (1000, 700), "white")
        d = ImageDraw.Draw(img)
        d.text((90, 45), key + " " + info["title"], fill="black")
        d.rectangle((90, 90, 910, 610), outline="black", width=4)
        d.rectangle((180, 160, 460, 360), outline="black", width=3)
        d.rectangle((520, 160, 820, 360), outline="black", width=3)
        d.rectangle((380, 420, 620, 560), outline="#2F7D57", width=4)
        d.text((220, 220), "main room", fill="black")
        d.text((560, 220), "support", fill="black")
        d.text((430, 480), "court", fill="#2F7D57")
        if key == "T7_2_code":
            d.text((110, 630), "road width ?", fill="gray")
            d.text((730, 520), "height ?", fill="gray")
            d.text((110, 110), "north setback ?", fill="gray")
        if key == "T7_3_ab":
            d.text((690, 570), "B: section missing", fill="gray")
        img.save(case_dir / "plan.pdf", "PDF", resolution=100.0)


if __name__ == "__main__":
    main()
