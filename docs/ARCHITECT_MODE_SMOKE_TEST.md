# Architect Mode Smoke Test

Date: 2026-08-12
Branch: feat/v0.2-architect-cards

## Status

未実施

Reason:
- ChatGPT UI automation is not available from this environment. Previous Windows Computer Use attempts stopped because the active Chrome URL could not be determined with enough confidence for policy enforcement.

## Manual Test Prompts

Use `tests/fixtures/T6_compare/assignment.md`, `plan_A.pdf`, and `plan_B.pdf`.

```text
Vincent Van Duysenの設計原理でA案とB案を比較して
```

```text
Peter Zumthorの設計原理でA案とB案を比較して
```

```text
Louis Kahnの設計原理でA案とB案を比較して
```

```text
安藤忠雄の設計原理でA案とB案を比較して
```

```text
丹下健三の設計原理でA案とB案を比較して
```

## Expected Differentiation

- Van Duysen: selective views, restraint, material continuity.
- Zumthor: body, atmosphere, material presence, threshold sequence.
- Kahn: served/servant, order, structure, light.
- Ando: geometry, wall, light/dark, approach, nature.
- Tange: urban scale, public flow, structure, civic exterior space.
