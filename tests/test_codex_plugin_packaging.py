from __future__ import annotations

import json
import struct
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "esquisse-kun"
MANIFEST = PLUGIN / ".codex-plugin" / "plugin.json"
PACKAGED_SKILL = PLUGIN / "skills" / "esquisse-kun" / "SKILL.md"
CANONICAL_SKILL = ROOT / "skills" / "esquisse-kun" / "SKILL.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_manifest_and_skill_package() -> None:
    manifest = load_json(MANIFEST)
    assert manifest["name"] == "esquisse-kun"
    assert manifest["version"] == "0.2.0-alpha.1"
    assert manifest["skills"] == "./skills/"
    assert manifest["license"] == "MIT"
    assert manifest["repository"] == "https://github.com/signal-yield/esquisse-kun"
    assert PACKAGED_SKILL.is_file()


def test_listing_metadata_limits_and_urls() -> None:
    interface = load_json(MANIFEST)["interface"]
    assert len(interface["displayName"]) <= 30
    assert len(interface["shortDescription"]) <= 30
    assert len(interface["longDescription"]) <= 4000
    assert len(interface["defaultPrompt"]) <= 3
    for prompt in interface["defaultPrompt"]:
        assert len(prompt) <= 128
    for field in ("websiteURL", "privacyPolicyURL", "termsOfServiceURL"):
        parsed = urlparse(interface[field])
        assert parsed.scheme == "https"
        assert parsed.netloc


def test_manifest_images_are_square_pngs() -> None:
    interface = load_json(MANIFEST)["interface"]
    for field in ("composerIcon", "logo"):
        image_path = PLUGIN / interface[field].removeprefix("./")
        assert image_path.is_file()
        data = image_path.read_bytes()
        assert data[:8] == b"\x89PNG\r\n\x1a\n"
        width, height = struct.unpack(">II", data[16:24])
        assert width == height == 512


def test_packaged_skill_matches_canonical() -> None:
    assert PACKAGED_SKILL.read_bytes() == CANONICAL_SKILL.read_bytes()
    result = subprocess.run(
        [sys.executable, "scripts/sync_codex_plugin_skill.py", "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr


def test_reference_card_packaged() -> None:
    path = PLUGIN / "skills" / "esquisse-kun" / "references" / "architects" / "vincent-van-duysen.md"
    text = path.read_text(encoding="utf-8")
    assert "Possible operation" in text
    assert "Do not say" in text


def test_fixtures_exist() -> None:
    for case in ("T1", "T2", "T3", "T4", "T5"):
        base = ROOT / "tests" / "fixtures" / case
        assert (base / "assignment.md").is_file()
        assert (base / "plan.pdf").is_file()
        truth = load_json(base / "ground_truth.json")
        assert "room_names" in truth
        assert "deliberately_unknown_fields" in truth
    compare = ROOT / "tests" / "fixtures" / "T6_compare"
    for name in ("assignment.md", "plan_A.pdf", "plan_B.pdf", "ground_truth.json"):
        assert (compare / name).is_file()
    truth = load_json(compare / "ground_truth.json")
    assert truth["same_assignment"] is True
    assert "100-point scores" in truth["must_not_infer"]


def test_guardrails_visible() -> None:
    text = PACKAGED_SKILL.read_text(encoding="utf-8")
    required = [
        "図面を勝手に補完しない",
        "推定値を使う場合は「参考値」と明記し、判定根拠にしない",
        "主要な問題は最大3点",
        "道路斜線",
        "隣地斜線",
        "北側斜線",
        "日影規制",
        "適法",
        "次に直す3点",
        "A/B案比較モード",
        "A案 / B案 エスキス比較",
        "まだ決めない",
        "100点満点の自動採点は禁止",
    ]
    for phrase in required:
        assert phrase in text


def test_submission_materials() -> None:
    text = (ROOT / "docs" / "OPENAI_PLUGIN_DIRECTORY_SUBMISSION.md").read_text(encoding="utf-8")
    assert text.count("### Positive Test ") == 5
    assert text.count("### Negative Test ") == 3
    assert "Submit Stop Point" in text


def test_ab_compare_negative_cases_documented() -> None:
    path = ROOT / "tests" / "fixtures" / "T6_compare" / "negative_cases.json"
    cases = json.loads(path.read_text(encoding="utf-8"))
    assert len(cases) >= 4
    expected_ids = {
        "N1_missing_b",
        "N2_different_premises",
        "N3_low_resolution_b",
        "N4_no_rubric_score_request",
    }
    assert expected_ids.issubset({case["id"] for case in cases})
    text = "\n".join(case["expected"] for case in cases)
    for phrase in ["Do not invent", "premises differ", "lower information quantity", "100-point scores"]:
        assert phrase in text


def test_no_product_audience_limiting_wording() -> None:
    checked_paths = [
        ROOT / "README.md",
        ROOT / "docs" / "DEMO_0817.md",
        ROOT / "docs" / "index.html",
        MANIFEST,
        CANONICAL_SKILL,
        PACKAGED_SKILL,
    ]
    text = "\n".join(path.read_text(encoding="utf-8") for path in checked_paths)
    forbidden = ["学" + "生", "stu" + "dent", "stu" + "dents"]
    for phrase in forbidden:
        assert phrase.lower() not in text.lower()
