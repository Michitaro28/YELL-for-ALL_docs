# フロントエンドのためのJavaScript完全ガイド

## JavaScriptとは

JavaScriptは、Webページに動的な機能を追加するプログラミング言語です。ブラウザ上で動作し、ユーザーインタラクションの処理、DOM操作、非同期通信など、モダンなWebアプリケーションに不可欠な機能を提供します。

## JavaScript基礎

### 変数と定数

```javascript
// var（古い書き方、使用は推奨されない）
var oldVariable = "古い方式";

// let（再代入可能）
let userName = "太郎";
userName = "花子"; // 再代入可能

// const（再代入不可）
const API_URL = "https://api.example.com";
const userInfo = { name: "太郎", age: 25 };
// userInfo = {}; // エラー：再代入不可
userInfo.name = "花子"; // オブジェクトの中身は変更可能
```

### データ型

```javascript
// プリミティブ型
const number = 42;
const string = "Hello World";
const boolean = true;
const nullValue = null;
const undefinedValue = undefined;
const symbol = Symbol("unique");
const bigint = 123n;

// オブジェクト型
const array = [1, 2, 3, "four", true];
const object = {
  name: "太郎",
  age: 30,
  hobbies: ["読書", "映画鑑賞"]
};
const func = function() { return "Hello"; };

// 型の確認
console.log(typeof number);    // "number"
console.log(typeof string);    // "string"
console.log(typeof boolean);   // "boolean"
console.log(Array.isArray(array)); // true
```

### 関数

```javascript
// 関数宣言
function greet(name) {
  return `こんにちは、${name}さん！`;
}

// 関数式
const greetFunction = function(name) {
  return `こんにちは、${name}さん！`;
};

// アロー関数
const greetArrow = (name) => {
  return `こんにちは、${name}さん！`;
};

// アロー関数（短縮形）
const greetShort = name => `こんにちは、${name}さん！`;

// 複数パラメータ
const add = (a, b) => a + b;

// デフォルトパラメータ
const greetWithDefault = (name = "ゲスト") => `こんにちは、${name}さん！`;

// 使用例
console.log(greet("太郎"));           // "こんにちは、太郎さん！"
console.log(add(5, 3));               // 8
console.log(greetWithDefault());      // "こんにちは、ゲストさん！"
```

## DOM操作

### 要素の取得

```javascript
// IDで取得
const header = document.getElementById("header");

// クラス名で取得（複数要素）
const buttons = document.getElementsByClassName("btn");

// タグ名で取得
const paragraphs = document.getElementsByTagName("p");

// CSSセレクタで取得（最初の要素）
const firstButton = document.querySelector(".btn");
const specificElement = document.querySelector("#main .content");

// CSSセレクタで取得（すべての要素）
const allButtons = document.querySelectorAll(".btn");
const allLinks = document.querySelectorAll("a[href^='https']");
```

### 要素の操作

```javascript
// 要素の作成
const newDiv = document.createElement("div");
const newText = document.createTextNode("新しいテキスト");

// 属性の操作
const link = document.querySelector("a");
link.setAttribute("href", "https://example.com");
link.getAttribute("href"); // "https://example.com"
link.removeAttribute("target");

// クラスの操作
const element = document.querySelector(".container");
element.classList.add("active");
element.classList.remove("inactive");
element.classList.toggle("highlighted");
element.classList.contains("active"); // true/false

// テキスト内容の変更
element.textContent = "新しいテキスト";
element.innerHTML = "<strong>HTML付きテキスト</strong>";

// スタイルの変更
element.style.color = "red";
element.style.backgroundColor = "yellow";
element.style.fontSize = "16px";
```

### 要素の追加・削除

```javascript
// 要素の追加
const parent = document.querySelector(".parent");
const child = document.createElement("div");
child.textContent = "新しい子要素";

parent.appendChild(child);               // 末尾に追加
parent.insertBefore(child, parent.firstChild); // 先頭に追加

// より柔軟な挿入
parent.insertAdjacentHTML("beforeend", "<p>HTML文字列</p>");
parent.insertAdjacentElement("afterbegin", child);

// 要素の削除
child.remove();                         // 要素自体を削除
parent.removeChild(child);              // 親から子要素を削除

// 要素の置換
const newElement = document.createElement("span");
newElement.textContent = "置換された要素";
parent.replaceChild(newElement, child);
```

## イベント処理

### イベントリスナーの基本

```javascript
// イベントリスナーの追加
const button = document.querySelector("#myButton");

// 基本的な書き方
button.addEventListener("click", function(event) {
  console.log("ボタンがクリックされました！");
  console.log("イベント:", event);
});

// アロー関数を使用
button.addEventListener("click", (event) => {
  console.log("ボタンがクリックされました！");
});

// 名前付き関数を使用
function handleButtonClick(event) {
  console.log("ボタンがクリックされました！");
  // イベントのデフォルト動作を防ぐ
  event.preventDefault();
  // イベントの伝播を停止
  event.stopPropagation();
}

button.addEventListener("click", handleButtonClick);

// イベントリスナーの削除
button.removeEventListener("click", handleButtonClick);
```

### 各種イベントの実装例

```javascript
// フォームの処理
const form = document.querySelector("#contactForm");
const nameInput = document.querySelector("#name");
const emailInput = document.querySelector("#email");

form.addEventListener("submit", (event) => {
  event.preventDefault(); // ページリロードを防ぐ
  
  const formData = {
    name: nameInput.value,
    email: emailInput.value
  };
  
  // バリデーション
  if (!formData.name || !formData.email) {
    alert("すべての項目を入力してください");
    return;
  }
  
  console.log("送信データ:", formData);
  // API送信処理などを実行
});

// 入力値の即座な検証
emailInput.addEventListener("input", (event) => {
  const email = event.target.value;
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  
  if (email && !emailRegex.test(email)) {
    event.target.style.borderColor = "red";
  } else {
    event.target.style.borderColor = "green";
  }
});

// キーボードイベント
document.addEventListener("keydown", (event) => {
  // Escキーでモーダルを閉じる
  if (event.key === "Escape") {
    closeModal();
  }
  
  // Ctrl+Sで保存
  if (event.ctrlKey && event.key === "s") {
    event.preventDefault();
    saveDocument();
  }
});

// マウスイベント
const draggableElement = document.querySelector(".draggable");

draggableElement.addEventListener("mousedown", (event) => {
  console.log("マウスダウン:", event.clientX, event.clientY);
});

draggableElement.addEventListener("mousemove", (event) => {
  // ドラッグ処理
});

draggableElement.addEventListener("mouseup", (event) => {
  console.log("マウスアップ");
});
```

### イベント委譲（Event Delegation）

```javascript
// 親要素にイベントリスナーを設定
const todoList = document.querySelector("#todoList");

todoList.addEventListener("click", (event) => {
  // 削除ボタンがクリックされた場合
  if (event.target.classList.contains("delete-btn")) {
    const todoItem = event.target.closest(".todo-item");
    todoItem.remove();
  }
  
  // チェックボックスがクリックされた場合
  if (event.target.classList.contains("todo-checkbox")) {
    const todoItem = event.target.closest(".todo-item");
    todoItem.classList.toggle("completed");
  }
});

// 動的に要素を追加
function addTodoItem(text) {
  const todoItem = document.createElement("div");
  todoItem.className = "todo-item";
  todoItem.innerHTML = `
    <input type="checkbox" class="todo-checkbox">
    <span class="todo-text">${text}</span>
    <button class="delete-btn">削除</button>
  `;
  todoList.appendChild(todoItem);
}
```

## 非同期処理

### Promise と async/await

```javascript
// Promise の基本
function fetchUserData(userId) {
  return new Promise((resolve, reject) => {
    // 模擬的な非同期処理
    setTimeout(() => {
      if (userId > 0) {
        resolve({
          id: userId,
          name: "太郎",
          email: "taro@example.com"
        });
      } else {
        reject(new Error("無効なユーザーID"));
      }
    }, 1000);
  });
}

// Promise の使用
fetchUserData(1)
  .then(user => {
    console.log("ユーザー情報:", user);
    return fetchUserPosts(user.id);
  })
  .then(posts => {
    console.log("投稿:", posts);
  })
  .catch(error => {
    console.error("エラー:", error.message);
  });

// async/await の使用
async function loadUserProfile(userId) {
  try {
    const user = await fetchUserData(userId);
    console.log("ユーザー情報:", user);
    
    const posts = await fetchUserPosts(user.id);
    console.log("投稿:", posts);
    
    return { user, posts };
  } catch (error) {
    console.error("エラー:", error.message);
    throw error;
  }
}

// 使用例
loadUserProfile(1)
  .then(profile => {
    console.log("プロファイル読み込み完了:", profile);
  })
  .catch(error => {
    console.error("プロファイル読み込み失敗:", error);
  });
```

### Fetch API

```javascript
// GET リクエスト
async function fetchData() {
  try {
    const response = await fetch("https://api.example.com/users");
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("データ取得エラー:", error);
    throw error;
  }
}

// POST リクエスト
async function createUser(userData) {
  try {
    const response = await fetch("https://api.example.com/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer token123"
      },
      body: JSON.stringify(userData)
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const result = await response.json();
    return result;
  } catch (error) {
    console.error("ユーザー作成エラー:", error);
    throw error;
  }
}

// 使用例
async function handleUserCreation() {
  const userData = {
    name: "花子",
    email: "hanako@example.com"
  };
  
  try {
    const newUser = await createUser(userData);
    console.log("新しいユーザー:", newUser);
    
    // UI更新
    displaySuccessMessage("ユーザーが正常に作成されました");
  } catch (error) {
    displayErrorMessage("ユーザーの作成に失敗しました");
  }
}
```

## 配列とオブジェクトの操作

### 配列の高階関数

```javascript
const users = [
  { id: 1, name: "太郎", age: 25, active: true },
  { id: 2, name: "花子", age: 30, active: false },
  { id: 3, name: "次郎", age: 28, active: true },
  { id: 4, name: "久美", age: 35, active: true }
];

// map - 配列の各要素を変換
const userNames = users.map(user => user.name);
console.log(userNames); // ["太郎", "花子", "次郎", "久美"]

const userDisplays = users.map(user => ({
  ...user,
  displayName: `${user.name} (${user.age}歳)`
}));

// filter - 条件に合う要素だけを抽出
const activeUsers = users.filter(user => user.active);
const youngUsers = users.filter(user => user.age < 30);

// find - 条件に合う最初の要素を取得
const specificUser = users.find(user => user.name === "太郎");

// reduce - 配列を単一の値に集約
const totalAge = users.reduce((sum, user) => sum + user.age, 0);
const averageAge = totalAge / users.length;

// some - 条件に合う要素が存在するかチェック
const hasActiveUser = users.some(user => user.active);

// every - すべての要素が条件に合うかチェック
const allActive = users.every(user => user.active);

// sort - 配列のソート
const sortedByAge = users.sort((a, b) => a.age - b.age);
const sortedByName = users.sort((a, b) => a.name.localeCompare(b.name));
```

### オブジェクトの操作

```javascript
const user = {
  name: "太郎",
  age: 25,
  email: "taro@example.com"
};

// 分割代入
const { name, age, email } = user;
console.log(name); // "太郎"

// 残りの属性を取得
const { name: userName, ...otherProps } = user;
console.log(otherProps); // { age: 25, email: "taro@example.com" }

// オブジェクトのマージ
const additionalInfo = { city: "東京", country: "日本" };
const completeUser = { ...user, ...additionalInfo };

// 動的なプロパティ名
const propertyName = "dynamicProp";
const dynamicObject = {
  [propertyName]: "動的な値",
  [`${propertyName}2`]: "別の動的な値"
};

// オブジェクトのキーと値を取得
const keys = Object.keys(user);        // ["name", "age", "email"]
const values = Object.values(user);    // ["太郎", 25, "taro@example.com"]
const entries = Object.entries(user);  // [["name", "太郎"], ["age", 25], ...]

// エントリーからオブジェクトを再構築
const rebuiltUser = Object.fromEntries(entries);
```

## 実践的な実装例

### 動的なToDoリスト

```javascript
class TodoApp {
  constructor() {
    this.todos = [];
    this.nextId = 1;
    this.init();
  }
  
  init() {
    this.setupEventListeners();
    this.render();
  }
  
  setupEventListeners() {
    const addForm = document.querySelector("#add-todo-form");
    const todoList = document.querySelector("#todo-list");
    const filterButtons = document.querySelectorAll(".filter-btn");
    
    addForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const input = e.target.querySelector("#todo-input");
      this.addTodo(input.value.trim());
      input.value = "";
    });
    
    todoList.addEventListener("click", (e) => {
      const todoId = parseInt(e.target.closest(".todo-item")?.dataset.id);
      
      if (e.target.classList.contains("toggle-btn")) {
        this.toggleTodo(todoId);
      } else if (e.target.classList.contains("delete-btn")) {
        this.deleteTodo(todoId);
      }
    });
    
    filterButtons.forEach(btn => {
      btn.addEventListener("click", (e) => {
        const filter = e.target.dataset.filter;
        this.setFilter(filter);
      });
    });
  }
  
  addTodo(text) {
    if (!text) return;
    
    const todo = {
      id: this.nextId++,
      text: text,
      completed: false,
      createdAt: new Date()
    };
    
    this.todos.push(todo);
    this.render();
  }
  
  toggleTodo(id) {
    const todo = this.todos.find(t => t.id === id);
    if (todo) {
      todo.completed = !todo.completed;
      this.render();
    }
  }
  
  deleteTodo(id) {
    this.todos = this.todos.filter(t => t.id !== id);
    this.render();
  }
  
  setFilter(filter) {
    this.currentFilter = filter;
    this.render();
    
    // フィルターボタンのアクティブ状態を更新
    document.querySelectorAll(".filter-btn").forEach(btn => {
      btn.classList.toggle("active", btn.dataset.filter === filter);
    });
  }
  
  getFilteredTodos() {
    switch (this.currentFilter) {
      case "active":
        return this.todos.filter(todo => !todo.completed);
      case "completed":
        return this.todos.filter(todo => todo.completed);
      default:
        return this.todos;
    }
  }
  
  render() {
    const todoList = document.querySelector("#todo-list");
    const filteredTodos = this.getFilteredTodos();
    
    todoList.innerHTML = filteredTodos.map(todo => `
      <div class="todo-item ${todo.completed ? 'completed' : ''}" data-id="${todo.id}">
        <button class="toggle-btn">${todo.completed ? '✓' : '○'}</button>
        <span class="todo-text">${this.escapeHtml(todo.text)}</span>
        <button class="delete-btn">削除</button>
      </div>
    `).join("");
    
    // 統計情報の更新
    this.updateStats();
  }
  
  updateStats() {
    const total = this.todos.length;
    const completed = this.todos.filter(todo => todo.completed).length;
    const active = total - completed;
    
    document.querySelector("#stats").innerHTML = `
      全体: ${total} | 完了: ${completed} | 未完了: ${active}
    `;
  }
  
  escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
  }
}

// アプリケーションの初期化
document.addEventListener("DOMContentLoaded", () => {
  new TodoApp();
});
```

### APIデータを使用した動的コンテンツ

```javascript
class UserManager {
  constructor() {
    this.users = [];
    this.loading = false;
    this.init();
  }
  
  async init() {
    await this.loadUsers();
    this.setupEventListeners();
  }
  
  async loadUsers() {
    this.setLoading(true);
    
    try {
      const response = await fetch("https://jsonplaceholder.typicode.com/users");
      this.users = await response.json();
      this.renderUsers();
    } catch (error) {
      this.showError("ユーザーデータの読み込みに失敗しました");
      console.error("Error loading users:", error);
    } finally {
      this.setLoading(false);
    }
  }
  
  setupEventListeners() {
    const searchInput = document.querySelector("#user-search");
    const sortSelect = document.querySelector("#user-sort");
    
    // 検索機能（デバウンス付き）
    let searchTimeout;
    searchInput.addEventListener("input", (e) => {
      clearTimeout(searchTimeout);
      searchTimeout = setTimeout(() => {
        this.filterUsers(e.target.value);
      }, 300);
    });
    
    // ソート機能
    sortSelect.addEventListener("change", (e) => {
      this.sortUsers(e.target.value);
    });
    
    // ユーザーカードのクリックイベント
    document.addEventListener("click", (e) => {
      if (e.target.closest(".user-card")) {
        const userId = parseInt(e.target.closest(".user-card").dataset.userId);
        this.showUserDetails(userId);
      }
    });
  }
  
  filterUsers(searchTerm) {
    const filtered = this.users.filter(user => 
      user.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      user.email.toLowerCase().includes(searchTerm.toLowerCase())
    );
    this.renderUsers(filtered);
  }
  
  sortUsers(sortBy) {
    let sorted = [...this.users];
    
    switch (sortBy) {
      case "name":
        sorted.sort((a, b) => a.name.localeCompare(b.name));
        break;
      case "email":
        sorted.sort((a, b) => a.email.localeCompare(b.email));
        break;
      case "company":
        sorted.sort((a, b) => a.company.name.localeCompare(b.company.name));
        break;
    }
    
    this.users = sorted;
    this.renderUsers();
  }
  
  renderUsers(usersToRender = this.users) {
    const container = document.querySelector("#users-container");
    
    if (usersToRender.length === 0) {
      container.innerHTML = "<p>ユーザーが見つかりません</p>";
      return;
    }
    
    container.innerHTML = usersToRender.map(user => `
      <div class="user-card" data-user-id="${user.id}">
        <h3>${this.escapeHtml(user.name)}</h3>
        <p><strong>Email:</strong> ${this.escapeHtml(user.email)}</p>
        <p><strong>Company:</strong> ${this.escapeHtml(user.company.name)}</p>
        <p><strong>City:</strong> ${this.escapeHtml(user.address.city)}</p>
      </div>
    `).join("");
  }
  
  async showUserDetails(userId) {
    const user = this.users.find(u => u.id === userId);
    if (!user) return;
    
    try {
      // ユーザーの投稿を取得
      const postsResponse = await fetch(`https://jsonplaceholder.typicode.com/posts?userId=${userId}`);
      const posts = await postsResponse.json();
      
      // モーダルで詳細を表示
      this.showModal(`
        <h2>${this.escapeHtml(user.name)}</h2>
        <p><strong>Email:</strong> ${this.escapeHtml(user.email)}</p>
        <p><strong>Phone:</strong> ${this.escapeHtml(user.phone)}</p>
        <p><strong>Website:</strong> <a href="http://${user.website}" target="_blank">${this.escapeHtml(user.website)}</a></p>
        <p><strong>Company:</strong> ${this.escapeHtml(user.company.name)}</p>
        <p><strong>Address:</strong> ${this.escapeHtml(user.address.street)}, ${this.escapeHtml(user.address.city)}</p>
        
        <h3>投稿 (${posts.length}件)</h3>
        <div class="posts-list">
          ${posts.map(post => `
            <div class="post-item">
              <h4>${this.escapeHtml(post.title)}</h4>
              <p>${this.escapeHtml(post.body)}</p>
            </div>
          `).join("")}
        </div>
      `);
    } catch (error) {
      this.showError("ユーザー詳細の読み込みに失敗しました");
    }
  }
  
  showModal(content) {
    const modal = document.createElement("div");
    modal.className = "modal";
    modal.innerHTML = `
      <div class="modal-content">
        <span class="close">&times;</span>
        ${content}
      </div>
    `;
    
    document.body.appendChild(modal);
    
    // モーダルを閉じる処理
    const closeModal = () => {
      document.body.removeChild(modal);
    };
    
    modal.querySelector(".close").addEventListener("click", closeModal);
    modal.addEventListener("click", (e) => {
      if (e.target === modal) closeModal();
    });
    
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") closeModal();
    });
  }
  
  setLoading(loading) {
    this.loading = loading;
    const loadingElement = document.querySelector("#loading");
    loadingElement.style.display = loading ? "block" : "none";
  }
  
  showError(message) {
    const errorDiv = document.createElement("div");
    errorDiv.className = "error-message";
    errorDiv.textContent = message;
    
    document.body.appendChild(errorDiv);
    
    setTimeout(() => {
      if (document.body.contains(errorDiv)) {
        document.body.removeChild(errorDiv);
      }
    }, 5000);
  }
  
  escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
  }
}

// アプリケーションの初期化
document.addEventListener("DOMContentLoaded", () => {
  new UserManager();
});
```

## モダンJavaScriptの機能

### テンプレートリテラル

```javascript
const name = "太郎";
const age = 25;

// 基本的な使用
const message = `こんにちは、${name}さん！あなたは${age}歳ですね。`;

// 複数行文字列
const htmlTemplate = `
  <div class="user-card">
    <h2>${name}</h2>
    <p>年齢: ${age}歳</p>
    <p>成人: ${age >= 20 ? "はい" : "いいえ"}</p>
  </div>
`;

// タグ付きテンプレートリテラル
function highlight(strings, ...values) {
  return strings.reduce((result, string, i) => {
    const value = values[i] ? `<mark>${values[i]}</mark>` : "";
    return result + string + value;
  }, "");
}

const highlighted = highlight`名前は${name}で、年齢は${age}歳です。`;
```

### 分割代入

```javascript
// 配列の分割代入
const colors = ["red", "green", "blue", "yellow"];
const [primary, secondary, ...others] = colors;
console.log(primary);   // "red"
console.log(secondary); // "green"
console.log(others);    // ["blue", "yellow"]

// オブジェクトの分割代入
const user = {
  name: "太郎",
  age: 25,
  email: "taro@example.com",
  address: {
    city: "東京",
    country: "日本"
  }
};

const { name, age, email, ...userInfo } = user;
const { address: { city, country } } = user; // ネストした分割代入

// 関数のパラメータで分割代入
function greetUser({ name, age = 0 }) {
  return `こんにちは、${name}さん！年齢は${age}歳ですね。`;
}

console.log(greetUser({ name: "花子", age: 30 }));
```

### クラスとモジュール

```javascript
// クラスの定義
class User {
  constructor(name, email) {
    this.name = name;
    this.email = email;
    this.createdAt = new Date();
  }
  
  // インスタンスメソッド
  greet() {
    return `こんにちは、${this.name}さん！`;
  }
  
  // ゲッター
  get displayName() {
    return `${this.name} <${this.email}>`;
  }
  
  // セッター
  set email(newEmail) {
    if (this.isValidEmail(newEmail)) {
      this._email = newEmail;
    } else {
      throw new Error("無効なメールアドレスです");
    }