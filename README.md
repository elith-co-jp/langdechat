# LLM評価ライブラリ Lang de chat
## 概要
- LLMモデルの性能やプロンプトによるLLMの性能評価を行うライブラリです。

## インストール方法

Install from PyPI:
```
pip install langdechat
```

## 利用方法
- OpenAIのAPIキーを登録し、利用します
- 現在v0.1.1では日付計算のみの質問と回答のデータセットを6件用意しています
- 質問の前後でプロンプトを付けることでGPT-3.5の性能評価を行えます

```python
import os

os.environ["OPENAI_API_KEY"] = <OpenAIのAPIキー>

from langdechat.langeval import TastingPrompt

# プレフィックスプロンプト
h = TastingPrompt(prefix_prompt="質問：今日は火曜日です。4日後は何日？\n回答：土曜日")

# サフィックスプロンプト
h = TastingPrompt(suffix_prompt="let's think step by step")

# 付属なし
h = TastingPrompt()

h.run()
```

## データセット
- 日付計算のデータセットは[gpt4-with-calc](https://github.com/githubnext/gpt4-with-calc)のリポジトリ(MITライセンス)のデータを利用し、整形しています
