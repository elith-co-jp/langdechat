# LLM評価ライブラリ Lang de chat（ラング・ド・シャ）
## 概要
- LLMによるプロダクトリリースの際にモデル自体の評価やプロンプトの評価を簡単に行いたいと思い、作成しました。
- OpenAIなどのLLMのでは利用にAPI料金がかかってしまいますが、「Lang de chat」を利用すれば気軽に少量データでタスクに特化した日本語プロンプトで評価できます。
- 日本語LLMモデルの性能や日本語プロンプトによるLLMの性能評価を行うライブラリです。
- 今後は様々なタスクに特化したLLMモデル評価・プロンプト評価が可能です。

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

# 追加プロンプトなし
h = TastingPrompt()

h.run()
```

## データセット
- 日付計算のデータセットは[gpt4-with-calc](https://github.com/githubnext/gpt4-with-calc)のリポジトリ(MITライセンス)のデータを利用し、整形しています。
- 今後はJGLUEデータセットやライセンス的に問題のないデータセットの日本語翻訳したデータセット、アノテーションから作成したデータセットを追加する予定です。

## 評価可能なタスク
- 日付計算-1：今日は火曜日です。4日後は何日？


