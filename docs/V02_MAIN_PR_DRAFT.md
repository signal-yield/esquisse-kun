# v0.2 Main PR Draft

## Title

Release v0.2 with A/B comparison, missing-info navigation, and architect views

## Summary

- Adds A/B design comparison for same-assignment alternatives.
- Adds Missing Information Navigator for single-option review, A/B comparison, building-code screening, and reference architect views.
- Expands curated Reference Architect Cards to five architects: Vincent Van Duysen, Peter Zumthor, Louis Kahn, Tadao Ando / 安藤忠雄, and Kenzo Tange / 丹下健三.
- Integrates A/B comparison with architect views while keeping the final recommendation grounded in the user's assignment and drawings.
- Retains legal-review safety: no final legal compliance determination, no arbitrary scoring, and no use of estimated values as legal grounds.

## Testing

- `python -m pytest -q`: 14 passed
- Plugin validator: PASS
- Package extraction validator: PASS
- Package extraction pytest: 14 passed
- ChatGPT smoke test: manual checklist prepared in `docs/CHATGPT_V02_RELEASE_SMOKE_TEST.md`

## Safety / Regression

- v0.1 standard esquisse review remains in place.
- Assignment condition review, building-code first-pass review, slant-plane screening, shadow-regulation screening, and Van Duysen card remain covered by tests/guardrails.
- Drawing values remain separated into explicit, readable, estimated, and unknown.
- Missing information is not treated as a design defect.
- Reference architect views are principle-based and do not imitate surface style.
- Building-code review remains preliminary and does not claim final legality.

## Notes

- Do not merge directly to `main` until manual ChatGPT smoke testing is complete.
- Plugin Directory resubmission is intentionally out of scope for this PR.
