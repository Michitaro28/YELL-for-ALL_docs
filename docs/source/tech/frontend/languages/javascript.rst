
    フロントエンドJavaScript解説
    ====================================

    はじめに
    ========

    JavaScript（JS）は、Webブラウザ上で動作するプログラミング言語で、Webページに動的な機能を追加するために使用されます。HTMLが構造、CSSが見た目を担当するのに対し、JavaScriptはWebページの振る舞いや機能を制御します。

    基本概念
    ========

    変数と データ型
    --------------

    JavaScriptでは、``var``、``let``、``const``を使って変数を宣言します。

    .. code-block:: javascript

    // 変数の宣言
    let name = "田中";
    const age = 25;
    var isActive = true;

    // データ型の例
    let number = 42;           // 数値
    let text = "Hello World";  // 文字列
    let flag = false;          // 真偽値
    let items = [1, 2, 3];     // 配列
    let person = {             // オブジェクト
        name: "佐藤",
        age: 30
    };

    関数
    ----

    関数は処理をまとめて再利用可能にする仕組みです。

    .. code-block:: javascript

    // 関数宣言
    function greet(name) {
        return "こんにちは、" + name + "さん！";
    }

    // アロー関数（ES6以降）
    const multiply = (a, b) => a * b;

    // 使用例
    console.log(greet("山田"));     // "こんにちは、山田さん！"
    console.log(multiply(5, 3));   // 15

    DOM操作
    =======

    DOM（Document Object Model）は、HTMLドキュメントをJavaScriptから操作するためのAPIです。

    要素の取得
    ----------

    .. code-block:: javascript

    // IDで要素を取得
    const element = document.getElementById("myButton");

    // クラス名で要素を取得
    const elements = document.getElementsByClassName("item");

    // CSSセレクタで要素を取得
    const firstItem = document.querySelector(".item");
    const allItems = document.querySelectorAll(".item");

    要素の操作
    ----------

    .. code-block:: javascript

    // テキストの変更
    element.textContent = "新しいテキスト";

    // HTMLの変更
    element.innerHTML = "<strong>太字テキスト</strong>";

    // スタイルの変更
    element.style.color = "red";
    element.style.display = "none";

    // クラスの追加・削除
    element.classList.add("active");
    element.classList.remove("inactive");
    element.classList.toggle("highlight");

    実際の使用例
    ============

    ボタンクリックイベント
    --------------------

    .. code-block:: html

    <!-- HTML -->
    <button id="clickMe">クリックしてください</button>
    <p id="message"></p>

    .. code-block:: javascript

    // JavaScript
    const button = document.getElementById("clickMe");
    const message = document.getElementById("message");

    button.addEventListener("click", function() {
        message.textContent = "ボタンがクリックされました！";
    });

    フォームの検証
    --------------

    .. code-block:: html

    <!-- HTML -->
    <form id="userForm">
        <input type="text" id="username" placeholder="ユーザー名">
        <input type="email" id="email" placeholder="メールアドレス">
        <button type="submit">送信</button>
    </form>
    <div id="error"></div>

    .. code-block:: javascript

    // JavaScript
    const form = document.getElementById("userForm");
    const errorDiv = document.getElementById("error");

    form.addEventListener("submit", function(event) {
        event.preventDefault(); // デフォルトの送信を防ぐ

        const username = document.getElementById("username").value;
        const email = document.getElementById("email").value;

        if (username.length < 3) {
            errorDiv.textContent = "ユーザー名は3文字以上で入力してください";
            return;
        }

        if (!email.includes("@")) {
            errorDiv.textContent = "正しいメールアドレスを入力してください";
            return;
        }

        errorDiv.textContent = "";
        alert("フォームが正常に送信されました！");
    });

    動的なリスト作成
    --------------

    .. code-block:: html

    <!-- HTML -->
    <input type="text" id="itemInput" placeholder="アイテムを入力">
    <button id="addItem">追加</button>
    <ul id="itemList"></ul>

    .. code-block:: javascript

    // JavaScript
    const input = document.getElementById("itemInput");
    const addButton = document.getElementById("addItem");
    const list = document.getElementById("itemList");

    addButton.addEventListener("click", function() {
        const itemText = input.value.trim();
        
        if (itemText !== "") {
            const listItem = document.createElement("li");
            listItem.textContent = itemText;
            
            // 削除ボタンの追加
            const deleteButton = document.createElement("button");
            deleteButton.textContent = "削除";
            deleteButton.addEventListener("click", function() {
                list.removeChild(listItem);
            });
            
            listItem.appendChild(deleteButton);
            list.appendChild(listItem);
            input.value = ""; // 入力欄をクリア
        }
    });

    非同期処理
    ==========

    非同期処理は、時間のかかる処理（API呼び出しなど）を行う際に、ページをブロックしないようにする仕組みです。

    Fetch APIを使用したHTTP通信
    -------------------------

    .. code-block:: javascript

    // GETリクエスト
    fetch("https://api.example.com/users")
        .then(response => response.json())
        .then(data => {
            console.log("取得したデータ:", data);
            // データをページに表示
            displayUsers(data);
        })
        .catch(error => {
            console.error("エラー:", error);
        });

    // async/awaitを使用した書き方
    async function fetchUsers() {
        try {
            const response = await fetch("https://api.example.com/users");
            const data = await response.json();
            displayUsers(data);
        } catch (error) {
            console.error("エラー:", error);
        }
    }

    function displayUsers(users) {
        const container = document.getElementById("userContainer");
        container.innerHTML = "";
        
        users.forEach(user => {
            const userDiv = document.createElement("div");
            userDiv.innerHTML = `
                <h3>${user.name}</h3>
                <p>Email: ${user.email}</p>
            `;
            container.appendChild(userDiv);
        });
    }

    イベント処理
    ============

    JavaScriptでは様々なイベントに対応できます。

    よく使用されるイベント
    --------------------

    .. code-block:: javascript

    // クリックイベント
    element.addEventListener("click", function(event) {
        console.log("要素がクリックされました");
    });

    // マウスオーバー・アウト
    element.addEventListener("mouseenter", function() {
        this.style.backgroundColor = "lightblue";
    });

    element.addEventListener("mouseleave", function() {
        this.style.backgroundColor = "";
    });

    // キー入力イベント
    input.addEventListener("keyup", function(event) {
        if (event.key === "Enter") {
            console.log("Enterキーが押されました");
        }
    });

    // ページ読み込み完了
    document.addEventListener("DOMContentLoaded", function() {
        console.log("ページの読み込みが完了しました");
        // 初期化処理をここに書く
    });

    実践的な例：簡単なタブ機能
    ========================

    .. code-block:: html

    <!-- HTML -->
    <div class="tab-container">
        <div class="tabs">
            <button class="tab-button active" data-tab="tab1">タブ1</button>
            <button class="tab-button" data-tab="tab2">タブ2</button>
            <button class="tab-button" data-tab="tab3">タブ3</button>
        </div>
        <div class="tab-content">
            <div id="tab1" class="tab-panel active">タブ1の内容</div>
            <div id="tab2" class="tab-panel">タブ2の内容</div>
            <div id="tab3" class="tab-panel">タブ3の内容</div>
        </div>
    </div>

    .. code-block:: css

    /* CSS */
    .tab-button {
        padding: 10px 20px;
        border: none;
        background-color: #f0f0f0;
        cursor: pointer;
    }

    .tab-button.active {
        background-color: #007bff;
        color: white;
    }

    .tab-panel {
        display: none;
        padding: 20px;
        border: 1px solid #ddd;
    }

    .tab-panel.active {
        display: block;
    }

    .. code-block:: javascript

    // JavaScript
    document.addEventListener("DOMContentLoaded", function() {
        const tabButtons = document.querySelectorAll(".tab-button");
        const tabPanels = document.querySelectorAll(".tab-panel");

        tabButtons.forEach(button => {
            button.addEventListener("click", function() {
                const targetTab = this.getAttribute("data-tab");

                // すべてのタブボタンとパネルから active クラスを削除
                tabButtons.forEach(btn => btn.classList.remove("active"));
                tabPanels.forEach(panel => panel.classList.remove("active"));

                // クリックされたタブボタンと対応するパネルにactiveクラスを追加
                this.classList.add("active");
                document.getElementById(targetTab).classList.add("active");
            });
        });
    });

    ベストプラクティス
    ==================

    コードの組織化
    --------------

    .. code-block:: javascript

    // モジュールパターンを使用した組織化
    const TodoApp = {
        init: function() {
            this.bindEvents();
            this.loadTodos();
        },

        bindEvents: function() {
            document.getElementById("addTodo").addEventListener("click", 
                this.addTodo.bind(this));
        },

        addTodo: function() {
            // TODO追加の処理
        },

        loadTodos: function() {
            // TODO読み込みの処理
        }
    };

    // アプリケーションの初期化
    TodoApp.init();

    エラーハンドリング
    ----------------

    .. code-block:: javascript

    function processUserData(userData) {
        try {
            if (!userData || !userData.name) {
                throw new Error("ユーザーデータが不正です");
            }
            
            // データ処理
            return userData.name.toUpperCase();
        } catch (error) {
            console.error("エラーが発生しました:", error.message);
            return "不明なユーザー";
        }
    }

    パフォーマンスの考慮
    ------------------

    .. code-block:: javascript

    // イベント委譲を使用してパフォーマンスを向上
    document.getElementById("itemList").addEventListener("click", function(event) {
        if (event.target.classList.contains("delete-button")) {
            // 削除処理
            event.target.parentElement.remove();
        }
    });

    // デバウンス処理（検索入力など）
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    const searchInput = document.getElementById("search");
    const debouncedSearch = debounce(function(query) {
        // 検索処理
        console.log("検索:", query);
    }, 300);

    searchInput.addEventListener("input", function() {
        debouncedSearch(this.value);
    });

    まとめ
    ======

    フロントエンドJavaScriptは、Webページを動的で対話的なものにするための強力なツールです。基本的なDOM操作から始めて、イベント処理、非同期通信まで段階的に学習することで、より複雑なWebアプリケーションを構築できるようになります。

    重要なポイント：

    - **DOM操作**: 要素の取得、変更、追加、削除
    - **イベント処理**: ユーザーの操作に応答する仕組み
    - **非同期処理**: APIとの通信やタイマー処理
    - **エラーハンドリング**: 予期しない状況への対応
    - **パフォーマンス**: 効率的なコードの書き方

    継続的な学習と実践を通じて、より高度なJavaScript技術を身につけていきましょう。