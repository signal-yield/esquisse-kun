# エスキスクン / Esquisse-kun

[日本語](#日本語) | [English](#english)

![Version](https://img.shields.io/badge/version-v0.2%20alpha.2-blue)
![Tests](https://img.shields.io/badge/tests-16%20passed-brightgreen)
![Live workflow](https://img.shields.io/badge/live%20workflow-passed-brightgreen)
![Case 001](https://img.shields.io/badge/case%20001-partial-yellow)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## 日本語

**図面を勝手に補完しない、建築設計の一次レビュー用AIプラグイン。**

エスキスクンは、建築設計案の条件、図面、空間構成、動線、光、視線、断面、建築法規の見落とし候補を、ホワイトボックスに整理するskills-only pluginです。読めない値を作らず、明示値・読取値・推定値・不明値を分けて扱います。

### ステータス

| Branch | Status |
|---|---|
| `main` | public alpha `0.2.0-alpha.2` |
| `develop/v0.2` | merged into `main` |

検証範囲ごとの状態は次のとおりです。

| 検証範囲 | 状態 | 意味 |
|---|---|---|
| 自動・スモークテスト | 16 passed | 既存テスト関数の結果 |
| ChatGPT実機連携 | PASS | 重調クン→エスキスクンの連続起動 |
| Case 001 | PARTIAL | GIS・ハザード・所管確認が未完了 |

いずれのバッジ・ステータスも、機能が所定の安全ルールに従って動いたことを示すものであり、現在の法規適合性・安全性の確認を意味しません。

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

#### 3分で分かるワークフロー

```text
1. /jucho-kun で行政調査項目を整理
2. 人が公式GIS・原典を確認
3. /エスキスクン で図面と行政条件を照合
4. 人が最終判断
```

価値の源泉は「AI同士が一致したから正しい」ことではなく、それぞれの出力から公式原典へ戻って確認できることにあります。

### 実機検証

2026-08-13、ChatGPT Work Mode上の同一会話で `/jucho-kun` と `/エスキスクン` を連続起動する実機テストを実施しました。スキル連携（起動・引き継ぎ・4分類・法規3分類・不足情報ナビ）は **PASS** です。ただし、千葉市新庁舎を題材としたCase 001全体は、現在のGIS・ハザードマップの地点別確認と所管窓口・有資格者による最終確認が未完了のため、引き続き **PARTIAL** です。

- [実機連携テスト記録](docs/LIVE_WORKFLOW_TEST_20260813.md)
- [Case 001: 千葉市新庁舎](docs/cases/001-chiba-city-hall/README.md)
- [Case 001 Test Protocol](docs/cases/001-chiba-city-hall/TEST_PROTOCOL.md)
- [Case 001 Results](docs/cases/001-chiba-city-hall/RESULTS.md)

### 出力例

Case 001における出力の要約例です。PDF画像やスクリーンショットではなく、テキスト表として示します。これはCase 001の要約例であり、現在の法的判断ではありません。

| 項目 | 状態 | 次の確認 |
|---|---|---|
| 用途地域 | 基本設計時点では確認 | 現在の公式GISで再確認 |
| 接道・道路種別 | 要確認 | 道路種別・法定幅員・境界資料 |
| 避難・防火区画 | 判定不能 | 避難計画図・防火区画図 |

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

### 免責事項

本pluginは設計学習・設計検討のための一次レビュー支援です。最終的な法規判断、設計判断、著作権・利用許諾判断は、最新の公式原典、自治体資料、建築士、確認検査機関、権利者等により確認してください。

### 作者

Signal Yield Advisory / Koichi Matsuda<br>
signalYield@gmail.com<br>
https://signal-yield.github.io/esquisse-kun/

### ライセンス

MIT

## English

**A white-box AI plugin for preliminary architectural design review—without inventing missing drawing information.**

Esquisse-kun is a skills-only plugin for early architectural design review. It organizes design requirements, drawings, spatial planning, circulation, light, sightlines, sections, and first-pass building-code screening while keeping the evidence visible.

### Status

| Branch | Status |
|---|---|
| `main` | public alpha `0.2.0-alpha.2` |
| `develop/v0.2` | merged into `main` |

Verification scope and status:

| Verification scope | Status | Meaning |
|---|---|---|
| Automated smoke tests | 16 passed | Result of the existing test functions |
| ChatGPT live workflow | PASS | Sequential invocation of Jucho-kun then Esquisse-kun |
| Case 001 | PARTIAL | Current GIS, hazard, and competent-office checks remain outstanding |

Every badge and status here indicates that a feature operated according to its defined safety rules. None of them indicate current legal compliance or safety.

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

#### Workflow in Three Minutes

```text
1. Use /jucho-kun to organize administrative research items
2. A human verifies the official GIS and source documents
3. Use /エスキスクン to cross-check drawings against administrative conditions
4. A human makes the final decision
```

The value is not that two AI outputs agree with each other. It is that each output can be traced back to official sources for human verification.

### Live Verification

On 2026-08-13, a live test invoked `/jucho-kun` and `/エスキスクン` sequentially within the same ChatGPT Work Mode conversation. The skill workflow itself — invocation, handoff, the four information classes, three-way code classification, and the missing-information navigator — is **PASS**. Case 001, which uses the Chiba City Hall project as its subject, remains **PARTIAL**, because current parcel-level GIS and hazard-map verification and confirmation by the competent office and licensed professionals are still outstanding.

- [Live Workflow Test Record](docs/LIVE_WORKFLOW_TEST_20260813.md)
- [Case 001: Chiba City Hall](docs/cases/001-chiba-city-hall/README.md)
- [Case 001 Test Protocol](docs/cases/001-chiba-city-hall/TEST_PROTOCOL.md)
- [Case 001 Results](docs/cases/001-chiba-city-hall/RESULTS.md)

### Example Output

An example output summary from Case 001, shown as a text table rather than a PDF image or screenshot. This is a Case 001 summary example, not a current legal determination.

| Item | Status | Next verification |
|---|---|---|
| Zoning | Confirmed for the basic-design stage | Re-verify against the current official GIS |
| Road access and classification | Requires verification | Road classification, legal width, and boundary material |
| Egress and fire compartments | Undetermined | Egress plan and fire-compartment plan |

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
