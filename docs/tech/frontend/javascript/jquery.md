# jQuery入門ガイド

jQueryは、JavaScriptをより簡単に書けるようにするライブラリです。HTML要素の操作、イベント処理、アニメーションなどを直感的に実装できます。

## jQueryとは

jQueryは「write less, do more」（少ない記述で、より多くのことを）をモットーとするJavaScriptライブラリです。複雑なJavaScriptコードを簡潔に書くことができます。

### jQueryの特徴

- **シンプルな構文**: CSS セレクターを使った要素の選択
- **クロスブラウザ対応**: ブラウザの違いを意識せずに開発可能
- **豊富な機能**: DOM操作、イベント処理、アニメーション、Ajax通信
- **チェーンメソッド**: 複数の処理を連続して実行可能

## jQueryの導入

### CDNを使用した導入方法

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>jQuery入門</title>
    <!-- jQuery CDNの読み込み -->
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
</head>
<body>
    <h1>jQuery入門</h1>
    
    <script>
        // jQueryのコードをここに書きます
        $(document).ready(function() {
            console.log("jQueryが読み込まれました！");
        });
    </script>
</body>
</html>
```

### ローカルファイルを使用した導入方法

```html
<!-- ダウンロードしたjQueryファイルを使用 -->
<script src="js/jquery-3.7.1.min.js"></script>
```

## 基本的な構文

### jQueryの基本形

```javascript
$(document).ready(function() {
    // DOMが読み込まれた後に実行されるコード
    console.log("ページの読み込みが完了しました");
});

// 短縮形
$(function() {
    // 同じ意味のコード
    console.log("ページの読み込みが完了しました");
});
```

### 要素の選択（セレクター）

```javascript
$(function() {
    // IDで選択
    $("#myId")           // <div id="myId">
    
    // クラスで選択
    $(".myClass")        // <div class="myClass">
    
    // タグで選択
    $("p")               // すべての<p>要素
    
    // 属性で選択
    $("[data-role='button']")  // data-role="button"を持つ要素
    
    // 複合セレクター
    $("div.myClass")     // class="myClass"を持つdiv要素
    $("#container p")    // id="container"内のすべてのp要素
    $("li:first")        // 最初のli要素
    $("li:last")         // 最後のli要素
    $("li:eq(2)")        // 3番目のli要素（0から開始）
});
```

## DOM操作

### テキストとHTMLの操作

```html
<!-- HTML -->
<div id="content">
    <p id="message">元のメッセージ</p>
    <div id="info"></div>
</div>

<button id="changeText">テキスト変更</button>
<button id="addHTML">HTML追加</button>
```

```javascript
$(function() {
    // テキストの取得と設定
    $("#changeText").click(function() {
        // テキストの取得
        var currentText = $("#message").text();
        console.log("現在のテキスト: " + currentText);
        
        // テキストの設定
        $("#message").text("新しいメッセージに変更されました！");
    });
    
    // HTMLの取得と設定
    $("#addHTML").click(function() {
        // HTMLの設定
        $("#info").html("<strong>重要:</strong> これは<em>HTML</em>です");
        
        // HTMLの追加
        $("#info").append("<br>追加のテキスト");
        $("#info").prepend("先頭に追加: ");
    });
});
```

### 属性とCSSの操作

```html
<!-- HTML -->
<img id="myImage" src="image1.jpg" alt="画像1">
<button id="changeImage">画像変更</button>
<button id="toggleStyle">スタイル切り替え</button>

<style>
.highlight {
    background-color: yellow;
    border: 2px solid red;
}
.large-text {
    font-size: 20px;
    font-weight: bold;
}
</style>
```

```javascript
$(function() {
    // 属性の操作
    $("#changeImage").click(function() {
        // 属性の取得
        var currentSrc = $("#myImage").attr("src");
        console.log("現在の画像: " + currentSrc);
        
        // 属性の設定
        $("#myImage").attr({
            "src": "image2.jpg",
            "alt": "画像2"
        });
    });
    
    // CSS操作
    $("#toggleStyle").click(function() {
        // CSSクラスの追加/削除
        $("#myImage").toggleClass("highlight");
        
        // 直接CSSスタイルの設定
        $("#myImage").css({
            "border-radius": "10px",
            "transition": "all 0.3s ease"
        });
    });
});
```

### 要素の作成と削除

```html
<!-- HTML -->
<ul id="itemList">
    <li>アイテム1</li>
    <li>アイテム2</li>
</ul>

<input type="text" id="newItem" placeholder="新しいアイテム">
<button id="addItem">追加</button>
<button id="removeItem">最後のアイテムを削除</button>
```

```javascript
$(function() {
    // 要素の追加
    $("#addItem").click(function() {
        var newText = $("#newItem").val();
        if (newText.trim() !== "") {
            // 新しいli要素を作成して追加
            var newLi = $("<li>").text(newText);
            $("#itemList").append(newLi);
            
            // 入力欄をクリア
            $("#newItem").val("");
        }
    });
    
    // 要素の削除
    $("#removeItem").click(function() {
        $("#itemList li:last").remove();
    });
    
    // リストアイテムをクリックで削除
    $(document).on("click", "#itemList li", function() {
        $(this).fadeOut(function() {
            $(this).remove();
        });
    });
});
```

## イベント処理

### 基本的なイベント

```html
<!-- HTML -->
<button id="clickBtn">クリック</button>
<input type="text" id="textInput" placeholder="何か入力してください">
<div id="mouseArea" style="width: 200px; height: 100px; background: lightblue;">
    マウスイベントエリア
</div>
<div id="output"></div>
```

```javascript
$(function() {
    // クリックイベント
    $("#clickBtn").click(function() {
        $("#output").append("<p>ボタンがクリックされました！</p>");
    });
    
    // 入力イベント
    $("#textInput").on("input", function() {
        var inputValue = $(this).val();
        $("#output").html("<p>入力中: " + inputValue + "</p>");
    });
    
    // マウスイベント
    $("#mouseArea")
        .mouseenter(function() {
            $(this).css("background-color", "yellow");
            $("#output").append("<p>マウスが入りました</p>");
        })
        .mouseleave(function() {
            $(this).css("background-color", "lightblue");
            $("#output").append("<p>マウスが出ました</p>");
        });
    
    // フォーカスイベント
    $("#textInput")
        .focus(function() {
            $(this).css("border", "2px solid green");
        })
        .blur(function() {
            $(this).css("border", "1px solid #ccc");
        });
});
```

### フォームイベント

```html
<!-- HTML -->
<form id="myForm">
    <div>
        <label for="name">名前:</label>
        <input type="text" id="name" name="name" required>
    </div>
    <div>
        <label for="email">メール:</label>
        <input type="email" id="email" name="email" required>
    </div>
    <div>
        <label for="age">年齢:</label>
        <select id="age" name="age">
            <option value="">選択してください</option>
            <option value="teen">10代</option>
            <option value="twenties">20代</option>
            <option value="thirties">30代</option>
        </select>
    </div>
    <button type="submit">送信</button>
</form>
<div id="formOutput"></div>
```

```javascript
$(function() {
    // フォーム送信イベント
    $("#myForm").submit(function(e) {
        e.preventDefault(); // デフォルトの送信動作を防ぐ
        
        // フォームデータの取得
        var formData = {
            name: $("#name").val(),
            email: $("#email").val(),
            age: $("#age").val()
        };
        
        // バリデーション
        if (formData.name === "" || formData.email === "") {
            $("#formOutput").html("<p style='color: red;'>名前とメールは必須です</p>");
            return;
        }
        
        // 送信成功時の処理
        $("#formOutput").html(
            "<h3>送信されたデータ:</h3>" +
            "<p>名前: " + formData.name + "</p>" +
            "<p>メール: " + formData.email + "</p>" +
            "<p>年齢: " + formData.age + "</p>"
        );
        
        // フォームをリセット
        this.reset();
    });
    
    // 選択変更イベント
    $("#age").change(function() {
        var selectedAge = $(this).val();
        if (selectedAge) {
            $("#formOutput").append("<p>年齢層が選択されました: " + selectedAge + "</p>");
        }
    });
});
```

## アニメーション

### 基本的なアニメーション

```html
<!-- HTML -->
<div id="animationBox" style="width: 100px; height: 100px; background: red;">
    アニメーション
</div>

<button id="fadeToggle">フェード切り替え</button>
<button id="slideToggle">スライド切り替え</button>
<button id="customAnimate">カスタムアニメーション</button>
```

```javascript
$(function() {
    // フェードイン/フェードアウト
    $("#fadeToggle").click(function() {
        $("#animationBox").fadeToggle(1000); // 1000ms = 1秒
    });
    
    // スライドアップ/スライドダウン
    $("#slideToggle").click(function() {
        $("#animationBox").slideToggle("slow");
    });
    
    // カスタムアニメーション
    $("#customAnimate").click(function() {
        $("#animationBox").animate({
            width: "200px",
            height: "200px",
            opacity: 0.5,
            marginLeft: "50px"
        }, 2000, function() {
            // アニメーション完了後のコールバック
            alert("アニメーションが完了しました！");
            
            // 元に戻す
            $(this).animate({
                width: "100px",
                height: "100px",
                opacity: 1,
                marginLeft: "0px"
            }, 1000);
        });
    });
});
```

### 連続アニメーション（チェーン）

```html
<!-- HTML -->
<div id="chainBox" style="width: 50px; height: 50px; background: blue; position: relative;">
    チェーン
</div>
<button id="startChain">チェーンアニメーション開始</button>
```

```javascript
$(function() {
    $("#startChain").click(function() {
        $("#chainBox")
            .animate({left: "200px"}, 1000)          // 右に移動
            .animate({top: "100px"}, 1000)           // 下に移動
            .animate({left: "0px"}, 1000)            // 左に移動
            .animate({top: "0px"}, 1000)             // 上に移動
            .fadeOut(500)                            // フェードアウト
            .fadeIn(500);                            // フェードイン
    });
});
```

## Ajax通信

### 基本的なAjax

```html
<!-- HTML -->
<button id="loadData">データ読み込み</button>
<button id="sendData">データ送信</button>
<div id="ajaxResult"></div>
```

```javascript
$(function() {
    // GET リクエスト
    $("#loadData").click(function() {
        $.ajax({
            url: "https://jsonplaceholder.typicode.com/posts/1",
            method: "GET",
            dataType: "json",
            beforeSend: function() {
                $("#ajaxResult").html("<p>読み込み中...</p>");
            },
            success: function(data) {
                $("#ajaxResult").html(
                    "<h3>取得したデータ:</h3>" +
                    "<p>タイトル: " + data.title + "</p>" +
                    "<p>内容: " + data.body + "</p>"
                );
            },
            error: function(xhr, status, error) {
                $("#ajaxResult").html("<p style='color: red;'>エラーが発生しました: " + error + "</p>");
            }
        });
    });
    
    // POST リクエスト
    $("#sendData").click(function() {
        var postData = {
            title: "jQueryからの投稿",
            body: "これはjQueryのAjaxで送信されたデータです",
            userId: 1
        };
        
        $.ajax({
            url: "https://jsonplaceholder.typicode.com/posts",
            method: "POST",
            data: JSON.stringify(postData),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(response) {
                $("#ajaxResult").html(
                    "<h3>送信成功:</h3>" +
                    "<p>作成されたID: " + response.id + "</p>" +
                    "<p>タイトル: " + response.title + "</p>"
                );
            },
            error: function(xhr, status, error) {
                $("#ajaxResult").html("<p style='color: red;'>送信エラー: " + error + "</p>");
            }
        });
    });
});
```

### 簡略化されたAjaxメソッド

```javascript
$(function() {
    // $.get() - GETリクエストの簡略形
    $("#simpleGet").click(function() {
        $.get("https://jsonplaceholder.typicode.com/users/1")
            .done(function(data) {
                console.log("成功:", data);
            })
            .fail(function() {
                console.log("失敗");
            });
    });
    
    // $.post() - POSTリクエストの簡略形
    $("#simplePost").click(function() {
        $.post("https://jsonplaceholder.typicode.com/posts", {
            title: "簡単な投稿",
            body: "$.post()を使用",
            userId: 1
        })
        .done(function(data) {
            console.log("投稿成功:", data);
        });
    });
    
    // $.getJSON() - JSON取得の簡略形
    $("#getJson").click(function() {
        $.getJSON("https://jsonplaceholder.typicode.com/posts/1", function(data) {
            console.log("JSONデータ:", data);
        });
    });
});
```

## 実践的な例：ToDoアプリ

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>jQuery ToDoアプリ</title>
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    <style>
        .todo-app {
            max-width: 500px;
            margin: 50px auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 8px;
        }
        .todo-input {
            width: 70%;
            padding: 10px;
            margin-right: 10px;
        }
        .add-btn {
            padding: 10px 20px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .todo-list {
            list-style: none;
            padding: 0;
            margin-top: 20px;
        }
        .todo-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
            border-bottom: 1px solid #eee;
        }
        .todo-item.completed {
            opacity: 0.6;
            text-decoration: line-through;
        }
        .delete-btn {
            background: #dc3545;
            color: white;
            border: none;
            padding: 5px 10px;
            border-radius: 4px;
            cursor: pointer;
        }
        .complete-btn {
            background: #28a745;
            color: white;
            border: none;
            padding: 5px 10px;
            border-radius: 4px;
            cursor: pointer;
            margin-right: 5px;
        }
    </style>
</head>
<body>
    <div class="todo-app">
        <h1>ToDoアプリ</h1>
        <div>
            <input type="text" id="todoInput" class="todo-input" placeholder="新しいタスクを入力">
            <button id="addTodo" class="add-btn">追加</button>
        </div>
        <ul id="todoList" class="todo-list"></ul>
        <div>
            <p>総タスク数: <span id="totalCount">0</span></p>
            <p>完了済み: <span id="completedCount">0</span></p>
        </div>
    </div>

    <script>
        $(function() {
            var todos = [];
            var todoId = 0;

            // タスク追加
            function addTodo() {
                var todoText = $("#todoInput").val().trim();
                if (todoText === "") {
                    alert("タスクを入力してください");
                    return;
                }

                var todo = {
                    id: ++todoId,
                    text: todoText,
                    completed: false
                };

                todos.push(todo);
                $("#todoInput").val("");
                renderTodos();
                updateCounts();
            }

            // タスク表示
            function renderTodos() {
                var $todoList = $("#todoList");
                $todoList.empty();

                todos.forEach(function(todo) {
                    var $todoItem = $("<li>")
                        .addClass("todo-item")
                        .attr("data-id", todo.id);

                    if (todo.completed) {
                        $todoItem.addClass("completed");
                    }

                    var $todoText = $("<span>").text(todo.text);
                    var $buttons = $("<div>");

                    var $completeBtn = $("<button>")
                        .addClass("complete-btn")
                        .text(todo.completed ? "戻す" : "完了")
                        .click(function() {
                            toggleComplete(todo.id);
                        });

                    var $deleteBtn = $("<button>")
                        .addClass("delete-btn")
                        .text("削除")
                        .click(function() {
                            deleteTodo(todo.id);
                        });

                    $buttons.append($completeBtn, $deleteBtn);
                    $todoItem.append($todoText, $buttons);
                    $todoList.append($todoItem);
                });
            }

            // 完了状態切り替え
            function toggleComplete(id) {
                var todo = todos.find(function(t) { return t.id === id; });
                if (todo) {
                    todo.completed = !todo.completed;
                    renderTodos();
                    updateCounts();
                }
            }

            // タスク削除
            function deleteTodo(id) {
                if (confirm("このタスクを削除しますか？")) {
                    todos = todos.filter(function(t) { return t.id !== id; });
                    
                    // フェードアウトアニメーション
                    $("[data-id='" + id + "']").fadeOut(300, function() {
                        renderTodos();
                        updateCounts();
                    });
                }
            }

            // カウント更新
            function updateCounts() {
                var totalCount = todos.length;
                var completedCount = todos.filter(function(t) { return t.completed; }).length;
                
                $("#totalCount").text(totalCount);
                $("#completedCount").text(completedCount);
            }

            // イベント登録
            $("#addTodo").click(addTodo);
            
            $("#todoInput").keypress(function(e) {
                if (e.which === 13) { // Enterキー
                    addTodo();
                }
            });

            // 初期表示
            updateCounts();
        });
    </script>
</body>
</html>
```

## よく使うjQueryメソッド一覧

### 基本操作
```javascript
// 要素選択
$("selector")           // セレクターで要素選択
$(this)                 // 現在の要素
$(document)             // ドキュメント全体

// 内容操作
.text()                 // テキストの取得/設定
.html()                 // HTMLの取得/設定
.val()                  // フォーム要素の値取得/設定
.attr()                 // 属性の取得/設定
.removeAttr()           // 属性の削除

// CSS操作
.css()                  // CSSスタイルの取得/設定
.addClass()             // クラス追加
.removeClass()          // クラス削除
.toggleClass()          // クラス切り替え
.hasClass()             // クラス存在確認

// DOM操作
.append()               // 末尾に追加
.prepend()              // 先頭に追加
.after()                // 要素の後に追加
.before()               // 要素の前に追加
.remove()               // 要素削除
.empty()                // 子要素をすべて削除

// イベント
.click()                // クリックイベント
.on()                   // イベント登録
.off()                  // イベント削除
.trigger()              // イベント発火

// アニメーション
.show()                 // 表示
.hide()                 // 非表示
.fadeIn()               // フェードイン
.fadeOut()              // フェードアウト
.slideUp()              // スライドアップ
.slideDown()            // スライドダウン
.animate()              // カスタムアニメーション
```

## まとめ

jQueryは、JavaScriptをより簡単に書けるようにする強力なライブラリです。この章で学習した内容：

- **jQueryの導入**: CDNまたはローカルファイルでの読み込み方法
- **基本構文**: セレクターと$(document).ready()の使い方
- **DOM操作**: 要素の選択、内容変更、属性操作
- **イベント処理**: クリック、フォーム、マウスイベントの処理
- **アニメーション**: フェード、スライド、カスタムアニメーション
- **Ajax通信**: サーバーとの非同期通信
- **実践例**: ToDoアプリの実装

jQueryをマスターすることで、インタラクティブなWebページを効率的に作成できるようになります。まずは基本的な操作から始めて、徐々に複雑な機能に挑戦してみてください。

## 次のステップ

1. **jQueryプラグイン**: 既存のプラグインを使って機能を拡張
2. **jQuery UI**: ユーザーインターフェース要素の実装
3. **モダンJavaScript**: ES6+やReact、Vue.jsなどの学習
4. **パフォーマンス最適化**: jQueryコードの効率化

現代のWeb開発では、ReactやVue.jsなどのフレームワークが主流になっていますが、jQueryで学んだ概念は他の技術でも応用できる重要な基礎知識となります。