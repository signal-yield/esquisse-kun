# ChatGPT v0.2 Release Smoke Test

## Test Metadata

- 実施日:
- ChatGPT環境:
- Plugin version: 0.2.0-alpha.1
- 使用fixture: `tests/fixtures/T6_compare/assignment.md`, `plan_A.pdf`, `plan_B.pdf`
- 備考:

## Test A: Standard A/B

Prompt:

```text
A案とB案を比較して。
次のエスキスに持っていくならどちらかまで教えて。
```

Checklist:

- [ ] PASS / FAIL / 要修正: A/B取り違えなし
- [ ] PASS / FAIL / 要修正: 図面の明示値と推定値を混同しない
- [ ] PASS / FAIL / 要修正: arbitrary scoreなし
- [ ] PASS / FAIL / 要修正: 推奨理由が具体的
- [ ] PASS / FAIL / 要修正: 非推奨案から移植できる要素あり

## Test B: Missing Information

Prompt:

```text
この資料で法規も含めてA案とB案を比較して。
不足している情報があれば、次に何を描けばいいか教えて。
```

Checklist:

- [ ] PASS / FAIL / 要修正: 不足最大3件
- [ ] PASS / FAIL / 要修正: 必須度分類あり
- [ ] PASS / FAIL / 要修正: どの図面へ何を書くか案内
- [ ] PASS / FAIL / 要修正: 資料不足を案の欠陥扱いしない

## Test C: Van Duysen

Prompt:

```text
Vincent Van Duysenの設計原理を参照してA案とB案を比較して。
```

Expected focus:

- [ ] PASS / FAIL / 要修正: 抑制
- [ ] PASS / FAIL / 要修正: 素材
- [ ] PASS / FAIL / 要修正: 選択的開放
- [ ] PASS / FAIL / 要修正: 内外関係

## Test D: Zumthor

Prompt:

```text
Peter Zumthorの設計原理を参照してA案とB案を比較して。
```

Expected focus:

- [ ] PASS / FAIL / 要修正: 身体感覚
- [ ] PASS / FAIL / 要修正: Atmosphere
- [ ] PASS / FAIL / 要修正: 光
- [ ] PASS / FAIL / 要修正: 素材
- [ ] PASS / FAIL / 要修正: シークエンス

## Test E: Kahn

Prompt:

```text
Louis Kahnの設計原理を参照してA案とB案を比較して。
```

Expected focus:

- [ ] PASS / FAIL / 要修正: served / servant
- [ ] PASS / FAIL / 要修正: 秩序
- [ ] PASS / FAIL / 要修正: 構造
- [ ] PASS / FAIL / 要修正: 幾何
- [ ] PASS / FAIL / 要修正: 光

## Test F: Ando

Prompt:

```text
安藤忠雄の設計原理を参照してA案とB案を比較して。
```

Expected focus:

- [ ] PASS / FAIL / 要修正: 壁
- [ ] PASS / FAIL / 要修正: 幾何
- [ ] PASS / FAIL / 要修正: アプローチ
- [ ] PASS / FAIL / 要修正: 光と暗さ
- [ ] PASS / FAIL / 要修正: 視線
- [ ] PASS / FAIL / 要修正: 自然

## Test G: Tange

Prompt:

```text
丹下健三の設計原理を参照してA案とB案を比較して。
```

Expected focus:

- [ ] PASS / FAIL / 要修正: 都市との関係
- [ ] PASS / FAIL / 要修正: 公共性
- [ ] PASS / FAIL / 要修正: 外部空間
- [ ] PASS / FAIL / 要修正: 人の流れ
- [ ] PASS / FAIL / 要修正: 構造
- [ ] PASS / FAIL / 要修正: 建築群

## Architect Differentiation

5人が違う結論を出す必要はない。同じA案を推奨してもPASS。ただし、何を見たか、なぜA/B/まだ決めないなのか、次に何を確認するか、どんな設計操作を提案するかには明確な差が必要。

FAIL例:

- 5人ともほぼ同一文章
- 5人とも光・素材・動線だけ
- 建築家名を入れ替えただけ

## Final Result

- [ ] PASS
- [ ] FAIL
- [ ] 要修正
