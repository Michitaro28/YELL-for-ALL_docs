
# CSS tips

## CSSのベストプラクティス

### 1. 命名規則

```css
/* BEM記法の例 */
.card { }                    /* Block */
.card__title { }             /* Element */
.card--featured { }          /* Modifier */

/* 良い例 */
.navigation-menu { }
.btn-primary { }
.form-input { }

/* 悪い例 */
.nav1 { }
.button { }
.red { }
```

### 2. 整理とコメント

```css
/* =================================
   リセットとベーススタイル
================================= */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* =================================
   レイアウト
================================= */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}

/* =================================
   コンポーネント
================================= */
.button {
    /* ベーススタイル */
    display: inline-block;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.button--primary {
    background-color: #007bff;
    color: white;
}

.button--secondary {
    background-color: #6c757d;
    color: white;
}
```

### 3. パフォーマンスの最適化

```css
/* 効率的なセレクタ */
.navigation a { }            /* 良い */
.navigation > ul > li > a { } /* 避ける */

/* will-changeプロパティでアニメーション最適化 */
.animated-element {
    will-change: transform;
}

/* 不要なreflowを避ける */
.optimized-animation {
    transform: translateX(100px);    /* 良い */
    /* left: 100px; */               /* パフォーマンスに影響 */
}
```

## よく使用されるCSSテクニック

### 1. 中央配置の方法

```css
/* Flexboxを使用した中央配置 */
.flex-center {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

/* Gridを使用した中央配置 */
.grid-center {
    display: grid;
    place-items: center;
    min-height: 100vh;
}

/* 絶対位置での中央配置 */
.absolute-center {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

/* マージンを使用した水平中央配置 */
.margin-center {
    width: 300px;
    margin: 0 auto;
}
```

### 2. クリアフィックス（Floatのクリア）

```css
/* モダンなクリアフィックス */
.clearfix::after {
    content: "";
    display: table;
    clear: both;
}

/* レガシーブラウザ対応 */
.clearfix {
    zoom: 1; /* IE6/7用 */
}

.clearfix::before,
.clearfix::after {
    content: "";
    display: table;
}

.clearfix::after {
    clear: both;
}
```

### 3. レスポンシブ画像とメディア

```css
/* 基本的なレスポンシブ画像 */
.responsive-img {
    max-width: 100%;
    height: auto;
}

/* アスペクト比を維持する画像コンテナ */
.aspect-ratio-container {
    position: relative;
    width: 100%;
    padding-bottom: 56.25%; /* 16:9比率 */
    overflow: hidden;
}

.aspect-ratio-container img,
.aspect-ratio-container video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* 複数のアスペクト比 */
.ratio-16-9 { padding-bottom: 56.25%; }
.ratio-4-3 { padding-bottom: 75%; }
.ratio-1-1 { padding-bottom: 100%; }
```

### 4. カスタムプロパティ（CSS変数）

```css
/* CSS変数の定義 */
:root {
    --primary-color: #007bff;
    --secondary-color: #6c757d;
    --success-color: #28a745;
    --danger-color: #dc3545;
    
    --font-size-small: 0.875rem;
    --font-size-base: 1rem;
    --font-size-large: 1.25rem;
    
    --spacing-xs: 0.25rem;
    --spacing-sm: 0.5rem;
    --spacing-md: 1rem;
    --spacing-lg: 2rem;
    --spacing-xl: 3rem;
    
    --border-radius: 0.375rem;
    --box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12);
}

/* CSS変数の使用 */
.button {
    background-color: var(--primary-color);
    font-size: var(--font-size-base);
    padding: var(--spacing-sm) var(--spacing-md);
    border-radius: var(--border-radius);
    box-shadow: var(--box-shadow);
}

/* ダークモード対応 */
[data-theme="dark"] {
    --primary-color: #0d6efd;
    --background-color: #212529;
    --text-color: #ffffff;
}

body {
    background-color: var(--background-color, #ffffff);
    color: var(--text-color, #000000);
}
```

### 5. グラデーション

```css
/* 線形グラデーション */
.linear-gradient {
    background: linear-gradient(to right, #667eea, #764ba2);
    background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
    background: linear-gradient(to bottom, #667eea 0%, #764ba2 100%);
}

/* 放射グラデーション */
.radial-gradient {
    background: radial-gradient(circle, #667eea, #764ba2);
    background: radial-gradient(ellipse at center, #ff6b6b 0%, #4ecdc4 100%);
}

/* 複数のグラデーション */
.multiple-gradients {
    background: 
        linear-gradient(45deg, transparent 30%, rgba(255, 255, 255, 0.5) 30%, rgba(255, 255, 255, 0.5) 70%, transparent 70%),
        linear-gradient(-45deg, transparent 30%, rgba(0, 0, 0, 0.1) 30%, rgba(0, 0, 0, 0.1) 70%, transparent 70%),
        #667eea;
}
```

### 6. シャドウとエフェクト

```css
/* ボックスシャドウ */
.shadow-examples {
    /* 基本的なシャドウ */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    
    /* 複数のシャドウ */
    box-shadow: 
        0 1px 3px rgba(0, 0, 0, 0.12),
        0 1px 2px rgba(0, 0, 0, 0.24);
    
    /* 内側のシャドウ */
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
    
    /* 色付きシャドウ */
    box-shadow: 0 4px 20px rgba(76, 175, 80, 0.3);
}

/* テキストシャドウ */
.text-shadow-examples {
    /* 基本的なテキストシャドウ */
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
    
    /* 複数のテキストシャドウ */
    text-shadow: 
        1px 1px 0px #ccc,
        2px 2px 0px #c9c9c9,
        3px 3px 0px #bbb;
    
    /* グロー効果 */
    text-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
}

/* フィルター効果 */
.filter-examples {
    /* ぼかし */
    filter: blur(5px);
    
    /* 明度調整 */
    filter: brightness(1.2);
    
    /* コントラスト調整 */
    filter: contrast(1.5);
    
    /* グレースケール */
    filter: grayscale(100%);
    
    /* 色相回転 */
    filter: hue-rotate(90deg);
    
    /* 複数のフィルター */
    filter: brightness(1.1) contrast(1.2) saturate(1.3);
}
```

## フォームのスタイリング

```css
/* 基本的なフォームスタイル */
.form-container {
    max-width: 500px;
    margin: 0 auto;
    padding: 2rem;
    background: white;
    border-radius: var(--border-radius);
    box-shadow: var(--box-shadow);
}

.form-group {
    margin-bottom: var(--spacing-md);
}

.form-label {
    display: block;
    margin-bottom: var(--spacing-xs);
    font-weight: 600;
    color: var(--text-color);
}

.form-input,
.form-textarea,
.form-select {
    width: 100%;
    padding: var(--spacing-sm);
    border: 1px solid #ddd;
    border-radius: var(--border-radius);
    font-size: var(--font-size-base);
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.form-input:focus,
.form-textarea:focus,
.form-select:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.25);
}

/* カスタムチェックボックス */
.custom-checkbox {
    position: relative;
    display: inline-block;
    padding-left: 2rem;
    cursor: pointer;
}

.custom-checkbox input[type="checkbox"] {
    position: absolute;
    opacity: 0;
}

.custom-checkbox .checkmark {
    position: absolute;
    top: 0;
    left: 0;
    height: 1.25rem;
    width: 1.25rem;
    background-color: #eee;
    border-radius: 3px;
    transition: all 0.3s ease;
}

.custom-checkbox input[type="checkbox"]:checked ~ .checkmark {
    background-color: var(--primary-color);
}

.custom-checkbox .checkmark::after {
    content: "";
    position: absolute;
    display: none;
    left: 0.4rem;
    top: 0.2rem;
    width: 0.3rem;
    height: 0.6rem;
    border: solid white;
    border-width: 0 2px 2px 0;
    transform: rotate(45deg);
}

.custom-checkbox input[type="checkbox"]:checked ~ .checkmark::after {
    display: block;
}
```

## デバッグとトラブルシューティング

### よくある問題と解決法

| 問題 | 原因 | 解決法 |
|------|------|--------|
| 要素が表示されない | `display: none`が設定されている | `display`プロパティを確認 |
| レイアウトが崩れる | ボックスモデルの理解不足 | `box-sizing: border-box`を使用 |
| フロートがクリアされない | `clear`プロパティが不足 | クリアフィックスを適用 |
| 中央配置できない | 要素の`display`プロパティが不適切 | FlexboxまたはGridを使用 |
| z-indexが効かない | `position`が`static`のまま | `position: relative`等を設定 |

### デバッグ用CSS

```css
/* 要素の境界を可視化 */
* {
    outline: 1px solid red;
}

/* 特定の要素をハイライト */
.debug {
    background-color: rgba(255, 0, 0, 0.3) !important;
    border: 2px solid red !important;
}

/* グリッドの可視化 */
.debug-grid {
    background-image: 
        linear-gradient(rgba(255, 0, 0, 0.1) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 0, 0, 0.1) 1px, transparent 1px);
    background-size: 20px 20px;
}
```

## パフォーマンス最適化のヒント

### 1. CSSセレクタの最適化

```css
/* 効率的なセレクタ */
.navigation-link { }              /* 良い */
#header .navigation ul li a { }   /* 避ける（過度に具体的） */

/* クラスを使用 */
.active-link { }                  /* 良い */
a:nth-child(3) { }               /* 避ける（計算コストが高い） */
```

### 2. アニメーション最適化

```css
/* GPU アクセラレーションを利用 */
.optimized-animation {
    transform: translateZ(0);     /* ハードウェアアクセラレーション */
    will-change: transform;       /* ブラウザに変更予定を通知 */
}

/* 避けるべきプロパティのアニメーション */
.bad-animation {
    /* width: 100px;  */          /* レイアウトの再計算が発生 */
    /* height: 100px; */          /* レイアウトの再計算が発生 */
}

/* 推奨されるプロパティのアニメーション */
.good-animation {
    transform: scale(1.1);        /* 合成レイヤーで処理 */
    opacity: 0.8;                /* 合成レイヤーで処理 */
}
```

### 3. CSSの読み込み最適化

```html
<!-- クリティカルCSSをインライン化 -->
<style>
    /* 重要なスタイルをここに記述 */
    body { font-family: Arial, sans-serif; }
    .header { background: #333; }
</style>

<!-- 非クリティカルCSSは非同期読み込み -->
<link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="styles.css"></noscript>
```

## 実用的なコンポーネントライブラリの作成

```css
/* =================================
   ユーティリティクラス
================================= */

/* マージン */
.m-0 { margin: 0; }
.m-1 { margin: 0.25rem; }
.m-2 { margin: 0.5rem; }
.m-3 { margin: 1rem; }
.m-4 { margin: 1.5rem; }
.m-5 { margin: 3rem; }

/* パディング */
.p-0 { padding: 0; }
.p-1 { padding: 0.25rem; }
.p-2 { padding: 0.5rem; }
.p-3 { padding: 1rem; }
.p-4 { padding: 1.5rem; }
.p-5 { padding: 3rem; }

/* テキスト配置 */
.text-left { text-align: left; }
.text-center { text-align: center; }
.text-right { text-align: right; }
.text-justify { text-align: justify; }

/* ディスプレイ */
.d-none { display: none; }
.d-block { display: block; }
.d-inline { display: inline; }
.d-inline-block { display: inline-block; }
.d-flex { display: flex; }
.d-grid { display: grid; }

/* Flexユーティリティ */
.justify-start { justify-content: flex-start; }
.justify-center { justify-content: center; }
.justify-end { justify-content: flex-end; }
.justify-between { justify-content: space-between; }
.justify-around { justify-content: space-around; }

.align-start { align-items: flex-start; }
.align-center { align-items: center; }
.align-end { align-items: flex-end; }
.align-stretch { align-items: stretch; }

/* カラーユーティリティ */
.text-primary { color: var(--primary-color); }
.text-secondary { color: var(--secondary-color); }
.text-success { color: var(--success-color); }
.text-danger { color: var(--danger-color); }

.bg-primary { background-color: var(--primary-color); }
.bg-secondary { background-color: var(--secondary-color); }
.bg-success { background-color: var(--success-color); }
.bg-danger { background-color: var(--danger-color); }

/* =================================
   コンポーネント
================================= */

/* ボタンコンポーネント */
.btn {
    display: inline-block;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.5;
    text-align: center;
    text-decoration: none;
    vertical-align: middle;
    cursor: pointer;
    border: 1px solid transparent;
    border-radius: 0.375rem;
    transition: all 0.15s ease-in-out;
}

.btn:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.btn-primary {
    color: white;
    background-color: var(--primary-color);
    border-color: var(--primary-color);
}

.btn-secondary {
    color: white;
    background-color: var(--secondary-color);
    border-color: var(--secondary-color);
}

.btn-outline-primary {
    color: var(--primary-color);
    background-color: transparent;
    border-color: var(--primary-color);
}

.btn-outline-primary:hover {
    color: white;
    background-color: var(--primary-color);
}

/* カードコンポーネント */
.card {
    background: white;
    border: 1px solid rgba(0, 0, 0, 0.125);
    border-radius: 0.375rem;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12);
    overflow: hidden;
}

.card-header {
    padding: 1rem;
    background-color: rgba(0, 0, 0, 0.03);
    border-bottom: 1px solid rgba(0, 0, 0, 0.125);
}

.card-body {
    padding: 1rem;
}

.card-footer {
    padding: 1rem;
    background-color: rgba(0, 0, 0, 0.03);
    border-top: 1px solid rgba(0, 0, 0, 0.125);
}

.card-title {
    margin-bottom: 0.5rem;
    font-size: 1.25rem;
    font-weight: 500;
}

.card-text {
    margin-bottom: 1rem;
    color: #6c757d;
}
```

## モダンCSS機能

### 1. CSS Grid の高度な使用

```css
/* 複雑なレイアウト */
.complex-grid {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    grid-template-rows: auto 1fr auto;
    grid-gap: 1rem;
    min-height: 100vh;
}

.header {
    grid-column: 1 / -1;
    grid-row: 1;
}

.sidebar {
    grid-column: 1 / 4;
    grid-row: 2;
}

.main {
    grid-column: 4 / -1;
    grid-row: 2;
}

.footer {
    grid-column: 1 / -1;
    grid-row: 3;
}

/* サブグリッド（将来の機能） */
.subgrid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
}

.subgrid-item {
    display: grid;
    grid-template-rows: subgrid;
    grid-row: span 3;
}
```

### 2. 新しい単位とプロパティ

```css
/* 新しいビューポート単位 */
.new-viewport-units {
    height: 100svh;    /* Small viewport height */
    height: 100lvh;    /* Large viewport height */
    height: 100dvh;    /* Dynamic viewport height */
    
    width: 100svi;     /* Small viewport inline */
    width: 100lvi;     /* Large viewport inline */
    width: 100dvi;     /* Dynamic viewport inline */
}

/* Container queries */
@container (min-width: 400px) {
    .card {
        display: flex;
        flex-direction: row;
    }
}

/* Logical properties */
.logical-properties {
    margin-block-start: 1rem;    /* margin-top in LTR */
    margin-block-end: 1rem;      /* margin-bottom in LTR */
    margin-inline-start: 1rem;   /* margin-left in LTR */
    margin-inline-end: 1rem;     /* margin-right in LTR */
    
    border-inline-start: 1px solid #ccc;  /* border-left in LTR */
    padding-block: 1rem;         /* padding-top and padding-bottom */
    padding-inline: 2rem;        /* padding-left and padding-right */
}
```

## 次のステップ

CSSの基本を理解したら、以下のトピックを学習することをお勧めします：

### 1. 高度なCSS技術
- CSS-in-JS（Styled Components、Emotion）
- CSS Modules
- PostCSS とプリプロセッサ（Sass、Less）
- CSS フレームワーク（Tailwind CSS、Bootstrap）

### 2. パフォーマンス最適化
- Critical CSS の抽出
- CSS の圧縮と最適化
- 使用されていない CSS の削除
- CSS の読み込み戦略

### 3. 現代的な開発手法
- デザインシステム の構築
- コンポーネントベース設計
- CSS アーキテクチャ（BEM、OOCSS、SMACSS）
- CSS の変数とカスタムプロパティの活用

### 4. アクセシビリティ
- セマンティックなスタイリング
- スクリーンリーダー対応
- キーボードナビゲーション
- 色のコントラスト比

### 5. 実践的なプロジェクト
- レスポンシブな Web アプリケーション
- アニメーション豊富なランディングページ
- ダークモード対応サイト
- Progressive Web App（PWA）のスタイリング

CSSは Web デザインの基盤となる重要な技術です。継続的な学習と実践を通じて、魅力的で機能的な Web サイトを作成するスキルを身につけてください。