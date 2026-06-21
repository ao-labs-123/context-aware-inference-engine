```en

Core logic and structural analysis for Japanese dialogue are documented here. 
The underlying architecture is designed to be language-agnostic.

```
    English Documentation is available in ⁠/en⁠


本研究は、大規模言語モデルのような統計的生成AIに依存せず、会話や出来事の「文脈」を論理的に圧縮・推定する軽量な基盤AIの可能性を示すものである。

## Documentation
- [Background・Objective・Approach](docs/jp/README.ja.md)

## Stages
- [Stage 1: 基本的な文脈推定](docs/jp/stage1_design.md)
- [Stage 2: 最小限の聞き返し](docs/jp/stage2_design.md)
- [Stage 3: 因果関係推定](docs/jp/stage3_design.md)
- [Stage 4: 修飾構造の理解](docs/jp/stage4_design.md)
- [Stage 5: 名詞間の格関係推定](docs/jp/stage5_design.md)

## Comparison with Conventional AI
| 観点 | 統計的言語モデル（主に次トークン予測） | 文脈推定システム |
|---|---|---|
| 基本原理 | 大規模コーパスに基づく確率的予測 | 出来事・関係・役割に基づく論理推定 |
| 処理単位 | トークン／文単位 | 出来事・文脈単位 |
| 文脈の保持 | 発話履歴への依存が大きい | 抽象化された文脈構造を保持 |
| 記憶の圧縮方法 | 確率分布による統計的圧縮 | 因果関係・意図・役割の論理圧縮 |
| 会話が長くなった場合 | 文脈の一貫性が低下しやすい | 意味構造が保持されやすい |
| 聞き返し | 明示的に設計しない限り不安定 | 文脈不確定時に意図的に発生 |
| 暗黙意図の扱い | 表現依存で推定が揺らぎやすい | 前後関係から安定的に推定可能 |
| 主語・省略表現 | 明示されないと誤解釈しやすい | 日本語特有の省略構造に適応 |
| 計算資源 | 高い計算資源・メモリを要求 | 軽量な推論で動作可能 |
| コスト構造 | 高性能化に比例して高コスト | 低容量・低コストで運用可能 |
| 主な強み | 自然な文章生成・汎用知識 | 文脈理解・解釈の一貫性 |
| 想定用途 | 汎用対話・文章生成 | 解釈重視の対話・補助的AI基盤 |

※ 本比較は「対話における文脈保持と解釈」を主眼としたものであり、生成品質や知識量の優劣を示すものではない。

## Evidence / Demonstration

本リポジトリでは、文脈推定システムの段階的な理解能力の変化を、
例文および実証用デモを通して示す。

- [例文ベースの実証](https://github.com/ao-labs-123/subject-inference-demo)
- [インタラクティブデモ（Streamlit）](https://share.streamlit.io/)

各Stageは精度向上を目的とするだけでなく、AIの解釈過程を人間が追跡できるよう設計されています。

*現在、各Stageの解釈差を確認できるチャット形式の実証環境を構築中です。

詳細はdocs参照 or 実証で示す
