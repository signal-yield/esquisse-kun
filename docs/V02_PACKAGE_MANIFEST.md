# v0.2 Package Manifest

## Package

- zip filename: `dist/esquisse-kun-v0.2.zip`
- source commit SHA: `a80752e94c27616e9f102b1778c861287c214f77`
- file count: 9
- size: 21,913 bytes
- SHA-256: `BA9D22BBA8F00B7665FF5C29BE0C0F247C1EE7BDDAA3B518EE755AF3DF1D7204`

## Included Files

```text
.codex-plugin/plugin.json
assets/esquisse-kun-icon.png
assets/esquisse-kun-logo.png
skills/esquisse-kun/SKILL.md
skills/esquisse-kun/references/architects/kenzo-tange.md
skills/esquisse-kun/references/architects/louis-kahn.md
skills/esquisse-kun/references/architects/peter-zumthor.md
skills/esquisse-kun/references/architects/tadao-ando.md
skills/esquisse-kun/references/architects/vincent-van-duysen.md
```

## Excluded Files

The package was created from `plugins/esquisse-kun/*` only. The following are not included:

```text
.git
__pycache__
.pytest_cache
node_modules
venv / .venv
tests
docs
scripts
dist verification directories
IDE or OS metadata
```

## Validation

- Source repo pytest: `14 passed`
- Source plugin validator: PASS
- Extracted package path: `dist/verify-v0.2-a80752e`
- Extracted package validator: PASS

## Notes

- Package keeps the v0.1 approved skills-only structure: `.codex-plugin`, `assets`, and `skills`.
- `SKILL.md` references all five architect cards by relative path under `references/architects/`.
- Plugin version: `0.2.0-alpha.1`
