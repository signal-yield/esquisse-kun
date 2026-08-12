# エスキスクン / Esquisse-kun

[日本語](#日本語) | [English](#english)

## 日本語

**図面を勝手に補完しない、建築設計の一次レビュー用AIプラグイン。**

エスキスクンは、建築設計案の条件、図面、空間構成、動線、光、視線、断面、建築法規の見落とし候補を、ホワイトボックスに整理するskills-only pluginです。読めない値を作らず、明示値・読取値・推定値・不明値を分けて扱います。

### Status

| Branch | Status |
|---|---|
| `main` | approved v0.1 |
| `develop/v0.2` | release candidate `0.2.0-alpha.2` |

### できること

- 設計条件・要求条件と図面の一次レビュー
- 建築法規の一次スクリーニング
- 道路斜線、隣地斜線、北側斜線、日影規制の確認事項整理
- A案・B案比較
- 不足情報ナビゲーター
- Reference Architect Mode
- 公開資料を使ったlink-onlyケーススタディ手順の記録

### 情報の4分類

| 区分 | 意味 | 法規判断への使用 |
|---|---|---|
| 明示値 | 条件資料、面積表、寸法線、凡例に明記された値 | 使用可 |
| 読取値 | 図面から十分明瞭に読める値 | 使用可。ただし出所を示す |
| 推定値 | 縮尺・形状等から推測した値 | 参考のみ。法規判断の根拠にしない |
| 不明値 | 判読不能・未提出・不足 | 使用しない |

### A案・B案比較

同一条件に対する2案を、課題条件、空間構成、動線、光・視線、平面・断面、コンセプト、法規一次確認から比較します。100点満点の疑似採点や勝敗だけの断定は行わず、次の設計検討へ持っていく案と、もう一方から移植できる要素を整理します。

### 不足情報ナビゲーター

判定不能で止めず、次を返します。

```text
何が不足しているか
なぜ必要か
どの図面へ何を追加するか
追加後に何を判断できるか
```

### Reference Architect Mode

Reference Architect Modeは、建築家本人の意図を代弁したり、作品を表層的に模倣したりする機能ではありません。観察可能な特徴を設計原理へ翻訳し、現在案に応用するための問い・図面確認・設計操作を提示します。

v0.2では以下のcurated reference cardを収録しています。

- Vincent Van Duysen
- Peter Zumthor
- Louis Kahn
- Tadao Ando / 安藤忠雄
- Kenzo Tange / 丹下健三

### 重調クンとの連携

推奨ワークフロー:

```text
重調クンによる行政情報調査
→ 人による公式原典の確認
→ エスキスクンによる図面レビュー
```

AI同士の一致を正解とは扱いません。人が公式原典へ戻って確認できることを重視します。

詳しくは [重調クン×エスキスクン連携手順](docs/WORKFLOW_JUCHO_ESQUISSE.md) を参照してください。

### 公開図面を使ったケーススタディ

公開資料を使う場合も、公開されていることを再配布許諾とは扱いません。Case 001では千葉市新庁舎の公開基本設計資料をlink-onlyで扱います。

- [実案件ケース一覧](docs/cases/README.md)
- [Case 001: 千葉市新庁舎](docs/cases/001-chiba-city-hall/README.md)
- [Case 001 Test Protocol](docs/cases/001-chiba-city-hall/TEST_PROTOCOL.md)

### インストール方法

Repo-hosted Codex testing:

```bash
codex plugin marketplace add signal-yield/esquisse-kun
```

Then open `/plugins`, select the `signal-yield` marketplace, install `esquisse-kun`, and start a new conversation.

### プロンプト例

```text
この設計条件と図面をレビューしてください。
```

```text
A案とB案を比較して、次の設計検討へどちらを持っていくべきかレビューしてください。
```

```text
不足している情報があれば、次にどの図面へ何を追加すればいいか教えて。
```

```text
Peter Zumthorの設計原理を参照してA案とB案を比較してください。
```

### このツールがしないこと

- 図面にない値を補完する
- 法規の最終適合判断を行う
- 確認申請や専門家判断を代替する
- 建築家本人の意図を代弁する
- 作品写真、公開PDF、スクリーンショットを再配布する
- CAD/BIM/構造/設備の自動検証を行う

### 関連文書

- [Demo](docs/DEMO_0817.md)
- [データ・著作権・再配布ルール](docs/DATA_AND_RIGHTS.md)
- [ケーススタディ雛形](docs/CASE_STUDY_TEMPLATE.md)
- [v0.2 package manifest](docs/V02_PACKAGE_MANIFEST.md)

### Disclaimer

本pluginは設計学習・設計検討のための一次レビュー支援です。最終的な法規判断、設計判断、著作権・利用許諾判断は、最新の公式原典、自治体資料、建築士、確認検査機関、権利者等により確認してください。

### Author

Signal Yield Advisory / Koichi Matsuda<br>
signalYield@gmail.com<br>
https://signal-yield.github.io/esquisse-kun/

### License

MIT

## English

**A white-box AI plugin for preliminary architectural design review—without inventing missing drawing information.**

Esquisse-kun is a skills-only plugin for early architectural design review. It organizes design requirements, drawings, spatial planning, circulation, light, sightlines, sections, and first-pass building-code screening while keeping the evidence visible.

### Status

| Branch | Status |
|---|---|
| `main` | approved v0.1 |
| `develop/v0.2` | release candidate `0.2.0-alpha.2` |

### What It Does

- Reviews design requirements and drawings as a preliminary review.
- Separates drawing information into explicit, readable, estimated, and unknown values.
- Screens building-code issues as human-verifiable check items.
- Compares A/B design options without arbitrary scores.
- Converts missing information into concrete next drawings or notes.
- Applies reference-architect principles without style imitation.

### Four Information Classes

| Class | Meaning | Legal screening use |
|---|---|---|
| Explicit values | Written in requirements, schedules, dimensions, or legends | May be used |
| Readable values | Clearly readable from drawings | May be used with source noted |
| Estimated values | Inferred from scale or shape | Reference only; not legal grounds |
| Unknown values | Missing, unreadable, or not provided | Not used |

### A/B Design Comparison

The comparison mode checks whether two options share comparable conditions, then reviews requirements, spatial structure, circulation, light and sightlines, plan/section logic, concept alignment, and first-pass code risks. It recommends A, B, or still undecided, and identifies one transferable element from the other option.

### Missing Information Navigator

When the plugin cannot judge something, it should not stop at "unknown." It explains what is missing, why it matters, where to add it, and what can be reviewed after adding it.

### Reference Architect Mode

Reference Architect Mode does not imitate a designer's surface style or speak for the architect. It translates observable work and discourse into design principles, questions, drawing checks, and possible operations.

Curated cards in v0.2:

- Vincent Van Duysen
- Peter Zumthor
- Louis Kahn
- Tadao Ando
- Kenzo Tange

### Jucho-kun Workflow

Recommended workflow:

```text
Administrative research with Jucho-kun
→ Human verification against official sources
→ Drawing review with Esquisse-kun
```

Agreement between two AI outputs is not treated as proof. The value is that a human can return to official sources and verify assumptions.

See [Jucho-kun x Esquisse-kun workflow](docs/WORKFLOW_JUCHO_ESQUISSE.en.md).

### Public Drawing Case Studies

Public availability is not treated as redistribution permission. Case 001 uses official Chiba City documents as link-only sources.

- [Case studies](docs/cases/README.md)
- [Case 001: Chiba City Hall](docs/cases/001-chiba-city-hall/README.md)
- [Case 001 Test Protocol](docs/cases/001-chiba-city-hall/TEST_PROTOCOL.md)

### Installation

Repo-hosted Codex testing:

```bash
codex plugin marketplace add signal-yield/esquisse-kun
```

Open `/plugins`, select the `signal-yield` marketplace, install `esquisse-kun`, and start a new conversation.

### Example Prompts

```text
Review this design brief and drawings.
```

```text
Compare Option A and Option B and recommend which one to take into the next design iteration.
```

```text
If anything cannot be judged, tell me what to add to which drawing.
```

```text
Compare Option A and Option B using Peter Zumthor's design principles.
```

### What This Tool Does Not Do

- Invent missing drawing values
- Provide final legal compliance determinations
- Replace architects, reviewers, authorities, or rights holders
- Speak on behalf of reference architects
- Redistribute public PDFs, screenshots, or project images
- Perform CAD/BIM/structural/MEP verification

### Documents

- [Demo](docs/DEMO_0817.md)
- [Data, Rights, and Redistribution Rules](docs/DATA_AND_RIGHTS.en.md)
- [Case Study Template](docs/CASE_STUDY_TEMPLATE.en.md)
- [v0.2 package manifest](docs/V02_PACKAGE_MANIFEST.md)

### Disclaimer

This plugin supports preliminary design review and learning-oriented screening only. Final design, legal, copyright, and code-related decisions must be verified by humans against official sources, local authorities, licensed professionals, inspection bodies, and rights holders.

### Author

Signal Yield Advisory / Koichi Matsuda<br>
signalYield@gmail.com<br>
https://signal-yield.github.io/esquisse-kun/

### License

MIT
