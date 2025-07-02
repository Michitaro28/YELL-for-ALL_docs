# GEMINI CLI

## GEMINI CLIとは
Gemini CLI とは、ターミナルから直接 Gemini の機能を利用できる、オープンソース（Apache 2.0 ライセンス）の AI エージェントです。gemini コマンドを介して、自然言語でコーディング、デバッグ、情報検索、各種タスクの自動化などを実行できます。

## 料金
Gemini CLI は**無料**で利用できます。
個人の Google アカウントでログインすることで、1分あたり 60 リクエスト、1日あたり 1,000 リクエストまで無料でモデルを呼び出すことができます。
もちろん Google Workspace アカウントでも利用可能ですが、Google Workspace アカウントで Gemini CLI を利用する場合は Google Cloud プロジェクト ID の指定が必須です。
より多くのリクエストが必要な場合、使用量ベース課金の Google AI Studio または Vertex AI、あるいは有償版の Gemini Code Assist Standard / Enterprise ライセンスを利用することも可能です。

## 導入手順

1. 前提
node.js v18.0以上が必須のようです。環境にnode.js v18.0以上がない場合は下記からインストールしてください。
[Node.jsダウンロード](https://nodejs.org/ja/download)

2. Gemini CLIのダウンロード
ターミナル/コマンドプロンプトを開き、下記を実行するだけです。
```bash
npx https://github.com/google-gemini/gemini-cli
```

グローバル環境へのインストールは下記
```bash
npm install -g @google/gemini-cli
```

インストールは英語ですが、びっくりしないように！
求められてることは、
1. 見た目の設定
2. Googleアカウントへのログイン

上記の認証が完了したら使用できます。


# 活用に向けて
## 実際に使ってみよう！
現在（2025/07/03）では、リリースから１週間ほどです。実際の使い方や活用方法などは開発の中で使用するほか、活用についての記事なども多く出るでしょう！それらを活用しながら開発を進めていきましょう！


# 参考リンク
- [GeminiCLI公式ドキュメント](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/)
- [GeminiCodeAssist](https://codeassist.google/?hl=ja)
- [gemini-cli_GitHub公式リポジトリ](https://github.com/google-gemini/gemini-cli)
- [GeminiCLIの簡単チュートリアル（Zenn）](https://zenn.dev/schroneko/articles/gemini-cli-tutorial?source=post_page-----76af9c25f5c2---------------------------------------)
- [Googleの新AIエージェント「Gemini CLI」登場！使い方と基本機能を速報解説](https://chatgpt-lab.com/n/n4ccc9d035cab)
- [Gemini CLIを解説](https://blog.g-gen.co.jp/entry/gemini-cli-explained)