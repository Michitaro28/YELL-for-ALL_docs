# HTML 基本解説ガイド

## HTMLとは

HTML（HyperText Markup Language）は、Webページを作成するためのマークアップ言語です。「マークアップ」とは、文書に構造や意味を付与することを指します。HTMLを使用することで、テキストに見出し、段落、リンク、画像などの要素を追加し、Webブラウザで表示できる形式にできます。

## HTMLの基本構造

すべてのHTMLドキュメントは、以下の基本構造を持ちます：

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ページタイトル</title>
</head>
<body>
    <h1>メインの見出し</h1>
    <p>ここに本文を書きます。</p>
</body>
</html>
```

### 基本構造の解説

| 要素 | 説明 |
|------|------|
| `<!DOCTYPE html>` | HTML5であることを宣言 |
| `<html>` | HTML文書全体を囲む最上位要素 |
| `<head>` | ページの設定情報を記述（ブラウザには表示されない） |
| `<body>` | ページの内容を記述（ブラウザに表示される部分） |

## タグとは

HTMLでは「タグ」を使って要素を定義します。多くのタグは開始タグと終了タグのペアで構成されます。

```html
<タグ名>内容</タグ名>
```

例：
```html
<h1>これは見出しです</h1>
<p>これは段落です</p>
```

## 主要なHTMLタグ

### 見出しタグ

見出しは`<h1>`から`<h6>`までの6段階があります：

```html
<h1>最重要な見出し</h1>
<h2>重要な見出し</h2>
<h3>中程度の見出し</h3>
<h4>小見出し</h4>
<h5>より小さな見出し</h5>
<h6>最小の見出し</h6>
```

### 段落とテキスト

```html
<p>これは段落です。段落は文章をまとまりごとに分けるために使用します。</p>
<p>これは別の段落です。</p>

<strong>太字で強調</strong>
<em>斜体で強調</em>
<br> <!-- 改行タグ -->
```

### リスト

#### 順序なしリスト（箇条書き）
```html
<ul>
    <li>項目1</li>
    <li>項目2</li>
    <li>項目3</li>
</ul>
```

#### 順序付きリスト（番号付き）
```html
<ol>
    <li>最初の項目</li>
    <li>2番目の項目</li>
    <li>3番目の項目</li>
</ol>
```

### リンク

```html
<a href="https://www.example.com">外部サイトへのリンク</a>
<a href="page2.html">同じサイト内のページへのリンク</a>
<a href="#section1">同じページ内の特定の場所へのリンク</a>
```

### 画像

```html
<img src="image.jpg" alt="画像の説明">
```

## 属性について

HTMLタグには「属性」を追加できます。属性はタグに追加情報を提供します。

```html
<タグ名 属性名="属性値">内容</タグ名>
```

### よく使用される属性

| 属性 | 説明 | 例 |
|------|------|-----|
| `id` | 要素に一意の識別子を付与 | `<div id="header">` |
| `class` | 要素にクラス名を付与（CSS用） | `<p class="intro">` |
| `src` | 画像のファイルパス | `<img src="photo.jpg">` |
| `href` | リンク先のURL | `<a href="https://example.com">` |
| `alt` | 画像の代替テキスト | `<img alt="美しい風景">` |

## テーブル（表）

```html
<table>
    <thead>
        <tr>
            <th>名前</th>
            <th>年齢</th>
            <th>職業</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>菅原道太郎</td>
            <td>37</td>
            <td>エンジニア</td>
        </tr>
        <tr>
            <td>鹿山優月</td>
            <td>24</td>
            <td>デザイナー</td>
        </tr>
    </tbody>
</table>
```

### テーブル要素の説明

| 要素 | 説明 |
|------|------|
| `<table>` | テーブル全体を囲む |
| `<thead>` | テーブルのヘッダー部分 |
| `<tbody>` | テーブルの本体部分 |
| `<tr>` | テーブルの行 |
| `<th>` | ヘッダーセル |
| `<td>` | データセル |

## フォーム

ユーザーからの入力を受け取るためのフォーム要素：

```html
<form action="/submit" method="POST">
    <label for="name">名前:</label>
    <input type="text" id="name" name="name" required>
    
    <label for="email">メールアドレス:</label>
    <input type="email" id="email" name="email" required>
    
    <label for="message">メッセージ:</label>
    <textarea id="message" name="message" rows="4" cols="50"></textarea>
    
    <input type="submit" value="送信">
</form>
```

### 主要なinput type

| type | 説明 | 例 |
|------|------|-----|
| `text` | 一行のテキスト入力 | `<input type="text">` |
| `email` | メールアドレス入力 | `<input type="email">` |
| `password` | パスワード入力 | `<input type="password">` |
| `number` | 数値入力 | `<input type="number">` |
| `submit` | 送信ボタン | `<input type="submit">` |

## セマンティックHTML

HTML5では、文書の構造をより明確にするためのセマンティック要素が追加されました：

```html
<header>
    <h1>サイトタイトル</h1>
    <nav>
        <ul>
            <li><a href="#home">ホーム</a></li>
            <li><a href="#about">会社概要</a></li>
            <li><a href="#contact">お問い合わせ</a></li>
        </ul>
    </nav>
</header>

<main>
    <article>
        <h2>記事タイトル</h2>
        <p>記事の内容...</p>
    </article>
    
    <aside>
        <h3>関連情報</h3>
        <p>サイドバーの内容...</p>
    </aside>
</main>

<footer>
    <p>&copy; 2025 会社名</p>
</footer>
```

### セマンティック要素の説明

| 要素 | 説明 |
|------|------|
| `<header>` | ページやセクションのヘッダー |
| `<nav>` | ナビゲーションリンク |
| `<main>` | ページのメインコンテンツ |
| `<article>` | 独立したコンテンツ |
| `<section>` | 文書のセクション |
| `<aside>` | サイドバーや補足情報 |
| `<footer>` | ページやセクションのフッター |

## HTMLの記述のベストプラクティス

### 1. 適切なインデント
```html
<div>
    <h1>見出し</h1>
    <p>段落</p>
    <ul>
        <li>リスト項目1</li>
        <li>リスト項目2</li>
    </ul>
</div>
```

### 2. 適切な要素の使用
- 見出しには`<h1>`〜`<h6>`を使用
- 段落には`<p>`を使用
- リストには`<ul>`、`<ol>`、`<li>`を使用

### 3. 属性の適切な使用
```html
<!-- 良い例 -->
<img src="photo.jpg" alt="教室の写真">
<a href="https://example.com" title="外部サイトへ">リンク</a>

<!-- 悪い例 -->
<img src="photo.jpg">
<a href="https://example.com">リンク</a>
```

## 簡単なWebページの作成例

以下は、学んだ要素を組み合わせた簡単なWebページの例です：

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>私のWebサイト</title>
</head>
<body>
    <header>
        <h1>YELL for ALLのWebサイト</h1>
        <nav>
            <ul>
                <li><a href="#about">自己紹介</a></li>
                <li><a href="#skills">スキル</a></li>
                <li><a href="#contact">お問い合わせ</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section id="about">
            <h2>自己紹介</h2>
            <p>こんにちは！私は菅原道太郎です。<strong>Web開発</strong>に興味があります。</p>
            <img src="profile.jpg" alt="菅原道太郎のプロフィール写真">
        </section>
        
        <section id="skills">
            <h2>スキル</h2>
            <ul>
                <li>HTML</li>
                <li>CSS</li>
                <li>JavaScript</li>
                <li>Python</li>
            </ul>
        </section>
        
        <section id="contact">
            <h2>お問い合わせ</h2>
            <form>
                <label for="name">お名前:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">メールアドレス:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">メッセージ:</label>
                <textarea id="message" name="message"></textarea>
                
                <input type="submit" value="送信">
            </form>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2025 YELL for ALL. All rights reserved.</p>
    </footer>
</body>
</html>
```

