# ステージ2 ― 特定困難な主語に対する聞き返し（Clarification）

## 概要：
本ステップは、インテリジェントなフォールバック（代替措置）として機能します。ステージ1の決定論的なマッピングで主語を特定できない場合、あるいは文脈分析を行っても複数の候補が等しく妥当である場合にのみ、対象を絞った自然な形式で聞き返しを行います。これは、曖昧さが許容範囲を超えた場合にのみ介入するという、人間同士の対話に近い挙動を再現するものです。

## 主要ポイント：
**1. 閾値ベースのトリガー**：

エージェント特定に対する確信度が低い場合、または構文的に複数の候補が存在し、言語パターンのみでは解決できない場合にのみ聞き返しを開始します。
- 文に明示的な主語や心理的動詞、証拠的なマーカー（例：伝聞など）がない場合、明確化の依頼は厳格に必要です。

**2. 最小限の介入**：

対話の流れを妨げないよう、介入は特定の曖昧箇所のみに限定します。網羅的な質問は避け、文脈に基づいた確認（例：「それはあなた自身のことですか、それとも〇〇さんのことですか？」）を行います。

**3. 人間中心の信頼性**：

人間にとっても判断が難しい文は存在するという前提に立ちます。誤った推測を避けることで、AIの推論精度を保ち、ユーザーからの信頼を確保します。

| Input | Logic Process | Result |
| :--- | :--- | :--- |
| "Thought was strange." | Psychological Verb + Null Subject $\rightarrow$ [Default: Speaker] | AI assigns "I" as the agent. |
| "Thought it was strange apparently." | Psychological Verb + Null Subject + Evidential Marker $\rightarrow$ [Override: 3rd Party] | AI assigns "He/She/They" as the agent. |
| "Succeeded because you helped." | Null Subject + No Psychological Verb + No Evidential Marker $\rightarrow$ [Fallback: Ambiguous] | AI triggers Stage 2 clarification (Undetermined agent). |
