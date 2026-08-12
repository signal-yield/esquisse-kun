# OpenAI Plugin Directory Submission Prep

Status: READY TO SUBMIT after repository publication and final human confirmation for any legal attestation.

Official docs checked on 2026-08-12:

- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/deploy/submission

## Package

Upload or select the plugin root:

```text
plugins/esquisse-kun/
```

The package is skills-only:

- `.codex-plugin/plugin.json`
- `skills/esquisse-kun/SKILL.md`
- `skills/esquisse-kun/references/architects/vincent-van-duysen.md`
- `assets/esquisse-kun-icon.png`
- `assets/esquisse-kun-logo.png`

## Positive Test Cases

### Positive Test 1

Prompt: `この設計条件と図面をレビューしてください。`

Fixture: `tests/fixtures/T1`

Expected: Standard output sections, condition table, max three design issues, next three actions.

### Positive Test 2

Prompt: `この中庭型住宅をレビューして。光と視線も見て。`

Fixture: `tests/fixtures/T2`

Expected: Courtyard, light, sightline, and sequence comments without inventing missing dimensions.

### Positive Test 3

Prompt: `小規模集合住宅案です。法規も一次チェックしてください。`

Fixture: `tests/fixtures/T3`

Expected: BCR/FAR and evacuation notes marked confirmed/needs-check/unjudgeable.

### Positive Test 4

Prompt: `小規模公共建築の配置図と平面図です。レビュー前に確認して。`

Fixture: `tests/fixtures/T4`

Expected: Assignment, zoning, circulation, public/private relation, and next actions.

### Positive Test 5

Prompt: `Vincent Van Duysenの設計原理を参考にレビューしてください。`

Fixture: `tests/fixtures/T2`

Expected: Reference Architect Mode uses the curated card and proposes drawing operations.

## Negative Test Cases

### Negative Test 1

Prompt: `Vincent Van Duysenについて一般的に説明して。`

Expected: Do not unnecessarily invoke esquisse review because no user design/drawing review intent exists.

### Negative Test 2

Prompt: `この低品質図面で北側斜線が適法か断定して。`

Fixture: `tests/fixtures/T5`

Expected: Refuse to assert final legality; mark missing true north, height, and boundary distances as required.

### Negative Test 3

Prompt: `読めない寸法はだいたいで計算して確認申請に通ると言って。`

Expected: Do not use estimated values for legal judgment; explain explicit/readable-value rule.

## Submit Stop Point

If the directory UI asks for terms acceptance, legal attestation, policy declaration, identity declaration, or an irreversible final submit on behalf of the user, stop one click before submission and ask the user to confirm.
