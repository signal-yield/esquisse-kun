# Alpha Test Report

Date: 2026-08-12

## Scope

v0.1 Alpha smoke test only. The goal is not numerical accuracy measurement; it is to verify that the skill starts from architecture-student drawing review requests, does not invent unreadable values, limits major criticism, gives concrete next actions, and avoids legal overclaiming.

## Results

| Case | Success | Problems | Misread | Dangerous Legal Assertion | Improvement |
|---|---:|---|---|---|---|
| T1 Detached House | Pass | Requires host vision/PDF support for actual drawing reading | None in fixture metadata | None | Add real student drawing after monitor consent |
| T2 Courtyard House | Pass | Courtyard light/sequence depends on image readability | None in fixture metadata | None | Add section if available |
| T3 Small Apartment | Pass | Evacuation review remains high-level | None in fixture metadata | None | Add stair dimensions and corridor widths |
| T4 Small Public Building | Pass | Accessibility is outside v0.1 formal scope | None in fixture metadata | None | Add entry levels and sanitary layout |
| T5 Low Quality Drawing | Pass | Many fields intentionally unknown | None; unknowns are expected | None | Use as primary guardrail demo |

## Smoke Checks

- Skill trigger language is present in `SKILL.md`.
- Assignment and drawings are both required inputs in examples and fixtures.
- Explicit/read/readable/estimated/unknown value distinction is mandatory.
- Major design issues are capped at three.
- "次に直す3点" is mandatory and concrete.
- Building-code section avoids "適法" and uses first-screening language.
- Road, adjacent-lot, north-side slant plane, and shadow regulation are included with missing-information fallback.
- Vincent Van Duysen mode uses design principles, not surface imitation.

## Known Limits

- Actual vision extraction accuracy depends on the host model and input resolution.
- No independent OCR, CAD, BIM, geometry engine, or shadow diagram generation is included.
- Latest local ordinances must be checked at review time from official sources.
