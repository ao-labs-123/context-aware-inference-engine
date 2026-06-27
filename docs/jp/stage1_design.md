# Stage1：主語推定

## 日本語の主語推定ロジック (WIP)
日本語の “主語が省略されやすい問題” を改善してみるプロジェクトです。

AI がよくやる 主語の誤読（誰が思った？誰がやった？問題） を、
できるだけシンプルなロジックで減らすことを目指しています。

## プロジェクトの目的
	•	一人称の心理動詞 → 話し手を自動で主語として推定
	•	「〜らしい」「〜と聞いた」 → 三人称（伝聞）として扱う
	•	どちらでもない時 → 主語が不明として聞き返し候補

「複雑な文でも、“誰がそう思ったのか” をなるべく間違えずに理解したい！」
というシンプルな目的で作っています。

## 基本ロジック
1. 心理動詞 → 一人称（話し手）
例：　　　		

		•	「〜と思った」
		•	「〜と感じた」
		•	「〜と信じてる」

These almost always refer to the speaker in natural Japanese.

2. 伝聞表現 → 三人称
例：	
```example
		 •「〜らしい」
　　　　　　•「〜と聞いた」
　　　　　　•「〜そうだ」

```

These usually attach information to someone who is not the speaker.

3. どっちにも当てはまらない → 不確定
→ 聞き返しロジックと組み合わせる予定（WIP）

## Simple Python Prototype
こんな感じで最初の超シンプル版を作りました👇

def estimate_subject(sentence):
    psychological_verbs = ["思う", "思った", "感じる", "感じた", "信じる", "信じた"]
    hearsay_markers = ["らしい", "と聞いた", "そうだ"]

    # 一人称（話し手）
    if any(v in sentence for v in psychological_verbs):
        return "一人称（話し手）"

    # 三人称（伝聞）
    if any(h in sentence for h in hearsay_markers):
        return "三人称（伝聞）"

    # 不明（後で聞き返しロジックを足す）
    return "主語不明"


# --- テスト ---
tests = [
    "歩いていると思った",
    "Aさんが歩いていたらしい",
    "昨日道を歩いていた"
]

for t in tests:
    print(t, "→", estimate_subject(t))

歩いていると思った → 一人称（話し手）
Aさんが歩いていたらしい → 三人称（伝聞）
昨日道を歩いていた → 主語不明

## 今後の計画
	•	不確定時の聞き返しテンプレート追加
	•	三人称判定の精度アップ
	•	文構造をもう少し分解してロバストさ強化
	•	LLM の前処理として使える形に変換したい

## 注記
このREADMEはまだ WIP（開発中）です。
進化し次第どんどん更新していく予定！

