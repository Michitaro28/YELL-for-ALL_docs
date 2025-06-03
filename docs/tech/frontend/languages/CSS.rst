CSS入門ガイド
=============

CSSとは
-------

CSS（Cascading Style Sheets）は、HTMLで作成された文書の見た目やレイアウトを制御するためのスタイルシート言語です。CSSを使用することで、文書の構造（HTML）と表現（スタイル）を分離し、美しく使いやすいウェブページを作成できます。

.. note::
    CSSの「Cascading」は「連鎖」や「継承」を意味し、スタイルが親要素から子要素に継承される特性を表しています。

CSSの記述方法
-------------

CSSをHTMLに適用する3つの方法があります：

インラインスタイル
~~~~~~~~~~~~~~~~~~

HTML要素の ``style`` 属性に直接記述：

.. code-block:: html

    <p style="color: blue; font-size: 16px;">青色のテキスト</p>

内部スタイルシート
~~~~~~~~~~~~~~~~~~

HTML文書の ``<head>`` 内に ``<style>`` タグで記述：

.. code-block:: html

    <head>
        <style>
            p {
                color: blue;
                font-size: 16px;
            }
        </style>
    </head>

外部スタイルシート
~~~~~~~~~~~~~~~~~~

別のCSSファイルを作成してHTMLから読み込み：

.. code-block:: html

    <head>
        <link rel="stylesheet" href="styles.css">
    </head>

.. code-block:: css

   /* パフォーマンス最適化のテクニック */
   
    /* will-changeでアニメーション最適化 */
    .animated-element {
        will-change: transform, opacity;
        animation: slideIn 0.3s ease-out;
    }
   
   /* アニメーション完了後にwill-changeをリセット */
    .animated-element.animation-complete {
        will-change: auto;
    }
   
   /* transform3dでハードウェアアクセラレーション */
    .hardware-accelerated {
        transform: translate3d(0, 0, 0);
    }
   
   /* 効率的なセレクタの使用 */
    .specific-class {
       /* 良い例：クラスセレクタ */
    }

   /* 避けるべき：複雑なセレクタ */
   /* div > ul > li:nth-child(odd) > a:hover { } */

アクセシビリティの考慮
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: css

   /* フォーカス表示の改善 */
    button:focus,
    input:focus,
    textarea:focus,
    select:focus {
        outline: 2px solid #007bff;
        outline-offset: 2px;
    }
    
    /* ハイコントラストモード対応 */
    @media (prefers-contrast: high) {
        .card {
            border: 2px solid #000;
        }
        
        .button {
            border: 2px solid currentColor;
        }
    }
    
   /* 動きを減らす設定への対応 */
    @media (prefers-reduced-motion: reduce) {
       *,
       *::before,
       *::after {
            animation-duration: 0.01ms !important;
            animation-iteration-count: 1 !important;
            transition-duration: 0.01ms !important;
            scroll-behavior: auto !important;
        }
    }
   
   /* ダークモード対応 */
    @media (prefers-color-scheme: dark) {
        :root {
            --background-color: #1a1a1a;
            --text-color: #ffffff;
            --border-color: #404040;
        }
        
        body {
            background-color: var(--background-color);
            color: var(--text-color);
        }
        
        .card {
            background-color: #2d2d2d;
            border-color: var(--border-color);
        }
    }

現代的なCSSテクニック
--------------------

コンテナクエリ
~~~~~~~~~~~~~~

要素のサイズに基づくスタイル適用：

.. code-block:: css

    .card-container {
        container-type: inline-size;
        container-name: card;
    }
    
    .card {
        padding: 1rem;
    }
    
    .card__title {
        font-size: 1.25rem;
    }
    
    @container card (min-width: 300px) {
        .card {
            padding: 2rem;
        }
        
        .card__title {
            font-size: 1.5rem;
        }
    }
    
    @container card (min-width: 500px) {
        .card {
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 2rem;
        }
    }

CSS論理プロパティ
~~~~~~~~~~~~~~~~~

国際化に配慮したプロパティ：

.. code-block:: css

   .text-content {
       /* 従来の物理プロパティ */
        margin-left: 20px;
        padding-right: 15px;
        border-left: 2px solid blue;
        
       /* 論理プロパティ（推奨） */
        margin-inline-start: 20px;
        padding-inline-end: 15px;
        border-inline-start: 2px solid blue;
       
       /* 上下の論理プロパティ */
       margin-block-start: 10px;  /* margin-top */
       margin-block-end: 10px;    /* margin-bottom */
       padding-block: 15px;       /* padding-top + padding-bottom */
    }
    
    .writing-mode-example {
       writing-mode: vertical-rl; /* 縦書き（右から左） */
       /* この場合、論理プロパティが有効に働く */
    }

CSS関数の活用
~~~~~~~~~~~~~

.. code-block:: css

    .modern-functions {
       /* calc()で動的計算 */
        width: calc(100% - 40px);
        height: calc(100vh - 80px);
        
        /* min(), max(), clamp()でレスポンシブな値 */
        font-size: clamp(1rem, 4vw, 2rem);
        width: min(90%, 1200px);
        height: max(300px, 50vh);
        
        /* カスタムプロパティとの組み合わせ */
        margin: calc(var(--spacing-base) * 2);
        
        /* color-mix()で色の混合 */
        background-color: color-mix(in srgb, var(--primary-color) 80%, white);
        
        /* 環境変数（セーフエリア対応） */
        padding-top: env(safe-area-inset-top);
        padding-bottom: env(safe-area-inset-bottom);
    }

CSS Subgrid
~~~~~~~~~~~

.. code-block:: css

    .main-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
    }
    
    .card-grid {
        display: grid;
        grid-template-rows: subgrid;
        grid-row: span 3;
    }
    
    /* すべてのカードで行の高さが統一される */
    .card {
        display: grid;
        grid-template-rows: subgrid;
        grid-row: span 3;
    }

プリプロセッサ連携
------------------

Sass/SCSS例
~~~~~~~~~~~

.. code-block:: text

   // 変数定義
    $primary-color: #007bff;
    $secondary-color: #6c757d;
    $font-size-base: 16px;
    $spacing-unit: 8px;
    
    // マップ（連想配列）
    $colors: (
        'primary': $primary-color,
        'secondary': $secondary-color,
        'success': #28a745,
        'danger': #dc3545
    );
    
    $breakpoints: (
        'sm': 576px,
        'md': 768px,
        'lg': 992px,
        'xl': 1200px
    );
    
   // ミックスイン（再利用可能なスタイル）
    @mixin button-style($bg-color, $text-color: white) {
        background-color: $bg-color;
        color: $text-color;
        padding: ($spacing-unit * 1.5) ($spacing-unit * 3);
        border: none;
        border-radius: 4px;
        cursor: pointer;
        transition: all 0.3s ease;
        
        &:hover {
            background-color: darken($bg-color, 10%);
            transform: translateY(-2px);
        }
    }
    
    // メディアクエリミックスイン
    @mixin respond-to($breakpoint) {
        @if map-has-key($breakpoints, $breakpoint) {
            @media (min-width: map-get($breakpoints, $breakpoint)) {
                @content;
            }
        }
    }
   
   // 使用例
    .button {
        @include button-style(map-get($colors, 'primary'));
        
        &--secondary {
            @include button-style(map-get($colors, 'secondary'));
        }
        
        &--large {
            @include respond-to('md') {
                font-size: $font-size-base * 1.25;
                padding: ($spacing-unit * 2) ($spacing-unit * 4);
            }
        }
    }
   
   // ネスト記法
    .card {
        background: white;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        
        &__header {
            padding: $spacing-unit * 2;
            border-bottom: 1px solid #eee;
            
            h2 {
                margin: 0;
                color: $primary-color;
            }
        }
        
        &__content {
                padding: $spacing-unit * 2;
                
            p {
                margin-bottom: $spacing-unit;
                
                &:last-child {
                    margin-bottom: 0;
                }
            }
        }
        
        // 疑似クラス
        &:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
        }
    }

CSS-in-JS例（React + Styled Components）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

    import styled, { css } from 'styled-components';
    
    // テーマ定義
    const theme = {
        colors: {
            primary: '#007bff',
            secondary: '#6c757d',
            success: '#28a745',
            danger: '#dc3545'
        },
        spacing: {
            xs: '4px',
            sm: '8px',
            md: '16px',
            lg: '24px',
            xl: '32px'
        },
        breakpoints: {
            sm: '576px',
            md: '768px',
            lg: '992px',
            xl: '1200px'
        }
    };
   
   // スタイル付きコンポーネント
    const Button = styled.button`
        background-color: ${props => props.theme.colors.primary};
        color: white;
        padding: ${props => props.theme.spacing.sm} ${props => props.theme.spacing.md};
        border: none;
        border-radius: 4px;
        cursor: pointer;
        transition: all 0.3s ease;
        
        &:hover {
            background-color: ${props => darken(0.1, props.theme.colors.primary)};
            transform: translateY(-2px);
        }
        
        /* プロップスに基づく条件分岐 */
        ${props => props.variant === 'secondary' && css`
            background-color: ${props.theme.colors.secondary};
        `}
        
        ${props => props.size === 'large' && css`
            padding: ${props.theme.spacing.md} ${props.theme.spacing.lg};
            font-size: 18px;
        `}
        
        /* レスポンシブ対応 */
        @media (min-width: ${props => props.theme.breakpoints.md}) {
            padding: ${props => props.theme.spacing.md} ${props => props.theme.spacing.lg};
        }
    `;
    
    const Card = styled.div`
        background: white;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        overflow: hidden;
        transition: all 0.3s ease;
        
        &:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
        }
    `;
    
    const CardHeader = styled.div`
        padding: ${props => props.theme.spacing.lg};
        border-bottom: 1px solid #eee;
    `;
    
    const CardContent = styled.div`
        padding: ${props => props.theme.spacing.lg};
    `;

    トラブルシューティング
----------------------

よくある問題と解決法
~~~~~~~~~~~~~~~~~~~~

**問題1: スタイルが適用されない**

.. code-block:: css

   /* 詳細度の問題 */
   /* 解決法：より具体的なセレクタを使用 */
    .container .card {
        color: blue; /* より詳細度が高い */
    }
    
    /* またはカスタムプロパティを使用 */
    .card {
        color: var(--card-text-color, black);
    }

**問題2: レイアウトの崩れ**

.. code-block:: css

   /* box-sizingの統一 */
   * {
    box-sizing: border-box;
    }
   
   /* フレックスボックスでのアイテム伸縮制御 */
    .flex-item {
       flex-shrink: 0; /* 収縮を防ぐ */
       min-width: 0;   /* テキストオーバーフロー対策 */
    }

**問題3: パフォーマンスの問題**

.. code-block:: css

   /* 非効率なセレクタを避ける */
   /* NG */
   * { color: red; }
   div > * { margin: 10px; }
   
   /* OK */
    .text-content { color: red; }
   .spaced-content > * { margin: 10px; }
   
   /* transform使用でリペイントを避ける */
    .animated {
       transform: translateX(100px); /* Good */
       /* left: 100px; Bad - リフローが発生 */
    }

デバッグ手法
~~~~~~~~~~~~

.. code-block:: css

   /* 開発時のデバッグCSS */
   .debug * {
        outline: 1px solid red;
    }
    
    .debug *:hover {
        background-color: rgba(255, 0, 0, 0.1);
    }
    
    /* グリッドラインの表示 */
    .grid-debug {
        background-image:
            linear-gradient(rgba(0, 0, 255, 0.2) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 0, 255, 0.2) 1px, transparent 1px);
        background-size: 20px 20px;
    }
    
    /* フレックスボックスの可視化 */
    .flex-debug {
        background: repeating-linear-gradient(
            45deg,
            transparent,
            transparent 10px,
            rgba(255, 255, 0, 0.1) 10px,
            rgba(255, 255, 0, 0.1) 20px
        );
    }

まとめ
------

CSSは以下のような特徴を持つ重要な技術です：

- ウェブページの見た目とレイアウトを制御する基盤技術
- カスケード（継承）により効率的なスタイル管理が可能
- レスポンシブデザインやアニメーションなど、現代的なUI/UX実現に不可欠
- フレックスボックス、グリッド、カスタムプロパティなど継続的に進化

効果的なCSS開発のために：

- **設計思想**：BEMやSMACSSなどの手法を採用
- **保守性**：カスタムプロパティやプリプロセッサの活用
- **パフォーマンス**：効率的なセレクタとアニメーション最適化
- **アクセシビリティ**：すべてのユーザーに配慮したスタイル設計
- **モダンな機能**：コンテナクエリや論理プロパティの活用

継続的な学習のために、CSS仕様の最新動向をフォローし、実際のプロジェクトでの実践を通じてスキルを向上させていきましょう。

.. seealso::
    - `MDN Web Docs CSS <https://developer.mozilla.org/ja/docs/Web/CSS>`_
    - `W3C CSS仕様 <https://www.w3.org/Style/CSS/>`_
    - `Can I Use <https://caniuse.com/>`_ - ブラウザサポート状況
    - `CSS-Tricks <https://css-tricks.com/>`_ - 実践的なテクニック集
    - `Flexbox Froggy <https://flexboxfroggy.com/>`_ - フレックスボックス学習ゲーム
   - `Grid Garden <https://cssgridgarden.com/>`_ - グリッドレイアウト学習ゲーム styles.css */
    p {
        color: blue;
        font-size: 16px;
    }

.. tip::
    保守性と再利用性の観点から、外部スタイルシートの使用が推奨されます。

CSS基本構文
-----------

CSSの基本的な構文は以下の通りです：

.. code-block:: text
    セレクタ {
        プロパティ: 値;
        プロパティ: 値;
    }

例：

.. code-block:: text

    h1 {
        color: #333;
        font-size: 24px;
        text-align: center;
    }

セレクタの種類
--------------

要素セレクタ
~~~~~~~~~~~~

HTML要素名を指定：

.. code-block:: text

    p {
        color: black;
    }
    
    h1, h2, h3 {
        font-family: Arial, sans-serif;
    }

クラスセレクタ
~~~~~~~~~~~~~~

クラス属性を指定（``.`` で始まる）：

.. code-block:: css

    .highlight {
        background-color: yellow;
    }
    
    .container {
        max-width: 1200px;
        margin: 0 auto;
    }

    .. code-block:: html

    <p class="highlight">ハイライトされたテキスト</p>
    <div class="container">コンテナ内の要素</div>

IDセレクタ
~~~~~~~~~~

ID属性を指定（``#`` で始まる）：

.. code-block:: text

    #header {
        background-color: #f0f0f0;
        padding: 20px;
    }
    
    #navigation {
        position: fixed;
        top: 0;
        width: 100%;
    }

    .. code-block:: html

    <header id="header">ヘッダー</header>
    <nav id="navigation">ナビゲーション</nav>

属性セレクタ
~~~~~~~~~~~~

属性の値に基づいて選択：

.. code-block:: text

    input[type="text"] {
        border: 1px solid #ccc;
        padding: 8px;
    }
    
    a[href^="https://"] {
        color: green;
    }
    
    img[alt*="logo"] {
        width: 100px;
    }

疑似クラスと疑似要素
~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

    /* 疑似クラス */
    a:hover {
        color: red;
        text-decoration: underline;
    }
    
    input:focus {
        outline: 2px solid blue;
    }
    
    li:nth-child(odd) {
        background-color: #f9f9f9;
    }
    
    /* 疑似要素 */
    p::first-line {
        font-weight: bold;
    }
    
    .quote::before {
        content: """;
    }
    
    .quote::after {
        content: """;
    }

    主要なCSSプロパティ
    -------------------

    テキストスタイル
    ~~~~~~~~~~~~~~~~

.. code-block:: text

    .text-style {
       color: #333;                    /* 文字色 */
       font-family: "Helvetica", Arial, sans-serif;  /* フォント */
       font-size: 16px;                /* フォントサイズ */
       font-weight: bold;              /* フォントの太さ */
       font-style: italic;             /* フォントスタイル */
       text-align: center;             /* テキスト配置 */
       text-decoration: underline;     /* テキスト装飾 */
       line-height: 1.5;               /* 行間 */
       letter-spacing: 0.1em;          /* 文字間隔 */
       text-transform: uppercase;      /* 大文字変換 */
    }

背景
~~~~

    .. code-block:: css

    .background-example {
        background-color: #f0f0f0;
        background-image: url('pattern.png');
        background-repeat: no-repeat;
        background-position: center;
        background-size: cover;
        
        /* 短縮記法 */
        background: #f0f0f0 url('pattern.png') no-repeat center/cover;
    }

    ボーダー
    ~~~~~~~~

    .. code-block:: text

    .border-example {
        border-width: 2px;
        border-style: solid;
        border-color: #333;
        
        /* 短縮記法 */
        border: 2px solid #333;
        
        /* 個別指定 */
        border-top: 1px solid red;
        border-right: 2px dashed blue;
        border-bottom: 3px dotted green;
        border-left: 4px double orange;
        
        border-radius: 8px;             /* 角丸 */
    }

    マージンとパディング
    ~~~~~~~~~~~~~~~~~~~~

    .. code-block:: text

    .spacing-example {
        /* マージン（外側の余白） */
        margin-top: 10px;
        margin-right: 20px;
        margin-bottom: 10px;
        margin-left: 20px;
        
        /* 短縮記法 */
        margin: 10px 20px;              /* 上下 左右 */
        margin: 10px 20px 15px 25px;    /* 上 右 下 左 */
        
        /* パディング（内側の余白） */
        padding: 15px;                  /* 全方向 */
        padding: 10px 20px;             /* 上下 左右 */
    }

    ボックスモデル
    --------------

    CSSのボックスモデルは、すべての要素を矩形のボックスとして扱います：

    .. code-block:: text

    .box-model {
        width: 300px;           /* コンテンツ幅 */
        height: 200px;          /* コンテンツ高さ */
        padding: 20px;          /* 内側余白 */
        border: 5px solid #333; /* ボーダー */
        margin: 10px;           /* 外側余白 */
        
        /* ボックスサイズの計算方法を変更 */
        box-sizing: border-box; /* パディングとボーダーを含む */
    }

    .. important::
    ``box-sizing: border-box`` を使用すると、widthとheightにパディングとボーダーが含まれるため、レイアウトが予測しやすくなります。

    レイアウト
    ----------

    ディスプレイプロパティ
    ~~~~~~~~~~~~~~~~~~~~~~

    .. code-block:: text

    .display-examples {
        display: block;         /* ブロック要素 */
        display: inline;        /* インライン要素 */
        display: inline-block;  /* インラインブロック */
        display: none;          /* 非表示 */
        display: flex;          /* フレックスボックス */
        display: grid;          /* グリッド */
    }

    ポジション
    ~~~~~~~~~~

    .. code-block:: css

    .position-examples {
        position: static;       /* デフォルト */
        position: relative;     /* 相対位置 */
        position: absolute;     /* 絶対位置 */
        position: fixed;        /* 固定位置 */
        position: sticky;       /* スティッキー位置 */
        
        top: 10px;
        right: 20px;
        bottom: 30px;
        left: 40px;
        z-index: 1000;          /* 重なり順 */
    }

    フレックスボックス
    ~~~~~~~~~~~~~~~~~~

    現代的なレイアウト手法：

    .. code-block:: text

    .flex-container {
        display: flex;
        flex-direction: row;        /* row, column, row-reverse, column-reverse */
        justify-content: center;    /* 主軸の配置 */
        align-items: center;        /* 交差軸の配置 */
        flex-wrap: wrap;            /* 折り返し */
        gap: 20px;                  /* アイテム間の間隔 */
    }
    
    .flex-item {
        flex: 1;                    /* 伸縮比 */
        flex-grow: 1;               /* 伸長比 */
        flex-shrink: 1;             /* 収縮比 */
        flex-basis: auto;           /* 基本サイズ */
        align-self: flex-start;     /* 個別の交差軸配置 */
    }

    実用例：

    .. code-block:: text

    /* 3カラムレイアウト */
    .three-column {
        display: flex;
        gap: 20px;
    }
    
    .column {
        flex: 1;
        padding: 20px;
        background-color: #f9f9f9;
    }
    
    /* センタリング */
    .center-content {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    グリッドレイアウト
    ~~~~~~~~~~~~~~~~~~

    2次元レイアウトシステム：

    .. code-block:: text

    .grid-container {
        display: grid;
        grid-template-columns: 1fr 2fr 1fr;    /* 列の定義 */
        grid-template-rows: auto 1fr auto;     /* 行の定義 */
        grid-gap: 20px;                        /* アイテム間隔 */
        height: 100vh;
    }
    
    .grid-item-1 {
        grid-column: 1 / 3;     /* 列1から3まで */
        grid-row: 1;            /* 行1 */
    }
    
    .grid-item-2 {
        grid-area: 2 / 1 / 3 / 4;  /* 行2から3、列1から4 */
    }

    実用的なグリッドレイアウト：

    .. code-block:: text

    /* レスポンシブカードレイアウト */
    .card-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
        padding: 20px;
    }
    
    /* ヘッダー、メイン、フッターレイアウト */
    .page-layout {
        display: grid;
        grid-template-areas:
            "header header"
            "sidebar main"
            "footer footer";
        grid-template-rows: auto 1fr auto;
        grid-template-columns: 250px 1fr;
        min-height: 100vh;
    }
    
    .header { grid-area: header; }
    .sidebar { grid-area: sidebar; }
    .main { grid-area: main; }
    .footer { grid-area: footer; }

    レスポンシブデザイン
    --------------------

    メディアクエリ
    ~~~~~~~~~~~~~~

    異なる画面サイズに対応するスタイル：

    .. code-block:: text

    /* ベーススタイル（モバイルファースト） */
    .container {
        padding: 10px;
        font-size: 14px;
    }
    
    /* タブレット以上 */
    @media (min-width: 768px) {
        .container {
            padding: 20px;
            font-size: 16px;
        }
    }
    
    /* デスクトップ以上 */
    @media (min-width: 1024px) {
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 30px;
            font-size: 18px;
        }
    }
    
    /* 高解像度ディスプレイ対応 */
    @media (min-resolution: 2dppx) {
        .logo {
            background-image: url('logo@2x.png');
            background-size: 100px 50px;
        }
    }

    フルードレイアウト
    ~~~~~~~~~~~~~~~~~~

    .. code-block:: text

    .fluid-layout {
        width: 100%;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 5%;
    }
    
    .responsive-image {
        max-width: 100%;
        height: auto;
    }
    
    .responsive-video {
        position: relative;
        width: 100%;
        height: 0;
        padding-bottom: 56.25%; /* 16:9アスペクト比 */
    }
    
    .responsive-video iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }

    アニメーションとトランジション
    ------------------------------

    トランジション
    ~~~~~~~~~~~~~~

    プロパティの変化をスムーズに：

    .. code-block:: text

    .transition-example {
        background-color: blue;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        
        /* すべてのプロパティに0.3秒のトランジション */
        transition: all 0.3s ease;
    }
    
    .transition-example:hover {
        background-color: darkblue;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* 個別プロパティの指定 */
    .specific-transition {
        transition-property: background-color, transform;
        transition-duration: 0.3s, 0.5s;
        transition-timing-function: ease, ease-in-out;
        transition-delay: 0s, 0.1s;
    }

    キーフレームアニメーション
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    複雑なアニメーションの作成：

    .. code-block:: text

    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.1);
        }
    }
    
    .animated-element {
        animation: fadeIn 0.6s ease-out;
        }
    
    .pulsing-button {
        animation: pulse 2s infinite;
        }

    /* 複数アニメーションの組み合わせ */
    .complex-animation {
        animation:
            fadeIn 0.6s ease-out,
            pulse 2s infinite 0.6s;
            }

    カスタムプロパティ（CSS変数）
    -----------------------------

    再利用可能な値の定義：

    .. code-block:: text

    :root {
        /* カラーパレット */
        --primary-color: #007bff;
        --secondary-color: #6c757d;
        --success-color: #28a745;
        --danger-color: #dc3545;
        
        /* フォント */
        --font-family-base: "Helvetica Neue", Arial, sans-serif;
        --font-size-base: 16px;
        --line-height-base: 1.5;
        
        /* スペーシング */
        --spacing-sm: 8px;
        --spacing-md: 16px;
        --spacing-lg: 24px;
        --spacing-xl: 32px;
        
        /* ブレークポイント */
        --breakpoint-sm: 576px;
        --breakpoint-md: 768px;
        --breakpoint-lg: 992px;
        --breakpoint-xl: 1200px;
        }
    
    .button {
        background-color: var(--primary-color);
        color: white;
        padding: var(--spacing-sm) var(--spacing-md);
        font-family: var(--font-family-base);
        border: none;
        border-radius: 4px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        }
    
    .button:hover {
        background-color: color-mix(in srgb, var(--primary-color) 80%, black);
        }
    
    .button--secondary {
        background-color: var(--secondary-color);
        }
    
    .button--success {
        background-color: var(--success-color);
        }

    中級テクニック
    --------------

    セレクタの詳細度
    ~~~~~~~~~~~~~~~~

    CSSの適用優先順位を理解する：

    .. code-block:: text

    /* 詳細度: 0,0,0,1 */
    p {
        color: black;
        }
    
    /* 詳細度: 0,0,1,0 */
    .text {
        color: blue;
        }
    
    /* 詳細度: 0,1,0,0 */
    #content {
        color: green;
        }
    
    /* 詳細度: 0,0,1,1 */
    p.text {
        color: red;
        }
    
    /* 詳細度: 0,1,1,1 */
    #content p.text {
        color: purple;
        }
    
    /* !important（推奨されない） */
    .override {
        color: orange !important;
        }

    .. warning::
    ``!important`` の使用は避け、適切なセレクタ設計を心がけましょう。

    フロートクリアフィックス
    ~~~~~~~~~~~~~~~~~~~~~~~~

    .. code-block:: text

    /* 古い手法（参考用） */
    .clearfix::after {
        content: "";
        display: table;
        clear: both;
        }
    
    .float-left {
        float: left;
        }
    
    .float-right {
        float: right;
        }

    .. note::
    現代では、フレックスボックスやグリッドレイアウトの使用が推奨されます。

    CSS設計手法
    ~~~~~~~~~~~

    BEM記法の例：

    .. code-block:: text

    /* Block */
        .card {
            border: 1px solid #ddd;
            border-radius: 8px;
            overflow: hidden;
            }
        
        /* Element */
        .card__header {
            padding: 20px;
            background-color: #f8f9fa;
            border-bottom: 1px solid #ddd;
            }
        
        .card__title {
            margin: 0;
            font-size: 18px;
            font-weight: bold;
            }
        
        .card__content {
            padding: 20px;
            }
        
        .card__footer {
            padding: 15px 20px;
            background-color: #f8f9fa;
            border-top: 1px solid #ddd;
            }
        
        /* Modifier */
        .card--featured {
            border-color: #007bff;
            box-shadow: 0 4px 12px rgba(0,123,255,0.15);
            }
        
        .card--large {
            max-width: 600px;
            }
        
        .card__title--large {
            font-size: 24px;
            }


    パフォーマンス最適化
    --------------------


    効率的なセレクタ
    ~~~~~~~~~~~~~~~~~

    .. code-block:: text

    /* 効率的 */
    .navigation-item {
        /* スタイル */
    }
    
    /* 非効率（避ける） */
    div > ul > li > a {
        /* スタイル */
    }
    
    /* 非効率（避ける） */
    * {
        box-sizing: border-box;
    }
    
    /* 効率的 */
    html {
        box-sizing: border-box;
    }
    
    *, *::before, *::after {
        box-sizing: inherit;
    }

    CSSの軽量化
    ~~~~~~~~~~~

    .. code-block:: text

    /* 短縮プロパティの活用 */
    .optimized {
        /* 個別指定（冗長） */
        margin-top: 10px;
        margin-right: 20px;
        margin-bottom: 10px;
        margin-left: 20px;
        
        /* 短縮指定（推奨） */
        margin: 10px 20px;
        
        /* フォントの短縮指定 */
        font: bold 16px/1.5 Arial, sans-serif;
        /* font-weight: bold; font-size: 16px; line-height: 1.5; font-family: Arial, sans-serif; */
    }

    デバッグとツール
    ----------------

    開発者ツールの活用
    ~~~~~~~~~~~~~~~~~~

    .. code-block:: text

    /* デバッグ用のボーダー */
    * {
        outline: 1px solid red;
    }
    
    /* 特定要素のデバッグ */
    .debug {
        background-color: rgba(255, 0, 0, 0.1);
        border: 2px solid red;
    }
    
    /* グリッドの可視化 */
    .grid-debug {
        background-image:
            linear-gradient(rgba(255, 0, 0, 0.1) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 0, 0, 0.1) 1px, transparent 1px);
        background-size: 20px 20px;
    }

    実践的な例
    ----------

    カードコンポーネント
    ~~~~~~~~~~~~~~~~~~~~

    .. code-block:: css

    .card {
        background: white;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        overflow: hidden;
        transition: all 0.3s ease;
        max-width: 400px;
        margin: 20px;
    }
    
    .card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
    }
    
    .card__image {
        width: 100%;
        height: 200px;
        object-fit: cover;
    }
    
    .card__content {
        padding: 24px;
    }
    
    .card__title {
        margin: 0 0 12px 0;
        font-size: 20px;
        font-weight: 600;
        color: #333;
    }
    
    .card__description {
        margin: 0 0 20px 0;
        color: #666;
        line-height: 1.6;
    }
    
    .card__button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 6px;
        cursor: pointer;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .card__button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }

    ナビゲーションメニュー
    ~~~~~~~~~~~~~~~~~~~~~~

    .. code-block:: text

    .navigation {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 0 20px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    
    .nav-list {
        display: flex;
        list-style: none;
        margin: 0;
        padding: 0;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .nav-item {
        position: relative;
    }
    
    .nav-link {
        display: block;
        color: white;
        text-decoration: none;
        padding: 20px;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .nav-link::before {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        width: 0;
        height: 3px;
        background: #ffffff;
        transition: all 0.3s ease;
        transform: translateX(-50%);
    }
    
    .nav-link:hover::before {
        width: 80%;
    }
    
    .nav-link:hover {
        background: rgba(255, 255, 255, 0.1);
    }
    
    /* ドロップダウンメニュー */
    .dropdown {
        position: absolute;
        top: 100%;
        left: 0;
        background: white;
        min-width: 200px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        border-radius: 4px;
        opacity: 0;
        visibility: hidden;
        transform: translateY(-10px);
        transition: all 0.3s ease;
    }
    
    .nav-item:hover .dropdown {
        opacity: 1;
        visibility: visible;
        transform: translateY(0);
    }
    
    .dropdown-link {
        color: #333;
        padding: 12px 20px;
        border-bottom: 1px solid #eee;
    }
    
    .dropdown-link:hover {
        background: #f8f9fa;
    }

    ベストプラクティス
    ------------------

    コードの構造化
    ~~~~~~~~~~~~~~

    1. **ファイルの分割**：用途別にCSSファイルを分割
    2. **コメントの活用**：セクションや複雑な部分に説明を追加
    3. **一貫した命名規則**：BEMやSMACSSなどの手法を採用
    4. **インデントと整形**：読みやすいコードスタイルを維持

    .. code-block:: text

    /* ===========================================
    ヘッダーコンポーネント
    =========================================== */
        
        .header {
            /* レイアウト */
            position: sticky;
            top: 0;
            z-index: 1000;
            
            /* 見た目 */
            background: var(--color-primary);
            box-shadow: var(--shadow-sm);
        }
        
        .header__container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: var(--container-max-width);
            margin: 0 auto;
            padding: var(--spacing-md) var(--spacing-lg);
        }
        
        /* ===========================================
            レスポンシブ対応
            =========================================== */
        
        @media (max-width: 768px) {
            .header__container {
                padding: var(--spacing-sm) var(--spacing-md);
            }
        }

    メンテナンス性の向上
    ~~~~~~~~~~~~~~~~~~~~

    .. code-block:: text

        /* 設定ファイル（variables.css） */
        :root {
            /* カラーシステム */
            --color-primary: #007bff;
            --color-primary-dark: #0056b3;
            --color-primary-light: #66b3ff;
            
            /* タイポグラフィ */
            --font-family-primary: 'Helvetica Neue', Arial, sans-serif;
            --font-size-base: 16px;
            --font-size-large: 18px;
            --font-size-small: 14px;
            
            /* スペーシング */
            --spacing-xs: 4px;
            --spacing-sm: 8px;
            --spacing-md: 16px;
            --spacing-lg: 24px;
            --spacing-xl: 32px;
            
            /* シャドウ */
            --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.1);
            --shadow-md: 0 4px 8px rgba(0, 0, 0, 0.12);
            --shadow-lg: 0 8px 16px rgba(0, 0, 0, 0.15);
        }

    パフォーマンスの考慮
    ~~~~~~~~~~~~~~~~~~~~

    .. code-block:: text

        /*