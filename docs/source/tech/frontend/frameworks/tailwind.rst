    Tailwind CSS 完全ガイド
    ========================

    .. contents:: 目次
    :depth: 3
    :local:

    Tailwind CSSとは
    ================

    Tailwind CSSは、ユーティリティファーストのCSSフレームワークです。従来のCSSフレームワークとは異なり、予め定義されたコンポーネントではなく、小さなユーティリティクラスを組み合わせてUIを構築します。

    特徴
    ----

    * **ユーティリティファースト**: 単一の目的を持つクラスの組み合わせでスタイリング
    * **高いカスタマイズ性**: 設定ファイルで細かくカスタマイズ可能
    * **レスポンシブデザイン**: モバイルファーストでレスポンシブ対応
    * **パフォーマンス**: 未使用のCSSを自動的に削除（PurgeCSS統合）
    * **開発効率**: HTMLから離れることなくスタイリング可能

    従来のCSSとの比較
    -----------------

    **従来のCSS:**

    .. code-block:: css

    .card {
        padding: 1.5rem;
        margin-bottom: 1rem;
        background-color: white;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    **Tailwind CSS:**

    .. code-block:: html

    <div class="p-6 mb-4 bg-white rounded-lg shadow-md">
        <!-- カードの内容 -->
    </div>

    導入方法
    ========

    CDN経由での導入
    ---------------

    最も簡単な導入方法です。HTMLファイルの ``<head>`` セクションに以下を追加します：

    .. code-block:: html

    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tailwind CSS Example</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body>
        <h1 class="text-3xl font-bold underline">
        Hello Tailwind!
        </h1>
    </body>
    </html>

    .. note::
    CDN版は開発時のプロトタイピングには便利ですが、本番環境では推奨されません。

    npm/yarn経由での導入
    --------------------

    本格的な開発には、npm/yarnを使用した導入が推奨されます。

    **1. プロジェクトの初期化**

    .. code-block:: bash

    mkdir my-tailwind-project
    cd my-tailwind-project
    npm init -y

    **2. Tailwind CSSのインストール**

    .. code-block:: bash

    npm install -D tailwindcss
    npx tailwindcss init

    **3. 設定ファイルの編集**

    ``tailwind.config.js`` ファイルを編集します：

    .. code-block:: javascript

    /** @type {import('tailwindcss').Config} */
    module.exports = {
        content: ["./src/**/*.{html,js}"],
        theme: {
        extend: {},
        },
        plugins: [],
    }

    **4. CSSファイルの作成**

    ``src/input.css`` ファイルを作成し、以下を追加：

    .. code-block:: css

    @tailwind base;
    @tailwind components;
    @tailwind utilities;

    **5. ビルドコマンド**

    .. code-block:: bash

    npx tailwindcss -i ./src/input.css -o ./dist/output.css --watch

    PostCSS経由での導入
    -------------------

    より高度な設定が必要な場合は、PostCSSプラグインとして導入できます：

    .. code-block:: bash

    npm install -D tailwindcss postcss autoprefixer
    npx tailwindcss init -p

    基本的な使い方
    ==============

    ユーティリティクラスの基本
    --------------------------

    Tailwind CSSは数千のユーティリティクラスを提供します。各クラスは特定のCSSプロパティと値に対応しています。

    **スペーシング**

    .. code-block:: html

    <!-- パディング -->
    <div class="p-4">パディング16px</div>
    <div class="px-6 py-3">水平24px、垂直12px</div>
    
    <!-- マージン -->
    <div class="m-2">マージン8px</div>
    <div class="mt-8">上マージン32px</div>

    **色**

    .. code-block:: html

    <!-- 背景色 -->
    <div class="bg-blue-500">青い背景</div>
    <div class="bg-red-100">薄い赤の背景</div>
    
    <!-- テキスト色 -->
    <p class="text-gray-700">グレーのテキスト</p>
    <p class="text-green-600">緑のテキスト</p>

    **タイポグラフィ**

    .. code-block:: html

    <!-- フォントサイズ -->
    <h1 class="text-4xl">大きな見出し</h1>
    <p class="text-sm">小さなテキスト</p>
    
    <!-- フォントウェイト -->
    <p class="font-bold">太字</p>
    <p class="font-light">細字</p>
    
    <!-- テキスト配置 -->
    <p class="text-center">中央揃え</p>
    <p class="text-right">右揃え</p>

    レスポンシブデザイン
    --------------------

    Tailwind CSSはモバイルファーストのアプローチを採用しています。レスポンシブプレフィックスを使用してブレークポイント別のスタイルを適用できます。

    **ブレークポイント**

    * ``sm``: 640px以上
    * ``md``: 768px以上
    * ``lg``: 1024px以上
    * ``xl``: 1280px以上
    * ``2xl``: 1536px以上

    .. code-block:: html

    <div class="w-full md:w-1/2 lg:w-1/3">
        <!-- モバイル: 全幅、タブレット: 半分、デスクトップ: 1/3 -->
    </div>
    
    <h1 class="text-2xl md:text-4xl lg:text-6xl">
        <!-- レスポンシブなフォントサイズ -->
    </h1>

    Flexboxとグリッド
    -----------------

    **Flexbox**

    .. code-block:: html

    <!-- 基本的なFlexコンテナ -->
    <div class="flex justify-between items-center">
        <div>左</div>
        <div>右</div>
    </div>
    
    <!-- レスポンシブなFlex方向 -->
    <div class="flex flex-col md:flex-row gap-4">
        <div class="flex-1">アイテム1</div>
        <div class="flex-1">アイテム2</div>
    </div>

    **Grid**

    .. code-block:: html

    <!-- 基本的なグリッド -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div>カード1</div>
        <div>カード2</div>
        <div>カード3</div>
    </div>
    
    <!-- 複雑なグリッドレイアウト -->
    <div class="grid grid-cols-12 gap-4">
        <div class="col-span-12 md:col-span-8">メインコンテンツ</div>
        <div class="col-span-12 md:col-span-4">サイドバー</div>
    </div>

    実装例
    ======

    ナビゲーションバー
    ------------------

    .. code-block:: html

    <nav class="bg-white shadow-lg">
        <div class="max-w-7xl mx-auto px-4">
        <div class="flex justify-between items-center py-4">
            <!-- ロゴ -->
            <div class="flex items-center space-x-4">
            <img class="h-8 w-8" src="logo.svg" alt="Logo">
            <span class="font-bold text-xl text-gray-800">MyApp</span>
            </div>
            
            <!-- デスクトップメニュー -->
            <div class="hidden md:flex items-center space-x-8">
            <a href="#" class="text-gray-700 hover:text-blue-600 transition duration-200">
                ホーム
            </a>
            <a href="#" class="text-gray-700 hover:text-blue-600 transition duration-200">
                サービス
            </a>
            <a href="#" class="text-gray-700 hover:text-blue-600 transition duration-200">
                お問い合わせ
            </a>
            <button class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition duration-200">
                ログイン
            </button>
            </div>
            
            <!-- モバイルメニューボタン -->
            <div class="md:hidden">
            <button class="text-gray-700 hover:text-blue-600">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
            </button>
            </div>
        </div>
        </div>
    </nav>

    カードコンポーネント
    --------------------

    .. code-block:: html

    <div class="max-w-sm mx-auto bg-white rounded-xl shadow-md overflow-hidden">
        <div class="md:flex">
        <div class="md:shrink-0">
            <img class="h-48 w-full object-cover md:h-full md:w-48" 
                src="image.jpg" alt="Card image">
        </div>
        <div class="p-8">
            <div class="uppercase tracking-wide text-sm text-indigo-500 font-semibold">
            カテゴリ
            </div>
            <h3 class="block mt-1 text-lg leading-tight font-medium text-black hover:underline">
            カードタイトル
            </h3>
            <p class="mt-2 text-slate-500">
            ここにカードの説明文が入ります。簡潔で分かりやすい内容を記載します。
            </p>
            <div class="mt-4">
            <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                詳細を見る
            </button>
            </div>
        </div>
        </div>
    </div>

    フォーム
    --------

    .. code-block:: html

    <form class="max-w-md mx-auto bg-white p-8 rounded-lg shadow-md">
        <h2 class="text-2xl font-bold mb-6 text-center text-gray-800">
        お問い合わせ
        </h2>
        
        <!-- 名前フィールド -->
        <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="name">
            お名前
        </label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline focus:border-blue-500" 
                id="name" type="text" placeholder="山田太郎">
        </div>
        
        <!-- メールアドレスフィールド -->
        <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
            メールアドレス
        </label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline focus:border-blue-500" 
                id="email" type="email" placeholder="example@mail.com">
        </div>
        
        <!-- メッセージフィールド -->
        <div class="mb-6">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="message">
            メッセージ
        </label>
        <textarea class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline focus:border-blue-500 h-32 resize-none" 
                    id="message" placeholder="お問い合わせ内容をご記入ください"></textarea>
        </div>
        
        <!-- 送信ボタン -->
        <div class="flex items-center justify-center">
        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full transition duration-200" 
                type="submit">
            送信する
        </button>
        </div>
    </form>

    ダッシュボード レイアウト
    -------------------------

    .. code-block:: html

    <div class="min-h-screen bg-gray-100">
        <!-- ヘッダー -->
        <header class="bg-white shadow">
        <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
            <h1 class="text-3xl font-bold text-gray-900">ダッシュボード</h1>
        </div>
        </header>
        
        <!-- メインコンテンツ -->
        <main class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <!-- 統計カード -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
            <div class="bg-white overflow-hidden shadow rounded-lg">
            <div class="p-5">
                <div class="flex items-center">
                <div class="flex-shrink-0">
                    <div class="w-8 h-8 bg-blue-500 rounded-full flex items-center justify-center">
                    <span class="text-white text-sm font-medium">U</span>
                    </div>
                </div>
                <div class="ml-5 w-0 flex-1">
                    <dl>
                    <dt class="text-sm font-medium text-gray-500 truncate">
                        総ユーザー数
                    </dt>
                    <dd class="text-lg font-medium text-gray-900">
                        1,234
                    </dd>
                    </dl>
                </div>
                </div>
            </div>
            </div>
            
            <!-- 他の統計カードも同様に -->
            <div class="bg-white overflow-hidden shadow rounded-lg">
            <div class="p-5">
                <div class="flex items-center">
                <div class="flex-shrink-0">
                    <div class="w-8 h-8 bg-green-500 rounded-full flex items-center justify-center">
                    <span class="text-white text-sm font-medium">S</span>
                    </div>
                </div>
                <div class="ml-5 w-0 flex-1">
                    <dl>
                    <dt class="text-sm font-medium text-gray-500 truncate">
                        売上
                    </dt>
                    <dd class="text-lg font-medium text-gray-900">
                        ¥567,890
                    </dd>
                    </dl>
                </div>
                </div>
            </div>
            </div>
        </div>
        
        <!-- データテーブル -->
        <div class="bg-white shadow overflow-hidden sm:rounded-md">
            <div class="px-4 py-5 sm:px-6">
            <h3 class="text-lg leading-6 font-medium text-gray-900">
                最近のアクティビティ
            </h3>
            </div>
            <ul class="divide-y divide-gray-200">
            <li class="px-4 py-4 sm:px-6 hover:bg-gray-50">
                <div class="flex items-center justify-between">
                <div class="flex items-center">
                    <div class="flex-shrink-0 h-10 w-10">
                    <img class="h-10 w-10 rounded-full" src="avatar1.jpg" alt="User">
                    </div>
                    <div class="ml-4">
                    <div class="text-sm font-medium text-gray-900">
                        田中花子
                    </div>
                    <div class="text-sm text-gray-500">
                        新しい注文を作成しました
                    </div>
                    </div>
                </div>
                <div class="text-sm text-gray-500">
                    2時間前
                </div>
                </div>
            </li>
            </ul>
        </div>
        </main>
    </div>

    中級テクニック
    ==============

    カスタムスタイルの追加
    ----------------------

    ``@layer`` ディレクティブを使用してカスタムスタイルを追加できます：

    .. code-block:: css

    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    
    @layer components {
        .btn-primary {
        @apply bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded;
        }
        
        .card {
        @apply bg-white rounded-lg shadow-md p-6;
        }
    }
    
    @layer utilities {
        .text-shadow {
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }
    }

    設定ファイルのカスタマイズ
    --------------------------

    ``tailwind.config.js`` でテーマをカスタマイズできます：

    .. code-block:: javascript

    module.exports = {
        content: ["./src/**/*.{html,js}"],
        theme: {
        extend: {
            colors: {
            'brand': {
                50: '#eff6ff',
                500: '#3b82f6',
                900: '#1e3a8a',
            }
            },
            fontFamily: {
            'sans': ['Noto Sans JP', 'sans-serif'],
            },
            spacing: {
            '128': '32rem',
            '144': '36rem',
            },
            animation: {
            'fade-in': 'fadeIn 0.5s ease-in-out',
            },
            keyframes: {
            fadeIn: {
                '0%': { opacity: '0' },
                '100%': { opacity: '1' },
            }
            }
        },
        },
        plugins: [],
    }

    ダークモード
    ------------

    Tailwind CSSは簡単にダークモードを実装できます：

    .. code-block:: javascript

    // tailwind.config.js
    module.exports = {
        darkMode: 'class', // または 'media'
        // ...
    }

    .. code-block:: html

    <div class="bg-white dark:bg-gray-800">
        <h1 class="text-gray-900 dark:text-white">
        タイトル
        </h1>
        <p class="text-gray-600 dark:text-gray-300">
        説明文
        </p>
    </div>

    JavaScriptでダークモード切り替え：

    .. code-block:: javascript

    // ダークモード切り替え
    function toggleDarkMode() {
        document.documentElement.classList.toggle('dark');
    }

    プラグインの活用
    ----------------

    **公式プラグイン**

    .. code-block:: bash

    npm install @tailwindcss/forms @tailwindcss/typography @tailwindcss/aspect-ratio

    .. code-block:: javascript

    // tailwind.config.js
    module.exports = {
        plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
        ],
    }

    **カスタムプラグイン**

    .. code-block:: javascript

    // tailwind.config.js
    const plugin = require('tailwindcss/plugin')
    
    module.exports = {
        plugins: [
        plugin(function({ addUtilities }) {
            const newUtilities = {
            '.skew-10deg': {
                transform: 'skewY(-10deg)',
            },
            '.skew-15deg': {
                transform: 'skewY(-15deg)',
            },
            }
            addUtilities(newUtilities)
        })
        ],
    }

    最適化とベストプラクティス
    ==========================

    パフォーマンス最適化
    --------------------

    **PurgeCSS（自動）**
    Tailwind CSS v3.0以降では、未使用のCSSが自動的に削除されます。

    **JIT（Just-In-Time）モード**
    必要なクラスのみが生成されるため、ビルド時間が短縮されます。

    ベストプラクティス
    ------------------

    **1. コンポーネントベースの設計**

    .. code-block:: html

    <!-- 良い例：再利用可能なコンポーネント -->
    <button class="btn-primary">
        クリック
    </button>

    **2. レスポンシブデザインファースト**

    .. code-block:: html

    <!-- モバイルファーストでレスポンシブ -->
    <div class="text-sm md:text-base lg:text-lg">
        レスポンシブテキスト
    </div>

    **3. セマンティックな命名**

    .. code-block:: css

    @layer components {
        .article-title {
        @apply text-2xl font-bold text-gray-900 mb-4;
        }
        
        .article-content {
        @apply text-gray-700 leading-relaxed;
        }
    }

    **4. 一貫性のあるスペーシング**

    Tailwind CSSのスペーシングスケールを活用：

    .. code-block:: html

    <!-- 一貫したスペーシング -->
    <div class="space-y-4">
        <div class="p-4">コンテンツ1</div>
        <div class="p-4">コンテンツ2</div>
    </div>

    開発効率向上のテクニック
    ------------------------

    **1. エディタ拡張機能**

    * Tailwind CSS IntelliSense（VS Code）
    * 自動補完とプレビュー機能

    **2. ユーティリティファーストの思考**

    従来のCSSの考え方から、ユーティリティクラスの組み合わせで考える思考に転換。

    **3. デザインシステムとの統合**

    設定ファイルでデザインシステムの色やスペーシングを定義し、一貫性を保つ。

    トラブルシューティング
    ======================

    よくある問題と解決策
    --------------------

    **1. スタイルが適用されない**

    * content設定でファイルパスが正しく指定されているか確認
    * クラス名のタイポがないか確認
    * ビルドプロセスが正常に動作しているか確認

    **2. CSSファイルサイズが大きい**

    * 本番ビルドでPurgeCSSが有効になっているか確認
    * 不要なプラグインを削除

    **3. カスタムスタイルが効かない**

    * ``@layer`` ディレクティブを使用しているか確認
    * CSS詳細度の問題がないか確認

    まとめ
    ======

    Tailwind CSSは現代的なWeb開発において非常に強力なツールです。ユーティリティファーストのアプローチにより、高速な開発と一貫性のあるデザインシステムの構築が可能になります。

    **主なメリット:**

    * 開発速度の向上
    * デザインシステムの一貫性
    * レスポンシブデザインの簡単な実装
    * 高いカスタマイズ性
    * 優れたパフォーマンス

    **学習のポイント:**

    * ユーティリティクラスの命名規則を理解する
    * レスポンシブデザインの考え方をマスターする
    * 設定ファイルのカスタマイズ方法を覚える
    * 実際のプロジェクトで実践を積む

    継続的な学習と実践により、Tailwind CSSを使った効率的なWeb開発が可能になります。公式ドキュメントや実践的なプロジェクトを通じて、さらなるスキル向上を目指しましょう。

    参考資料
    ========

    * `Tailwind CSS 公式ドキュメント <https://tailwindcss.com/docs>`_
    * `Tailwind UI <https://tailwindui.com/>`_
    * `Headless UI <https://headlessui.com/>`_
    * `Tailwind CSS チートシート <https://nerdcave.com/tailwind-cheat-sheet>`_