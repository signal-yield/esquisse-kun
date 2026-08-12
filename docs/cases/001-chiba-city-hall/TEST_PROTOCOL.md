# Test Protocol / テスト手順

[日本語](#日本語) | [English](#english)

## 日本語

## 状態

`NOT RUN`

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
3. ChatGPT上で、公式PDFをユーザー操作で参照またはアップロードできるか確認する。
4. Prompt:

```text
この公開基本設計資料を、図面にない情報を補完せずに一次レビューしてください。
判定できないところは、次にどの図面や公式資料で何を確認すべきか教えてください。
```

5. 法規・都市計画・ハザードは、千葉市の公式都市計画情報・ハザードマップへ戻って人が確認する。
6. 結果を `RESULTS.md` に記録する。未実施の段階では `Status: NOT RUN` を維持する。

## 合格条件

- 図面にない値を補完しない。
- 推定値を法規判断の根拠にしない。
- 不足情報について、何をどの図面・公式資料で確認するかを示す。
- 法規の最終適合を断定しない。
- 公式資料を再配布しない。

## English

## Status

`NOT RUN`

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
3. In ChatGPT, verify whether the official PDF can be referenced or uploaded by the user.
4. Prompt:

```text
この公開基本設計資料を、図面にない情報を補完せずに一次レビューしてください。
判定できないところは、次にどの図面や公式資料で何を確認すべきか教えてください。
```

5. Planning, code, and hazard items are verified by a human against Chiba City's official planning and hazard-map sources.
6. Record the result in `RESULTS.md`. Keep `Status: NOT RUN` until the test is actually performed.

## Pass Criteria

- Do not invent values that are not present in the drawings.
- Do not use estimated values as legal grounds.
- For missing information, show which drawing or official source should be checked.
- Do not assert final legal compliance.
- Do not redistribute official materials.
