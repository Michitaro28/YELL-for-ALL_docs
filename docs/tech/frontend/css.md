# CSS 基本解説ガイド


## CSSとは

CSS（Cascading Style Sheets）は、HTMLで作成された文書の見た目やレイアウトを制御するスタイルシート言語です。HTMLが文書の構造を定義するのに対し、CSSは文書の外観（色、フォント、配置など）を定義します。

## CSSの基本構文

CSSは「セレクタ」と「宣言ブロック」で構成されます：

```text
セレクタ {
    プロパティ: 値;
    プロパティ: 値;
}
```

例：
```css
h1 {
    color: blue;
    font-size: 24px;
}
```

### 構文の説明

| 要素 | 説明 |
|------|------|
| セレクタ | スタイルを適用するHTML要素を指定 |
| プロパティ | 変更したいスタイルの種類 |
| 値 | プロパティに設定する具体的な内容 |
| 宣言 | プロパティと値のペア |
| 宣言ブロック | `{}`で囲まれた宣言の集まり |

## CSSをHTMLに適用する方法

### 1. 外部スタイルシート（推奨）

**style.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
}

h1 {
    color: navy;
}
```

**index.html**
```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>CSSの例</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>見出し</h1>
    <p>段落</p>
</body>
</html>
```

### 2. 内部スタイルシート

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>CSSの例</title>
    <style>
        body {
            background-color: #f0f0f0;
        }
        h1 {
            color: red;
        }
    </style>
</head>
<body>
    <h1>見出し</h1>
</body>
</html>
```

### 3. インラインスタイル

```html
<h1 style="color: green; font-size: 30px;">見出し</h1>
```

### 適用方法の比較

| 方法 | 利点 | 欠点 | 使用場面 |
|------|------|------|----------|
| 外部スタイルシート | 複数ページで共有可能、保守性が高い | ファイル数が増える | 一般的なWebサイト |
| 内部スタイルシート | 1つのファイルで完結 | 再利用できない | 単一ページ、テスト |
| インラインスタイル | 要素に直接適用 | 保守性が悪い | 緊急の修正、特殊な場合 |

## セレクタの種類

### 基本セレクタ

#### 要素セレクタ
```css
/* すべてのp要素に適用 */
p {
    color: black;
    line-height: 1.6;
}

/* すべてのh1要素に適用 */
h1 {
    font-size: 2em;
}
```

#### クラスセレクタ
```css
/* class="intro"の要素に適用 */
.intro {
    font-weight: bold;
    color: blue;
}

/* class="warning"の要素に適用 */
.warning {
    background-color: yellow;
    padding: 10px;
}
```

```html
<p class="intro">これは導入部分です。</p>
<div class="warning">注意事項</div>
```

#### IDセレクタ
```css
/* id="header"の要素に適用 */
#header {
    background-color: navy;
    color: white;
    padding: 20px;
}

/* id="main-content"の要素に適用 */
#main-content {
    margin: 20px;
}
```

```html
<header id="header">ヘッダー</header>
<main id="main-content">メインコンテンツ</main>
```

### 組み合わせセレクタ

#### 子孫セレクタ
```css
/* article内のすべてのp要素 */
article p {
    margin-bottom: 15px;
}

/* nav内のa要素 */
nav a {
    text-decoration: none;
    color: #333;
}
```

#### 子セレクタ
```css
/* ulの直接の子であるli要素のみ */
ul > li {
    list-style-type: square;
}
```

#### 隣接兄弟セレクタ
```css
/* h1の直後にあるp要素 */
h1 + p {
    font-weight: bold;
}
```

### 疑似クラス

```css
/* リンクの状態 */
a:link { color: blue; }        /* 未訪問のリンク */
a:visited { color: purple; }   /* 訪問済みのリンク */
a:hover { color: red; }        /* マウスオーバー時 */
a:active { color: orange; }    /* クリック時 */

/* その他の疑似クラス */
input:focus {                  /* フォーカス時 */
    border: 2px solid blue;
}

li:first-child {              /* 最初の子要素 */
    font-weight: bold;
}

tr:nth-child(even) {          /* 偶数番目の要素 */
    background-color: #f2f2f2;
}
```

## 主要なCSSプロパティ

### テキスト関連

```css
.text-example {
    /* フォント */
    font-family: "Arial", "Helvetica", sans-serif;
    font-size: 16px;
    font-weight: bold;        /* normal, bold, 100-900 */
    font-style: italic;       /* normal, italic, oblique */
    
    /* テキスト */
    color: #333333;
    text-align: center;       /* left, center, right, justify */
    text-decoration: underline; /* none, underline, overline, line-through */
    text-transform: uppercase; /* none, uppercase, lowercase, capitalize */
    line-height: 1.5;
    letter-spacing: 1px;
    word-spacing: 2px;
}
```

### 背景関連

```css
.background-example {
    background-color: #f0f0f0;
    background-image: url('image.jpg');
    background-repeat: no-repeat;    /* repeat, repeat-x, repeat-y, no-repeat */
    background-position: center center; /* top, center, bottom, left, right, % */
    background-size: cover;          /* auto, cover, contain, %, px */
    background-attachment: fixed;    /* scroll, fixed */
}

/* 短縮記法 */
.background-shorthand {
    background: #f0f0f0 url('image.jpg') no-repeat center center / cover;
}
```

### ボックスモデル

```css
.box-example {
    /* サイズ */
    width: 300px;
    height: 200px;
    
    /* パディング（内側の余白） */
    padding: 20px;              /* 上下左右すべて */
    padding: 10px 20px;         /* 上下10px, 左右20px */
    padding: 5px 10px 15px 20px; /* 上5px, 右10px, 下15px, 左20px */
    
    /* ボーダー */
    border: 2px solid #333;
    border-width: 2px;
    border-style: solid;        /* solid, dashed, dotted, none */
    border-color: #333;
    border-radius: 10px;        /* 角丸 */
    
    /* マージン（外側の余白） */
    margin: 20px;
    margin: 10px auto;          /* 上下10px, 左右中央揃え */
}
```

### ボックスモデルの図解

```
┌─────────────────────────────────────┐
│           Margin (外側余白)           │
│  ┌─────────────────────────────────┐  │
│  │        Border (境界線)         │  │
│  │  ┌─────────────────────────────┐ │  │
│  │  │     Padding (内側余白)     │ │  │
│  │  │  ┌─────────────────────────┐ │ │  │
│  │  │  │       Content        │ │ │  │
│  │  │  │      (コンテンツ)       │ │ │  │
│  │  │  └─────────────────────────┘ │ │  │
│  │  └─────────────────────────────┘ │  │
│  └─────────────────────────────────┘  │
└─────────────────────────────────────┘
```

### 色の指定方法

| 指定方法 | 例 | 説明 |
|----------|-----|------|
| 色名 | `red`, `blue`, `green` | 基本的な色名 |
| 16進数 | `#ff0000`, `#f00` | RGB値を16進数で表現 |
| RGB | `rgb(255, 0, 0)` | 赤緑青の値を0-255で指定 |
| RGBA | `rgba(255, 0, 0, 0.5)` | RGBに透明度を追加 |
| HSL | `hsl(0, 100%, 50%)` | 色相・彩度・明度で指定 |
| HSLA | `hsla(0, 100%, 50%, 0.5)` | HSLに透明度を追加 |

## レイアウト

### Display プロパティ

```css
.display-examples {
    /* ブロック要素（幅いっぱい、縦に積み重なる） */
    display: block;
    
    /* インライン要素（内容の幅のみ、横に並ぶ） */
    display: inline;
    
    /* インラインブロック要素（横に並ぶが、幅・高さ指定可能） */
    display: inline-block;
    
    /* 非表示 */
    display: none;
}
```

### Position プロパティ

```css
.position-examples {
    /* 通常の配置 */
    position: static;
    
    /* 相対位置（元の位置からの相対位置） */
    position: relative;
    top: 10px;
    left: 20px;
    
    /* 絶対位置（最寄りのpositioned要素からの絶対位置） */
    position: absolute;
    top: 0;
    right: 0;
    
    /* 固定位置（ビューポートからの固定位置） */
    position: fixed;
    bottom: 20px;
    right: 20px;
    
    /* スティッキー位置（スクロール時に固定） */
    position: sticky;
    top: 0;
}
```

### Float プロパティ

```css
.float-example {
    float: left;               /* 左に寄せる */
    float: right;              /* 右に寄せる */
    float: none;               /* フロートしない */
}

.clearfix {
    clear: both;               /* フロートをクリア */
}
```

## Flexbox レイアウト

### Flex コンテナ

```css
.flex-container {
    display: flex;
    
    /* メイン軸の方向 */
    flex-direction: row;        /* row, row-reverse, column, column-reverse */
    
    /* 折り返し */
    flex-wrap: nowrap;          /* nowrap, wrap, wrap-reverse */
    
    /* メイン軸の配置 */
    justify-content: flex-start; /* flex-start, flex-end, center, space-between, space-around, space-evenly */
    
    /* クロス軸の配置 */
    align-items: stretch;       /* stretch, flex-start, flex-end, center, baseline */
    
    /* 複数行の配置 */
    align-content: stretch;     /* stretch, flex-start, flex-end, center, space-between, space-around */
    
    /* ギャップ */
    gap: 20px;                  /* アイテム間の余白 */
}
```

### Flex アイテム

```css
.flex-item {
    /* 拡張比率 */
    flex-grow: 1;
    
    /* 縮小比率 */
    flex-shrink: 1;
    
    /* ベースサイズ */
    flex-basis: auto;
    
    /* 短縮記法 */
    flex: 1 1 auto;             /* grow shrink basis */
    
    /* 個別の配置 */
    align-self: center;         /* auto, flex-start, flex-end, center, baseline, stretch */
}
```

### Flexbox の実用例

```css
/* ヘッダーのナビゲーション */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
}

/* カードレイアウト */
.card-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.card {
    flex: 1 1 300px;            /* 最小幅300px、均等拡張 */
    padding: 20px;
    border: 1px solid #ddd;
}

/* 中央配置 */
.center-content {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}
```

## Grid レイアウト

### Grid コンテナ

```css
.grid-container {
    display: grid;
    
    /* グリッドの定義 */
    grid-template-columns: 1fr 2fr 1fr;      /* 3列（1:2:1の比率） */
    grid-template-rows: 100px auto 50px;     /* 3行 */
    
    /* または具体的なサイズ */
    grid-template-columns: 200px 1fr 200px;  /* 固定幅と可変幅の組み合わせ */
    grid-template-rows: repeat(3, 1fr);      /* 3行を均等分割 */
    
    /* ギャップ */
    gap: 20px;                               /* 行・列のギャップ */
    row-gap: 10px;                          /* 行のギャップ */
    column-gap: 20px;                       /* 列のギャップ */
}
```

### Grid アイテム

```css
.grid-item {
    /* グリッド位置の指定 */
    grid-column: 1 / 3;         /* 1列目から3列目まで */
    grid-row: 2 / 4;            /* 2行目から4行目まで */
    
    /* または */
    grid-column-start: 1;
    grid-column-end: 3;
    grid-row-start: 2;
    grid-row-end: 4;
    
    /* スパン記法 */
    grid-column: span 2;        /* 2列分 */
    grid-row: span 3;           /* 3行分 */
}
```

### Grid エリア

```css
.grid-layout {
    display: grid;
    grid-template-areas: 
        "header header header"
        "sidebar main main"
        "footer footer footer";
    grid-template-columns: 200px 1fr 1fr;
    grid-template-rows: 100px 1fr 50px;
    gap: 20px;
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.footer { grid-area: footer; }
```

## レスポンシブデザイン

### メディアクエリ

```css
/* 基本スタイル（モバイルファースト） */
.container {
    width: 100%;
    padding: 10px;
}

/* タブレット用 */
@media screen and (min-width: 768px) {
    .container {
        width: 750px;
        margin: 0 auto;
        padding: 20px;
    }
}

/* デスクトップ用 */
@media screen and (min-width: 1024px) {
    .container {
        width: 1000px;
        padding: 30px;
    }
}

/* 印刷用 */
@media print {
    .no-print {
        display: none;
    }
    
    body {
        font-size: 12pt;
        color: black;
    }
}
```

### よく使用されるブレークポイント

| デバイス | 幅 | メディアクエリ |
|----------|-----|----------------|
| スマートフォン | ~767px | `@media (max-width: 767px)` |
| タブレット | 768px~1023px | `@media (min-width: 768px) and (max-width: 1023px)` |
| デスクトップ | 1024px~ | `@media (min-width: 1024px)` |

### レスポンシブ画像

```css
.responsive-image {
    max-width: 100%;
    height: auto;
}

/* アスペクト比を保持 */
.image-container {
    position: relative;
    width: 100%;
    padding-bottom: 56.25%; /* 16:9のアスペクト比 */
}

.image-container img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
}
```

## アニメーション

### Transition

```css
.transition-example {
    background-color: blue;
    transition: background-color 0.3s ease;
}

.transition-example:hover {
    background-color: red;
}

/* 複数のプロパティ */
.multi-transition {
    width: 100px;
    height: 100px;
    background-color: blue;
    transition: width 0.3s ease, height 0.3s ease, background-color 0.5s linear;
}

.multi-transition:hover {
    width: 200px;
    height: 200px;
    background-color: red;
}
```

### Animation

```css
/* キーフレームの定義 */
@keyframes slideIn {
    0% {
        transform: translateX(-100%);
        opacity: 0;
    }
    100% {
        transform: translateX(0);
        opacity: 1;
    }
}

@keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
        transform: translateY(0);
    }
    40% {
        transform: translateY(-30px);
    }
    60% {
        transform: translateY(-15px);
    }
}

/* アニメーションの適用 */
.slide-in {
    animation: slideIn 0.5s ease-out;
}

.bounce-element {
    animation: bounce 2s infinite;
}

/* アニメーションの詳細設定 */
.complex-animation {
    animation-name: slideIn;
    animation-duration: 1s;
    animation-timing-function: ease-in-out;
    animation-delay: 0.5s;
    animation-iteration-count: 2;
    animation-direction: alternate;
    animation-fill-mode: forwards;
}
```

## 実践的なWebページの例

以下は、学んだ技術を組み合わせた実践的なWebページの例です：

### HTML
```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>モダンWebサイト</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header class="header">
        <nav class="navbar">
            <div class="logo">MyWebsite</div>
            <ul class="nav-links">
                <li><a href="#home">ホーム</a></li>
                <li><a href="#about">会社概要</a></li>
                <li><a href="#services">サービス</a></li>
                <li><a href="#contact">お問い合わせ</a></li>
            </ul>
        </nav>
    </header>
    
    <main class="main-content">
        <section class="hero">
            <h1>革新的なソリューション</h1>
            <p>私たちがあなたのビジネスを次のレベルへ導きます</p>
            <button class="cta-button">詳しく見る</button>
        </section>
        
        <section class="services">
            <h2>サービス</h2>
            <div class="service-grid">
                <div class="service-card">
                    <h3>Web開発</h3>
                    <p>モダンで高性能なWebサイトを構築します</p>
                </div>
                <div class="service-card">
                    <h3>デザイン</h3>
                    <p>ユーザー体験を重視したデザインを提供します</p>
                </div>
                <div class="service-card">
                    <h3>コンサルティング</h3>
                    <p>技術的な課題解決をサポートします</p>
                </div>
            </div>
        </section>
    </main>
    
    <footer class="footer">
        <p>&copy; 2024 MyWebsite. All rights reserved.</p>
    </footer>
</body>
</html>
```

### CSS
```css
/* リセットとベーススタイル */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    color: #333;
}

/* ヘッダー */
.header {
    background-color: #2c3e50;
    color: white;
    padding: 1rem 0;
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1000;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

.logo {
    font-size: 1.5rem;
    font-weight: bold;
}

.nav-links {
    display: flex;
    list-style: none;
    gap: 2rem;
}

.nav-links a {
    color: white;
    text-decoration: none;
    transition: color 0.3s ease;
}

.nav-links a:hover {
    color: #3498db;
}

/* メインコンテンツ */
.main-content {
    margin-top: 80px;
}

/* ヒーローセクション */
.hero {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    text-align: center;
    padding: 8rem 2rem;
}

.hero h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
    animation: slideIn 1s ease-out;
}

.hero p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
    animation: slideIn 1s ease-out 0.3s both;
}

.cta-button {
    background-color: #e74c3c;
    color: white;
    border: none;
    padding: 1rem 2rem;
    font-size: 1.1rem;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0.3s ease;
    animation: slideIn 1s ease-out 0.6s both;
}

.cta-button:hover {
    background-color: #c0392b;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

/* サービスセクション */
.services {
    padding: 6rem 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.services h2 {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 3rem;
    color: #2c3e50;
}

.service-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}

.service-card {
    background: white;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.service-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
}

.service-card h3 {
    color: #2c3e50;
    margin-bottom: 1rem;
    font-size: 1.5rem;
}

.service-card p {
    color: #666;
    line-height: 1.8;
}

/* フッター */
.footer {
    background-color: #34495e;
    color: white;
    text-align: center;
    padding: 2rem;
}

/* アニメーション */
@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* レスポンシブデザイン */
@media (max-width: 768px) {
    .navbar {
        flex-direction: column;
        gap: 1rem;
    }
    
    .nav-links {
        gap: 1rem;
    }
    
    .hero h1 {
        font-size: 2rem;
    }
    
    .hero p {
        font-size: 1rem;
    }
    
    .services {
        padding: 4rem 1rem;
    }
    
    .service-grid {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 480px) {
    .hero {
        padding: 4rem 1rem;
    }
    
    .hero h1 {
        font-size: 1.5rem;
    }
    
    .navbar {
        padding: 0 1rem;
    }
}
```