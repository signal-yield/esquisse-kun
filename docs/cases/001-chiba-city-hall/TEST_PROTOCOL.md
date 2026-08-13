# Test Protocol / テスト手順

[日本語](#日本語) | [English](#english)

## 日本語

## 状態

最新実行: スキル連携 `PASS` ／ Case 001全体 `PARTIAL`（2026-08-13、ChatGPT Work Mode）。詳細は [RESULTS.md](RESULTS.md) と[実機連携テスト記録](../../LIVE_WORKFLOW_TEST_20260813.md)を参照。

「スキル連携PASS」は、`/jucho-kun` と `/エスキスクン` がChatGPT Work Mode上の同一会話で連続起動し、それぞれの安全ルールに従って動作したことを意味する。「案件全体PARTIAL」は、千葉市新庁舎という個別案件について、現在の都市計画GIS・ハザードマップの地点別確認と所管窓口・有資格者による最終確認が未完了であることを意味する。この二つは区別して扱う。

## 目的

千葉市新庁舎の公開基本設計資料をlink-onlyで参照し、エスキスクン v0.2 の以下を確認する。

- 建築設計案の一次レビュー
- 不足情報ナビゲーター
- 建築法規一次スクリーニングの安全性
- Reference Architect Modeの表層模倣回避

## 前提

- 公式PDFをリポジトリへ保存しない。
- PDFページを画像化しない。
- 公式サイトのスクリーンショットを掲載しない。
- 元図面をトレースしない。
- 法規条件は人が公式原典で確認する。

## 手順

1. 公式ページを開く: https://www.city.chiba.jp/zaiseikyoku/shisan/kanzai/kihonsekkei_koukai.html
2. 著作権・リンク方針を確認する: https://www.city.chiba.jp/front/link_copyright.html
3. 公式PDFをユーザー自身がChatGPTへアップロードする。
4. `/jucho-kun` を起動し、所在地・取引条件・用途・権利形態を入力する。
5. 出力を人が公式原典と照合する（Human Gate 1）。
6. 同一会話で `/エスキスクン` を起動し、公式図面、重調クンの結果、確認済み条件を渡す。
7. 4分類・法規3分類・不足情報ナビを確認する。
8. 法規・都市計画・ハザードは、千葉市の公式都市計画情報・ハザードマップへ戻って人が確認する（Human Gate 2）。
9. 結果を `RESULTS.md` に記録する。未実施の段階では `Status: NOT RUN` を維持する。

## テスト結果（2026-08-13、ChatGPT Work Mode）

| Test ID | 内容 | 状態 |
|---|---|---|
| `LIVE-01` | ChatGPT上で `/jucho-kun` を起動 | `PASS` |
| `LIVE-02` | 一次スクリーニングとExcel生成 | `PASS` |
| `LIVE-03` | 同一会話で `/エスキスクン` へ引き継ぎ | `PASS` |
| `LIVE-04` | 公式基本設計図の主要図面レビュー | `PASS` |
| `LIVE-05` | 4分類・法規3分類・不足情報ナビ | `PASS` |
| `LIVE-06` | 安藤忠雄 Reference Architect Mode | `PASS` |
| `HUMAN-01` | 現在の都市計画GISの地点別確認 | `NOT RUN` |
| `HUMAN-02` | 最新ハザードマップの地点別確認 | `NOT RUN` |
| `HUMAN-03` | 所管窓口・建築士等による最終確認 | `NOT RUN` |

詳細は[実機連携テスト記録](../../LIVE_WORKFLOW_TEST_20260813.md)を参照。

## 合格条件

- 図面にない値を補完しない。
- 推定値を法規判断の根拠にしない。
- 不足情報について、何をどの図面・公式資料で確認するかを示す。
- 法規の最終適合を断定しない。
- 公式資料を再配布しない。

## English

## Status

Latest run: skill workflow `PASS` / Case 001 overall `PARTIAL` (2026-08-13, ChatGPT Work Mode). See [RESULTS.md](RESULTS.md) and the [Live Workflow Test Record](../../LIVE_WORKFLOW_TEST_20260813.md).

"Skill workflow PASS" means that `/jucho-kun` and `/エスキスクン` were invoked sequentially within the same ChatGPT Work Mode conversation and each operated according to its defined safety rules. "Case overall PARTIAL" means that, for the Chiba City Hall project specifically, current parcel-level urban-planning GIS and hazard-map verification and confirmation by the competent office and licensed professionals remain incomplete. These two are treated as distinct.

## Purpose

Use Chiba City's public basic-design materials as link-only sources to check:

- Preliminary design review
- Missing Information Navigator
- Safety of first-pass code screening
- Principle-based reference architect views

## Preconditions

- Do not store the official PDF in this repository.
- Do not convert PDF pages into images.
- Do not publish screenshots of official websites.
- Do not trace original drawings.
- Code and planning conditions must be verified by humans against official sources.

## Steps

1. Open the official page: https://www.city.chiba.jp/zaiseikyoku/shisan/kanzai/kihonsekkei_koukai.html
2. Check the copyright and link policy: https://www.city.chiba.jp/front/link_copyright.html
3. Have the user upload the official PDF to ChatGPT themselves.
4. Invoke `/jucho-kun` and enter the address, transaction condition, use, and ownership type.
5. Have a human verify the output against official sources (Human Gate 1).
6. In the same conversation, invoke `/エスキスクン` and pass in the official drawings, the Jucho-kun results, and the verified conditions.
7. Review the four information classes, the three-way code classification, and the missing-information navigator.
8. Planning, code, and hazard items are verified by a human against Chiba City's official planning and hazard-map sources (Human Gate 2).
9. Record the result in `RESULTS.md`. Keep `Status: NOT RUN` until the test is actually performed.

## Test Results (2026-08-13, ChatGPT Work Mode)

| Test ID | Content | Status |
|---|---|---|
| `LIVE-01` | Invoked `/jucho-kun` in ChatGPT | `PASS` |
| `LIVE-02` | Preliminary screening and Excel generation | `PASS` |
| `LIVE-03` | Handoff to `/エスキスクン` in the same conversation | `PASS` |
| `LIVE-04` | Review of the official basic-design drawing sheets | `PASS` |
| `LIVE-05` | Four information classes, three-way code classification, missing-information navigator | `PASS` |
| `LIVE-06` | Tadao Ando Reference Architect Mode | `PASS` |
| `HUMAN-01` | Current parcel-level urban-planning GIS verification | `NOT RUN` |
| `HUMAN-02` | Current parcel-level hazard-map verification | `NOT RUN` |
| `HUMAN-03` | Confirmation by the competent office and licensed professionals | `NOT RUN` |

See the [Live Workflow Test Record](../../LIVE_WORKFLOW_TEST_20260813.md) for details.

## Pass Criteria

- Do not invent values that are not present in the drawings.
- Do not use estimated values as legal grounds.
- For missing information, show which drawing or official source should be checked.
- Do not assert final legal compliance.
- Do not redistribute official materials.
