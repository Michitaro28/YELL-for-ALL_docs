HTML入門ガイド
==============

HTMLとは
--------

HTML（HyperText Markup Language）は、ウェブページを作成するための標準的なマークアップ言語です。HTMLを使用することで、テキスト、画像、リンクなどを組み合わせて構造化されたウェブページを作成できます。

.. note::
    HTMLは「マークアップ言語」であり、プログラミング言語ではありません。文書の構造と意味を定義するために使用されます。

基本構造
--------

すべてのHTMLドキュメントは、以下の基本構造を持ちます：

.. code-block:: html

    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ページタイトル</title>
    </head>
    <body>
        <!-- ここにコンテンツを記述 -->
    </body>
    </html>

各要素の説明：

- ``<!DOCTYPE html>``：HTML5文書であることを宣言
- ``<html>``：HTML文書のルート要素
- ``<head>``：文書のメタデータを含む
- ``<body>``：実際に表示されるコンテンツを含む

主要なHTML要素
--------------

見出し
~~~~~~

見出しは ``<h1>`` から ``<h6>`` まで6段階のレベルがあります：

.. code-block:: html

    <h1>メインタイトル</h1>
    <h2>セクション見出し</h2>
    <h3>サブセクション見出し</h3>
    <h4>小見出し</h4>
    <h5>更に小さな見出し</h5>
    <h6>最小の見出し</h6>

段落とテキスト
~~~~~~~~~~~~~~

.. code-block:: html

    <p>これは段落です。段落は文章をグループ化するために使用します。</p>

    <p>
        <strong>太字のテキスト</strong>や
        <em>強調されたテキスト</em>、
        <mark>ハイライトされたテキスト</mark>を含めることができます。
    </p>

リスト
~~~~~~

順序なしリスト：

.. code-block:: html

    <ul>
        <li>項目1</li>
        <li>項目2</li>
        <li>項目3</li>
    </ul>

順序ありリスト：

.. code-block:: html

    <ol>
        <li>第一項目</li>
        <li>第二項目</li>
        <li>第三項目</li>
    </ol>

リンクと画像
~~~~~~~~~~~~

リンクの作成：

.. code-block:: html

    <a href="https://example.com">外部サイトへのリンク</a>
    <a href="#section1">同一ページ内のアンカーリンク</a>
    <a href="mailto:contact@example.com">メールリンク</a>

画像の挿入：

.. code-block:: html

    <img src="image.jpg" alt="画像の説明" width="300" height="200">

.. important::
    ``alt`` 属性は必ず指定しましょう。アクセシビリティの向上に重要です。

テーブル
~~~~~~~~

基本的なテーブルの構造：

.. code-block:: html

    <table>
        <thead>
            <tr>
                <th>ヘッダー1</th>
                <th>ヘッダー2</th>
                <th>ヘッダー3</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>データ1</td>
                <td>データ2</td>
                <td>データ3</td>
            </tr>
            <tr>
                <td>データ4</td>
                <td>データ5</td>
                <td>データ6</td>
            </tr>
        </tbody>
    </table>

フォーム
~~~~~~~~

ユーザー入力を受け取るフォーム：

.. code-block:: html

    <form action="/submit" method="post">
        <div>
            <label for="name">名前：</label>
            <input type="text" id="name" name="name" required>
        </div>

        <div>
            <label for="email">メールアドレス：</label>
            <input type="email" id="email" name="email" required>
        </div>

        <div>
            <label for="message">メッセージ：</label>
            <textarea id="message" name="message" rows="4" cols="50"></textarea>
        </div>

        <div>
            <input type="radio" id="male" name="gender" value="male">
            <label for="male">男性</label>

            <input type="radio" id="female" name="gender" value="female">
            <label for="female">女性</label>
        </div>

        <div>
            <input type="checkbox" id="newsletter" name="newsletter" value="yes">
            <label for="newsletter">ニュースレターを受け取る</label>
        </div>

        <button type="submit">送信</button>
    </form>

セマンティックHTML
------------------

HTML5では、文書の構造をより明確に表現するためのセマンティック要素が導入されました：

.. code-block:: html

    <header>
        <nav>
            <ul>
                <li><a href="#home">ホーム</a></li>
                <li><a href="#about">について</a></li>
                <li><a href="#contact">お問い合わせ</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <article>
            <header>
                <h1>記事のタイトル</h1>
                <time datetime="2024-01-15">2024年1月15日</time>
            </header>

            <section>
                <h2>セクション1</h2>
                <p>セクションの内容...</p>
            </section>

            <section>
                <h2>セクション2</h2>
                <p>セクションの内容...</p>
            </section>

            <aside>
                <h3>関連情報</h3>
                <p>サイドバーの内容...</p>
            </aside>
        </article>
    </main>

    <footer>
        <p>&copy; 2024 サイト名. All rights reserved.</p>
    </footer>

各要素の役割：

- ``<header>``：ヘッダー情報
- ``<nav>``：ナビゲーションリンク
- ``<main>``：メインコンテンツ
- ``<article>``：独立したコンテンツ
- ``<section>``：文書の区画
- ``<aside>``：サイドバー、補足情報
- ``<footer>``：フッター情報

属性の活用
----------

グローバル属性
~~~~~~~~~~~~~~

すべての要素で使用できる属性：

.. code-block:: html

    <div id="unique-id" class="container main-content" data-value="123">
        <p title="ツールチップテキスト">マウスオーバーで説明が表示されます</p>
    </div>

- ``id``：要素の一意識別子
- ``class``：CSSクラスの指定
- ``data-*``：カスタムデータ属性
- ``title``：ツールチップテキスト

アクセシビリティ属性
~~~~~~~~~~~~~~~~~~~~

.. code-block:: html

    <img src="chart.png" alt="2024年売上グラフ"
        aria-describedby="chart-description">

    <p id="chart-description">
        このグラフは2024年の月別売上を示しています。
        4月に最高値を記録し、全体的に上昇傾向です。
    </p>

    <button aria-label="メニューを開く" aria-expanded="false">
        ☰
    </button>

中級テクニック
--------------

CSSとの連携
~~~~~~~~~~~

HTMLとCSSを効果的に組み合わせる方法：

.. code-block:: html

    <style>
    .card {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 16px;
        margin: 16px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .card-title {
        color: #333;
        margin-bottom: 8px;
    }

    .card-content {
        color: #666;
        line-height: 1.5;
    }
    </style>

    <div class="card">
        <h3 class="card-title">カードタイトル</h3>
        <p class="card-content">カードの内容テキスト...</p>
    </div>

メタデータの最適化
~~~~~~~~~~~~~~~~~~

SEOとソーシャルメディア共有のためのメタタグ：

.. code-block:: html

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="ページの説明文（160文字以内）">
        <meta name="keywords" content="キーワード1, キーワード2, キーワード3">

        <!-- Open Graph (Facebook) -->
        <meta property="og:title" content="ページタイトル">
        <meta property="og:description" content="ページの説明">
        <meta property="og:image" content="https://example.com/image.jpg">
        <meta property="og:url" content="https://example.com/page">

        <!-- Twitter Card -->
        <meta name="twitter:card" content="summary_large_image">
        <meta name="twitter:title" content="ページタイトル">
        <meta name="twitter:description" content="ページの説明">
        <meta name="twitter:image" content="https://example.com/image.jpg">
    </head>

ベストプラクティス
------------------

コードの構造化
~~~~~~~~~~~~~~

1. **適切なインデント**を使用してコードを読みやすくする
2. **セマンティックな要素**を選択して文書構造を明確にする
3. **コメント**を適切に使用してコードを説明する

.. code-block:: html

    <!-- ヘッダーセクション -->
    <header class="site-header">
        <!-- メインナビゲーション -->
        <nav class="main-navigation">
            <ul class="nav-list">
                <li class="nav-item">
                    <a href="#home" class="nav-link">ホーム</a>
                </li>
                <!-- 他のナビゲーション項目 -->
            </ul>
        </nav>
    </header>

バリデーションとテスト
~~~~~~~~~~~~~~~~~~~~~~

HTMLコードの品質を保つために：

1. **W3C Markup Validator**でHTMLの構文をチェック
2. **アクセシビリティツール**で使いやすさを確認
3. **複数のブラウザ**でテストを実行
4. **モバイルデバイス**での表示を確認

.. tip::
    開発者ツール（F12）を使用してHTMLの構造を確認し、デバッグを行いましょう。

まとめ
------

HTMLは以下のような特徴を持つ重要な技術です：

- ウェブページの構造と意味を定義する基盤技術
- セマンティックな要素を使用することで、アクセシビリティとSEOを向上
- CSSやJavaScriptと組み合わせることで、リッチなウェブ体験を提供
- 継続的に進化している標準（HTML5、HTML Living Standard）

継続的な学習のために、最新のHTML仕様やウェブ標準の動向をフォローし、実際のプロジェクトでの実践を通じてスキルを向上させていきましょう。

.. seealso::
    - `MDN Web Docs <https://developer.mozilla.org/ja/docs/Web/HTML>`_
    - `W3C HTML仕様 <https://www.w3.org/TR/html52/>`_
    - `Can I Use <https://caniuse.com/>`_ - ブラウザサポート状況の確認