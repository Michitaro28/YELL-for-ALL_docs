Git/GitHub の基本的な使い方
=============================

このドキュメントでは、YELL for ALL の開発チーム向けに Git および GitHub の基本的な使い方を説明します。

.. contents::
    :local:
    :depth: 2

Git の基本コマンド
-------------------

Git は分散型バージョン管理システムです。以下に代表的なコマンドを示します。

**初期化とクローン**

.. code-block:: bash

    git init         # 新しいリポジトリの初期化
    git clone <URL>  # 既存リポジトリの複製

**変更の記録**

.. code-block:: bash

    git status             # 作業ツリーの状態確認
    git add <file>         # ステージング
    git commit -m "msg"    # コミット

**履歴の確認**

.. code-block:: bash

    git log                # コミット履歴の表示
    git diff               # 差分の表示

**リモートとのやり取り**

.. code-block:: bash

    git pull               # リモートから取得＆マージ
    git push               # ローカルの変更をリモートへ

**ブランチ操作**

.. code-block:: bash

    git branch             # ブランチ一覧
    git checkout -b dev    # 新しいブランチ作成＆切り替え
    git merge dev          # 他のブランチをマージ

GitHub の基本操作
------------------

GitHub は Git リポジトリをホスティングするサービスです。以下の操作が基本です。

1. **リポジトリの作成**
    - GitHub 上で新しいリポジトリを作成
    - 初期設定（README、.gitignore、ライセンス）を選択

2. **リポジトリの連携**

.. code-block:: bash


    git remote add origin https://github.com/ユーザー名/リポジトリ名.git
    git push -u origin main


3. **Pull Request (PR) の作成**
    - 新しいブランチで開発
    - - GitHub 上で PR を作成し、レビューを依頼

4. **Issue の活用**
    - バグや要望を管理
    - タグ・担当者を設定してトラッキング

チーム開発における運用ルール
-----------------------------

- `main` ブランチは常に安定した状態を保つ
- 開発は必ずブランチを切って行う（例: `feature/〇〇`, `bugfix/〇〇`）
- PR は他メンバーのレビュー後に `main` にマージ
- コミットメッセージはわかりやすく、目的が明確なものにする

参考リンク
----------

- Git 公式: https://git-scm.com/
- GitHub Docs: https://docs.github.com/ja
