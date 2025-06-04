    ======================
    React入門〜中級者向けガイド
    ======================

    .. contents:: 目次
    :depth: 3
    :local:

    React概要
    =========

    Reactとは
    ---------

    ReactはFacebookによって開発されたJavaScriptライブラリで、ユーザーインターフェース（UI）の構築に特化しています。コンポーネントベースのアーキテクチャを採用し、再利用可能なUIコンポーネントを作成できます。

    主な特徴
    --------

    - **コンポーネントベース**: UIを独立したコンポーネントに分割
    - **宣言的**: データの状態に応じてUIがどのように見えるべきかを記述
    - **Virtual DOM**: 効率的なDOM更新により高いパフォーマンスを実現
    - **一方向データフロー**: データの流れが予測しやすく、デバッグが容易

    開発環境の構築
    ==============

    Node.jsのインストール
    --------------------

    まず、Node.jsをインストールします:

    .. code-block:: bash

    # Node.jsの公式サイトからダウンロードするか
    # パッケージマネージャーを使用
    
    # macOSの場合（Homebrew）
    brew install node
    
    # Windowsの場合（Chocolatey）
    choco install nodejs

    Create React Appを使用したプロジェクト作成
    ----------------------------------------

    .. code-block:: bash

    # Create React Appのインストール
    npx create-react-app my-react-app
    
    # プロジェクトディレクトリに移動
    cd my-react-app
    
    # 開発サーバーの起動
    npm start

    プロジェクト構造
    ---------------

    .. code-block:: text

    my-react-app/
    ├── public/
    │   ├── index.html
    │   └── favicon.ico
    ├── src/
    │   ├── App.js
    │   ├── App.css
    │   ├── index.js
    │   ├── index.css
    │   └── components/
    ├── package.json
    └── README.md

    React基礎
    =========

    JSXの理解
    ---------

    JSXはJavaScriptの拡張構文で、HTMLライクな記法でUIを記述できます:

    .. code-block:: javascript

    // JSXの例
    const element = <h1>Hello, World!</h1>;
    
    // JavaScript式の埋め込み
    const name = 'React';
    const greeting = <h1>Hello, {name}!</h1>;
    
    // 複数行のJSX
    const multiLine = (
        <div>
        <h1>タイトル</h1>
        <p>内容</p>
        </div>
    );

    初めてのコンポーネント
    --------------------

    関数コンポーネントの作成:

    .. code-block:: javascript

    // src/components/Welcome.js
    function Welcome(props) {
        return <h1>Hello, {props.name}!</h1>;
    }
    
    export default Welcome;

    アロー関数を使用した書き方:

    .. code-block:: javascript

    const Welcome = (props) => {
        return <h1>Hello, {props.name}!</h1>;
    };
    
    export default Welcome;

    コンポーネントの使用:

    .. code-block:: javascript

    // src/App.js
    import Welcome from './components/Welcome';
    
    function App() {
        return (
        <div>
            <Welcome name="Alice" />
            <Welcome name="Bob" />
        </div>
        );
    }
    
    export default App;

    Propsの活用
    -----------

    Propsはコンポーネント間でデータを渡すための仕組みです:

    .. code-block:: javascript

    // ユーザー情報コンポーネント
    const UserCard = (props) => {
        return (
        <div className="user-card">
            <img src={props.avatar} alt="Avatar" />
            <h2>{props.name}</h2>
            <p>{props.email}</p>
            <p>年齢: {props.age}</p>
        </div>
        );
    };
    
    // 使用例
    const App = () => {
        return (
        <UserCard
            name="田中太郎"
            email="tanaka@example.com"
            age={30}
            avatar="/images/avatar.jpg"
        />
        );
    };

    Props の分割代入:

    .. code-block:: javascript

    const UserCard = ({ name, email, age, avatar }) => {
        return (
        <div className="user-card">
            <img src={avatar} alt="Avatar" />
            <h2>{name}</h2>
            <p>{email}</p>
            <p>年齢: {age}</p>
        </div>
        );
    };

    Stateとフック
    =============

    useStateフックの基本
    ------------------

    useStateを使用して状態管理を行います:

    .. code-block:: javascript

    import React, { useState } from 'react';
    
    const Counter = () => {
        const [count, setCount] = useState(0);
    
        return (
        <div>
            <p>カウント: {count}</p>
            <button onClick={() => setCount(count + 1)}>
            増加
            </button>
            <button onClick={() => setCount(count - 1)}>
            減少
            </button>
            <button onClick={() => setCount(0)}>
            リセット
            </button>
        </div>
        );
    };

    複数の状態管理:

    .. code-block:: javascript

    const UserProfile = () => {
        const [name, setName] = useState('');
        const [email, setEmail] = useState('');
        const [age, setAge] = useState(0);
    
        const handleSubmit = (e) => {
        e.preventDefault();
        console.log({ name, email, age });
        };
    
        return (
        <form onSubmit={handleSubmit}>
            <input
            type="text"
            placeholder="名前"
            value={name}
            onChange={(e) => setName(e.target.value)}
            />
            <input
            type="email"
            placeholder="メールアドレス"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            />
            <input
            type="number"
            placeholder="年齢"
            value={age}
            onChange={(e) => setAge(parseInt(e.target.value))}
            />
            <button type="submit">送信</button>
        </form>
        );
    };

    オブジェクトと配列の状態管理
    --------------------------

    .. code-block:: javascript

    const TodoList = () => {
        const [todos, setTodos] = useState([]);
        const [inputValue, setInputValue] = useState('');
    
        const addTodo = () => {
        if (inputValue.trim()) {
            setTodos([
            ...todos,
            {
                id: Date.now(),
                text: inputValue,
                completed: false
            }
            ]);
            setInputValue('');
        }
        };
    
        const toggleTodo = (id) => {
        setTodos(todos.map(todo =>
            todo.id === id
            ? { ...todo, completed: !todo.completed }
            : todo
        ));
        };
    
        const deleteTodo = (id) => {
        setTodos(todos.filter(todo => todo.id !== id));
        };
    
        return (
        <div>
            <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder="新しいタスク"
            />
            <button onClick={addTodo}>追加</button>
            
            <ul>
            {todos.map(todo => (
                <li key={todo.id}>
                <span
                    style={{
                    textDecoration: todo.completed ? 'line-through' : 'none'
                    }}
                    onClick={() => toggleTodo(todo.id)}
                >
                    {todo.text}
                </span>
                <button onClick={() => deleteTodo(todo.id)}>削除</button>
                </li>
            ))}
            </ul>
        </div>
        );
    };

    イベントハンドリング
    ==================

    基本的なイベント処理
    ------------------

    .. code-block:: javascript

    const EventExample = () => {
        const [message, setMessage] = useState('');
    
        const handleClick = () => {
        alert('ボタンがクリックされました！');
        };
    
        const handleInputChange = (e) => {
        setMessage(e.target.value);
        };
    
        const handleSubmit = (e) => {
        e.preventDefault();
        console.log('送信されたメッセージ:', message);
        };
    
        return (
        <div>
            <button onClick={handleClick}>クリック</button>
            
            <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={message}
                onChange={handleInputChange}
                placeholder="メッセージを入力"
            />
            <button type="submit">送信</button>
            </form>
            
            <p>入力中: {message}</p>
        </div>
        );
    };

    カスタムイベントハンドラー
    ------------------------

    .. code-block:: javascript

    const ProductList = () => {
        const [products] = useState([
        { id: 1, name: '商品A', price: 1000 },
        { id: 2, name: '商品B', price: 2000 },
        { id: 3, name: '商品C', price: 3000 }
        ]);
    
        const handlePurchase = (productId, productName) => {
        alert(`${productName}を購入しました（ID: ${productId}）`);
        };
    
        return (
        <div>
            {products.map(product => (
            <div key={product.id}>
                <h3>{product.name}</h3>
                <p>価格: ¥{product.price}</p>
                <button
                onClick={() => handlePurchase(product.id, product.name)}
                >
                購入
                </button>
            </div>
            ))}
        </div>
        );
    };

    useEffectフック
    ===============

    基本的な使用法
    --------------

    .. code-block:: javascript

    import React, { useState, useEffect } from 'react';
    
    const DataFetcher = () => {
        const [data, setData] = useState(null);
        const [loading, setLoading] = useState(true);
    
        useEffect(() => {
        // コンポーネントマウント時に実行
        const fetchData = async () => {
            try {
            const response = await fetch('https://api.example.com/data');
            const result = await response.json();
            setData(result);
            } catch (error) {
            console.error('データ取得エラー:', error);
            } finally {
            setLoading(false);
            }
        };
    
        fetchData();
        }, []); // 空の依存配列 = マウント時のみ実行
    
        if (loading) return <div>読み込み中...</div>;
    
        return (
        <div>
            <h2>取得したデータ</h2>
            <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
        );
    };

    依存配列とクリーンアップ
    ----------------------

    .. code-block:: javascript

    const Timer = () => {
        const [seconds, setSeconds] = useState(0);
        const [isActive, setIsActive] = useState(false);
    
        useEffect(() => {
        let interval = null;
    
        if (isActive) {
            interval = setInterval(() => {
            setSeconds(seconds => seconds + 1);
            }, 1000);
        }
    
        // クリーンアップ関数
        return () => {
            if (interval) {
            clearInterval(interval);
            }
        };
        }, [isActive]); // isActiveが変更されたときに実行
    
        const toggle = () => {
        setIsActive(!isActive);
        };
    
        const reset = () => {
        setSeconds(0);
        setIsActive(false);
        };
    
        return (
        <div>
            <div>時間: {seconds}秒</div>
            <button onClick={toggle}>
            {isActive ? '停止' : '開始'}
            </button>
            <button onClick={reset}>リセット</button>
        </div>
        );
    };

    条件付きレンダリング
    ==================

    基本的な条件分岐
    --------------

    .. code-block:: javascript

    const LoginStatus = ({ isLoggedIn, username }) => {
        if (isLoggedIn) {
        return <h1>おかえりなさい、{username}さん！</h1>;
        } else {
        return <h1>ログインしてください</h1>;
        }
    };
    
    // 三項演算子を使用
    const LoginButton = ({ isLoggedIn, onLogin, onLogout }) => {
        return (
        <button onClick={isLoggedIn ? onLogout : onLogin}>
            {isLoggedIn ? 'ログアウト' : 'ログイン'}
        </button>
        );
    };

    論理AND演算子の活用
    -----------------

    .. code-block:: javascript

    const NotificationBadge = ({ count }) => {
        return (
        <div>
            <span>通知</span>
            {count > 0 && (
            <span className="badge">{count}</span>
            )}
        </div>
        );
    };
    
    const AdminPanel = ({ user }) => {
        return (
        <div>
            <h1>ダッシュボード</h1>
            {user.isAdmin && (
            <div>
                <h2>管理者メニュー</h2>
                <button>ユーザー管理</button>
                <button>システム設定</button>
            </div>
            )}
        </div>
        );
    };

    リストとkey
    ===========

    基本的なリスト表示
    ----------------

    .. code-block:: javascript

    const StudentList = () => {
        const students = [
        { id: 1, name: '田中太郎', grade: 'A' },
        { id: 2, name: '佐藤花子', grade: 'B' },
        { id: 3, name: '鈴木一郎', grade: 'A' }
        ];
    
        return (
        <div>
            <h2>学生一覧</h2>
            <ul>
            {students.map(student => (
                <li key={student.id}>
                {student.name} - 成績: {student.grade}
                </li>
            ))}
            </ul>
        </div>
        );
    };

    動的なリスト操作
    --------------

    .. code-block:: javascript

    const ShoppingCart = () => {
        const [items, setItems] = useState([
        { id: 1, name: 'りんご', price: 100, quantity: 2 },
        { id: 2, name: 'バナナ', price: 150, quantity: 1 }
        ]);
    
        const updateQuantity = (id, newQuantity) => {
        setItems(items.map(item =>
            item.id === id
            ? { ...item, quantity: Math.max(0, newQuantity) }
            : item
        ));
        };
    
        const removeItem = (id) => {
        setItems(items.filter(item => item.id !== id));
        };
    
        const total = items.reduce((sum, item) => sum + item.price * item.quantity, 0);
    
        return (
        <div>
            <h2>ショッピングカート</h2>
            {items.map(item => (
            <div key={item.id} className="cart-item">
                <span>{item.name}</span>
                <span>¥{item.price}</span>
                <button onClick={() => updateQuantity(item.id, item.quantity - 1)}>
                -
                </button>
                <span>{item.quantity}</span>
                <button onClick={() => updateQuantity(item.id, item.quantity + 1)}>
                +
                </button>
                <button onClick={() => removeItem(item.id)}>削除</button>
            </div>
            ))}
            <div>合計: ¥{total}</div>
        </div>
        );
    };

    フォーム処理
    ============

    制御されたコンポーネント
    ----------------------

    .. code-block:: javascript

    const ContactForm = () => {
        const [formData, setFormData] = useState({
        name: '',
        email: '',
        subject: '',
        message: '',
        category: 'general'
        });
    
        const [errors, setErrors] = useState({});
    
        const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: value
        }));
        };
    
        const validateForm = () => {
        const newErrors = {};
    
        if (!formData.name.trim()) {
            newErrors.name = '名前は必須です';
        }
    
        if (!formData.email.trim()) {
            newErrors.email = 'メールアドレスは必須です';
        } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
            newErrors.email = '有効なメールアドレスを入力してください';
        }
    
        if (!formData.message.trim()) {
            newErrors.message = 'メッセージは必須です';
        }
    
        return newErrors;
        };
    
        const handleSubmit = (e) => {
        e.preventDefault();
        const newErrors = validateForm();
    
        if (Object.keys(newErrors).length === 0) {
            console.log('フォーム送信:', formData);
            // フォームリセット
            setFormData({
            name: '',
            email: '',
            subject: '',
            message: '',
            category: 'general'
            });
            setErrors({});
        } else {
            setErrors(newErrors);
        }
        };
    
        return (
        <form onSubmit={handleSubmit}>
            <div>
            <label>名前:</label>
            <input
                type="text"
                name="name"
                value={formData.name}
                onChange={handleChange}
            />
            {errors.name && <span className="error">{errors.name}</span>}
            </div>
    
            <div>
            <label>メールアドレス:</label>
            <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
            />
            {errors.email && <span className="error">{errors.email}</span>}
            </div>
    
            <div>
            <label>件名:</label>
            <input
                type="text"
                name="subject"
                value={formData.subject}
                onChange={handleChange}
            />
            </div>
    
            <div>
            <label>カテゴリー:</label>
            <select
                name="category"
                value={formData.category}
                onChange={handleChange}
            >
                <option value="general">一般</option>
                <option value="technical">技術</option>
                <option value="billing">請求</option>
            </select>
            </div>
    
            <div>
            <label>メッセージ:</label>
            <textarea
                name="message"
                value={formData.message}
                onChange={handleChange}
                rows="4"
            />
            {errors.message && <span className="error">{errors.message}</span>}
            </div>
    
            <button type="submit">送信</button>
        </form>
        );
    };

    コンポーネント設計
    ==================

    コンポーネントの分割
    ------------------

    .. code-block:: javascript

    // Header.js
    const Header = ({ title, user, onLogout }) => {
        return (
        <header>
            <h1>{title}</h1>
            <div>
            <span>こんにちは、{user.name}さん</span>
            <button onClick={onLogout}>ログアウト</button>
            </div>
        </header>
        );
    };
    
    // Sidebar.js
    const Sidebar = ({ items, activeItem, onItemClick }) => {
        return (
        <nav>
            <ul>
            {items.map(item => (
                <li
                key={item.id}
                className={activeItem === item.id ? 'active' : ''}
                onClick={() => onItemClick(item.id)}
                >
                {item.label}
                </li>
            ))}
            </ul>
        </nav>
        );
    };
    
    // MainContent.js
    const MainContent = ({ content }) => {
        return (
        <main>
            {content}
        </main>
        );
    };
    
    // App.js
    const App = () => {
        const [user] = useState({ name: '田中太郎', id: 1 });
        const [activeItem, setActiveItem] = useState(1);
    
        const menuItems = [
        { id: 1, label: 'ダッシュボード' },
        { id: 2, label: 'プロファイル' },
        { id: 3, label: '設定' }
        ];
    
        const handleLogout = () => {
        console.log('ログアウト処理');
        };
    
        return (
        <div className="app">
            <Header
            title="マイアプリ"
            user={user}
            onLogout={handleLogout}
            />
            <div className="app-body">
            <Sidebar
                items={menuItems}
                activeItem={activeItem}
                onItemClick={setActiveItem}
            />
            <MainContent content={<div>メインコンテンツ</div>} />
            </div>
        </div>
        );
    };

    カスタムフック
    ==============

    再利用可能なロジックの抽出
    ------------------------

    .. code-block:: javascript

    // useLocalStorage.js
    import { useState, useEffect } from 'react';
    
    const useLocalStorage = (key, initialValue) => {
        const [storedValue, setStoredValue] = useState(() => {
        try {
            const item = window.localStorage.getItem(key);
            return item ? JSON.parse(item) : initialValue;
        } catch (error) {
            console.error('LocalStorage読み込みエラー:', error);
            return initialValue;
        }
        });
    
        const setValue = (value) => {
        try {
            setStoredValue(value);
            window.localStorage.setItem(key, JSON.stringify(value));
        } catch (error) {
            console.error('LocalStorage保存エラー:', error);
        }
        };
    
        return [storedValue, setValue];
    };
    
    // useFetch.js
    import { useState, useEffect } from 'react';
    
    const useFetch = (url) => {
        const [data, setData] = useState(null);
        const [loading, setLoading] = useState(true);
        const [error, setError] = useState(null);
    
        useEffect(() => {
        const fetchData = async () => {
            try {
            setLoading(true);
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const result = await response.json();
            setData(result);
            } catch (err) {
            setError(err.message);
            } finally {
            setLoading(false);
            }
        };
    
        fetchData();
        }, [url]);
    
        return { data, loading, error };
    };
    
    // 使用例
    const UserProfile = () => {
        const [preferences, setPreferences] = useLocalStorage('userPreferences', {
        theme: 'light',
        language: 'ja'
        });
    
        const { data: userData, loading, error } = useFetch('/api/user/profile');
    
        if (loading) return <div>読み込み中...</div>;
        if (error) return <div>エラー: {error}</div>;
    
        return (
        <div>
            <h1>{userData.name}のプロフィール</h1>
            <div>
            <label>
                テーマ:
                <select
                value={preferences.theme}
                onChange={(e) => setPreferences({
                    ...preferences,
                    theme: e.target.value
                })}
                >
                <option value="light">ライト</option>
                <option value="dark">ダーク</option>
                </select>
            </label>
            </div>
        </div>
        );
    };

    実践的なサンプルアプリケーション
    ==============================

    Todo管理アプリケーション
    ----------------------

    .. code-block:: javascript

    import React, { useState, useEffect } from 'react';
    
    const TodoApp = () => {
        const [todos, setTodos] = useState([]);
        const [inputValue, setInputValue] = useState('');
        const [filter, setFilter] = useState('all');
        const [editingId, setEditingId] = useState(null);
        const [editingText, setEditingText] = useState('');
    
        // LocalStorageからのデータ読み込み
        useEffect(() => {
        const savedTodos = localStorage.getItem('todos');
        if (savedTodos) {
            setTodos(JSON.parse(savedTodos));
        }
        }, []);
    
        // LocalStorageへの保存
        useEffect(() => {
        localStorage.setItem('todos', JSON.stringify(todos));
        }, [todos]);
    
        const addTodo = () => {
        if (inputValue.trim()) {
            const newTodo = {
            id: Date.now(),
            text: inputValue.trim(),
            completed: false,
            createdAt: new Date().toISOString()
            };
            setTodos([newTodo, ...todos]);
            setInputValue('');
        }
        };
    
        const toggleTodo = (id) => {
        setTodos(todos.map(todo =>
            todo.id === id
            ? { ...todo, completed: !todo.completed }
            : todo
        ));
        };
    
        const deleteTodo = (id) => {
        setTodos(todos.filter(todo => todo.id !== id));
        };
    
        const startEditing = (id, text) => {
        setEditingId(id);
        setEditingText(text);
        };
    
        const saveEdit = () => {
        if (editingText.trim()) {
            setTodos(todos.map(todo =>
            todo.id === editingId
                ? { ...todo, text: editingText.trim() }
                : todo
            ));
        }
        setEditingId(null);
        setEditingText('');
        };
    
        const cancelEdit = () => {
        setEditingId(null);
        setEditingText('');
        };
    
        const clearCompleted = () => {
        setTodos(todos.filter(todo => !todo.completed));
        };
    
        const filteredTodos = todos.filter(todo => {
        switch (filter) {
            case 'active':
            return !todo.completed;
            case 'completed':
            return todo.completed;
            default:
            return true;
        }
        });
    
        const completedCount = todos.filter(todo => todo.completed).length;
        const activeCount = todos.length - completedCount;
    
        return (
        <div className="todo-app">
            <h1>Todo管理</h1>
            
            <div className="input-section">
            <input
                type="text"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && addTodo()}
                placeholder="新しいタスクを入力..."
            />
            <button onClick={addTodo}>追加</button>
            </div>
    
            <div className="filter-section">
            <button
                className={filter === 'all' ? 'active' : ''}
                onClick={() => setFilter('all')}
            >
                すべて ({todos.length})
            </button>
            <button
                className={filter === 'active' ? 'active' : ''}
                onClick={() => setFilter('active')}
            >
                未完了 ({activeCount})
            </button>
            <button
                className={filter === 'completed' ? 'active' : ''}
                onClick={() => setFilter('completed')}
            >
                完了済み ({completedCount})
            </button>
            </div>
    
            <div className="todos-section">
            {filteredTodos.map(todo => (
                <div key={todo.id} className="todo-item">
                <input
                    type="checkbox"
                    checked={todo.completed}
                    onChange={() => toggleTodo(todo.id)}
                />
                
                {editingId === todo.id ? (
                    <div className="editing">
                    <input
                        type="text"
                        value={editingText}
                        onChange={(e) => setEditingText(e.target.value)}
                        onKeyPress={(e) => {
                        if (e.key === 'Enter') saveEdit();
                        if (e.key === 'Escape') cancelEdit();
                        }}
                        autoFocus
                    />
                    <button onClick={saveEdit}>保存</button>
                    <button onClick={cancelEdit}>キャンセル</button>
                    </div>
                ) : (
                    <div className="todo-content">
                    <span
                        className={todo.completed ? 'completed' : ''}
                        onDoubleClick={() => startEditing(todo.id, todo.text)}
                    >
                        {todo.text}
                    </span>
                    <button onClick={() => startEditing(todo.id, todo.text)}>
                        編集
                    </button>
                    <button onClick={() => deleteTodo(todo.id)}>
                        削除
                    </button>
                    </div>
                )}
                </div>
            ))}
            </div>

            {completedCount > 0 && (
            <div className="actions">
                <button onClick={clearCompleted}>
                完了済みタスクを削除
                </button>
            </div>
            )}
        </div>
        );
    };

    export default TodoApp;

    Context APIを使用した状態管理
    ============================

    グローバル状態の管理
    ------------------

    .. code-block:: javascript

    // contexts/AuthContext.js
    import React, { createContext, useContext, useReducer } from 'react';

    const AuthContext = createContext();

    const authReducer = (state, action) => {
        switch (action.type) {
        case 'LOGIN':
            return {
            ...state,
            user: action.payload,
            isAuthenticated: true,
            loading: false
            };
        case 'LOGOUT':
            return {
            ...state,
            user: null,
            isAuthenticated: false,
            loading: false
            };
        case 'SET_LOADING':
            return {
            ...state,
            loading: action.payload
            };
        default:
            return state;
        }
    };

    export const AuthProvider = ({ children }) => {
        const [state, dispatch] = useReducer(authReducer, {
        user: null,
        isAuthenticated: false,
        loading: true
        });

        const login = async (email, password) => {
        dispatch({ type: 'SET_LOADING', payload: true });
        try {
            // API呼び出しをシミュレート
            const response = await fetch('/api/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
            });
            
            if (response.ok) {
            const user = await response.json();
            dispatch({ type: 'LOGIN', payload: user });
            return { success: true };
            } else {
            throw new Error('ログインに失敗しました');
            }
        } catch (error) {
            dispatch({ type: 'SET_LOADING', payload: false });
            return { success: false, error: error.message };
        }
        };

        const logout = () => {
        dispatch({ type: 'LOGOUT' });
        };

        return (
        <AuthContext.Provider value={{
            ...state,
            login,
            logout
        }}>
            {children}
        </AuthContext.Provider>
        );
    };

    export const useAuth = () => {
        const context = useContext(AuthContext);
        if (!context) {
        throw new Error('useAuth must be used within an AuthProvider');
        }
        return context;
    };

    // components/LoginForm.js
    import React, { useState } from 'react';
    import { useAuth } from '../contexts/AuthContext';

    const LoginForm = () => {
        const [email, setEmail] = useState('');
        const [password, setPassword] = useState('');
        const [error, setError] = useState('');
        const { login, loading } = useAuth();

        const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        
        const result = await login(email, password);
        if (!result.success) {
            setError(result.error);
        }
        };

        return (
        <form onSubmit={handleSubmit}>
            <h2>ログイン</h2>
            {error && <div className="error">{error}</div>}
            
            <div>
            <label>メールアドレス:</label>
            <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
            />
            </div>
            
            <div>
            <label>パスワード:</label>
            <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
            />
            </div>
            
            <button type="submit" disabled={loading}>
            {loading ? 'ログイン中...' : 'ログイン'}
            </button>
        </form>
        );
    };

    パフォーマンス最適化
    ==================

    React.memoの使用
    ---------------

    .. code-block:: javascript

    import React, { memo, useState, useCallback } from 'react';

    // メモ化されたコンポーネント
    const ExpensiveComponent = memo(({ data, onUpdate }) => {
        console.log('ExpensiveComponent がレンダリングされました');
        
        return (
        <div>
            <h3>データ: {data.name}</h3>
            <p>値: {data.value}</p>
            <button onClick={() => onUpdate(data.id)}>
            更新
            </button>
        </div>
        );
    });

    // カスタム比較関数を使用したメモ化
    const UserCard = memo(({ user, isSelected, onSelect }) => {
        return (
        <div className={`user-card ${isSelected ? 'selected' : ''}`}>
            <h4>{user.name}</h4>
            <p>{user.email}</p>
            <button onClick={() => onSelect(user.id)}>
            選択
            </button>
        </div>
        );
    }, (prevProps, nextProps) => {
        // カスタム比較関数
        return (
        prevProps.user.id === nextProps.user.id &&
        prevProps.user.name === nextProps.user.name &&
        prevProps.user.email === nextProps.user.email &&
        prevProps.isSelected === nextProps.isSelected
        );
    });

    useCallbackとuseMemoの活用
    ------------------------

    .. code-block:: javascript

    import React, { useState, useCallback, useMemo } from 'react';

    const DataProcessor = () => {
        const [data, setData] = useState([]);
        const [filter, setFilter] = useState('');
        const [sortOrder, setSortOrder] = useState('asc');

        // 高コストな計算をメモ化
        const processedData = useMemo(() => {
        console.log('データ処理を実行中...');
        
        let filtered = data.filter(item =>
            item.name.toLowerCase().includes(filter.toLowerCase())
        );

        return filtered.sort((a, b) => {
            if (sortOrder === 'asc') {
            return a.name.localeCompare(b.name);
            } else {
            return b.name.localeCompare(a.name);
            }
        });
        }, [data, filter, sortOrder]);

        // コールバック関数をメモ化
        const handleAddItem = useCallback((newItem) => {
        setData(prevData => [...prevData, newItem]);
        }, []);

        const handleDeleteItem = useCallback((id) => {
        setData(prevData => prevData.filter(item => item.id !== id));
        }, []);

        const handleUpdateItem = useCallback((id, updates) => {
        setData(prevData =>
            prevData.map(item =>
            item.id === id ? { ...item, ...updates } : item
            )
        );
        }, []);

        return (
        <div>
            <div className="controls">
            <input
                type="text"
                placeholder="フィルター..."
                value={filter}
                onChange={(e) => setFilter(e.target.value)}
            />
            <select
                value={sortOrder}
                onChange={(e) => setSortOrder(e.target.value)}
            >
                <option value="asc">昇順</option>
                <option value="desc">降順</option>
            </select>
            </div>

            <div className="data-list">
            {processedData.map(item => (
                <DataItem
                key={item.id}
                item={item}
                onUpdate={handleUpdateItem}
                onDelete={handleDeleteItem}
                />
            ))}
            </div>

            <AddItemForm onAdd={handleAddItem} />
        </div>
        );
    };

    エラーハンドリング
    ================

    Error Boundaryの実装
    -------------------

    .. code-block:: javascript

    import React from 'react';

    class ErrorBoundary extends React.Component {
        constructor(props) {
        super(props);
        this.state = { hasError: false, error: null, errorInfo: null };
        }

        static getDerivedStateFromError(error) {
        // エラーが発生したときに状態を更新
        return { hasError: true };
        }

        componentDidCatch(error, errorInfo) {
        // エラーの詳細を記録
        this.setState({
            error: error,
            errorInfo: errorInfo
        });

        // エラーログを送信（実際のアプリでは）
        console.error('Error Boundary がエラーをキャッチしました:', error, errorInfo);
        }

        render() {
        if (this.state.hasError) {
            return (
            <div className="error-boundary">
                <h2>申し訳ございません。エラーが発生しました。</h2>
                <p>ページを再読み込みしてください。</p>
                
                {process.env.NODE_ENV === 'development' && (
                <details style={{ whiteSpace: 'pre-wrap' }}>
                    <summary>エラーの詳細</summary>
                    {this.state.error && this.state.error.toString()}
                    <br />
                    {this.state.errorInfo.componentStack}
                </details>
                )}
                
                <button onClick={() => window.location.reload()}>
                ページを再読み込み
                </button>
            </div>
            );
        }

        return this.props.children;
        }
    }

    // 使用例
    const App = () => {
        return (
        <ErrorBoundary>
            <Header />
            <Main />
            <Footer />
        </ErrorBoundary>
        );
    };

    非同期処理のエラーハンドリング
    ---------------------------

    .. code-block:: javascript

    import React, { useState, useEffect } from 'react';

    const useAsyncOperation = (asyncFunction) => {
        const [data, setData] = useState(null);
        const [loading, setLoading] = useState(false);
        const [error, setError] = useState(null);

        const execute = async (...args) => {
        try {
            setLoading(true);
            setError(null);
            const result = await asyncFunction(...args);
            setData(result);
            return result;
        } catch (err) {
            setError(err.message);
            throw err;
        } finally {
            setLoading(false);
        }
        };

        return { data, loading, error, execute };
    };

    const DataFetcher = ({ url }) => {
        const [retryCount, setRetryCount] = useState(0);
        const maxRetries = 3;

        const { data, loading, error, execute } = useAsyncOperation(
        async (fetchUrl) => {
            const response = await fetch(fetchUrl);
            if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }
            return response.json();
        }
        );

        useEffect(() => {
        execute(url);
        }, [url]);

        const handleRetry = () => {
        if (retryCount < maxRetries) {
            setRetryCount(prev => prev + 1);
            execute(url);
        }
        };

        if (loading) {
        return <div className="loading">読み込み中...</div>;
        }

        if (error) {
        return (
            <div className="error-container">
            <h3>エラーが発生しました</h3>
            <p>{error}</p>
            {retryCount < maxRetries && (
                <button onClick={handleRetry}>
                再試行 ({retryCount + 1}/{maxRetries + 1})
                </button>
            )}
            {retryCount >= maxRetries && (
                <p>最大再試行回数に達しました。後でもう一度お試しください。</p>
            )}
            </div>
        );
        }

        return (
        <div className="data-container">
            <h3>取得したデータ</h3>
            <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
        );
    };

    テスト
    ======

    React Testing Libraryを使用したテスト
    -----------------------------------

    .. code-block:: javascript

    // Counter.test.js
    import React from 'react';
    import { render, screen, fireEvent } from '@testing-library/react';
    import '@testing-library/jest-dom';
    import Counter from './Counter';

    describe('Counter コンポーネント', () => {
        test('初期値が0で表示される', () => {
        render(<Counter />);
        const countElement = screen.getByText('カウント: 0');
        expect(countElement).toBeInTheDocument();
        });

        test('増加ボタンをクリックするとカウントが増える', () => {
        render(<Counter />);
        const incrementButton = screen.getByText('増加');
        
        fireEvent.click(incrementButton);
        
        expect(screen.getByText('カウント: 1')).toBeInTheDocument();
        });

        test('減少ボタンをクリックするとカウントが減る', () => {
        render(<Counter />);
        const decrementButton = screen.getByText('減少');
        
        fireEvent.click(decrementButton);
        
        expect(screen.getByText('カウント: -1')).toBeInTheDocument();
        });

        test('リセットボタンをクリックするとカウントが0になる', () => {
        render(<Counter />);
        const incrementButton = screen.getByText('増加');
        const resetButton = screen.getByText('リセット');
        
        // カウントを増やす
        fireEvent.click(incrementButton);
        fireEvent.click(incrementButton);
        
        // リセット
        fireEvent.click(resetButton);
        
        expect(screen.getByText('カウント: 0')).toBeInTheDocument();
        });
    });

    // フォームのテスト例
    // LoginForm.test.js
    import React from 'react';
    import { render, screen, fireEvent, waitFor } from '@testing-library/react';
    import userEvent from '@testing-library/user-event';
    import LoginForm from './LoginForm';

    describe('LoginForm コンポーネント', () => {
        test('フォーム要素が正しく表示される', () => {
        render(<LoginForm />);
        
        expect(screen.getByLabelText('メールアドレス:')).toBeInTheDocument();
        expect(screen.getByLabelText('パスワード:')).toBeInTheDocument();
        expect(screen.getByRole('button', { name: 'ログイン' })).toBeInTheDocument();
        });

        test('無効なメールアドレスでエラーが表示される', async () => {
        const user = userEvent.setup();
        render(<LoginForm />);
        
        const emailInput = screen.getByLabelText('メールアドレス:');
        const submitButton = screen.getByRole('button', { name: 'ログイン' });
        
        await user.type(emailInput, 'invalid-email');
        await user.click(submitButton);
        
        await waitFor(() => {
            expect(screen.getByText('有効なメールアドレスを入力してください')).toBeInTheDocument();
        });
        });

        test('正しい情報でログイン処理が呼ばれる', async () => {
        const mockOnLogin = jest.fn();
        const user = userEvent.setup();
        
        render(<LoginForm onLogin={mockOnLogin} />);
        
        const emailInput = screen.getByLabelText('メールアドレス:');
        const passwordInput = screen.getByLabelText('パスワード:');
        const submitButton = screen.getByRole('button', { name: 'ログイン' });
        
        await user.type(emailInput, 'test@example.com');
        await user.type(passwordInput, 'password123');
        await user.click(submitButton);
        
        expect(mockOnLogin).toHaveBeenCalledWith({
            email: 'test@example.com',
            password: 'password123'
        });
        });
    });

    デプロイメント
    ==============

    本番環境への準備
    --------------

    .. code-block:: bash

    # 本番用ビルドの作成
    npm run build

    # ビルドファイルの確認
    ls -la build/

    # 本番環境用の環境変数設定
    # .env.production
    REACT_APP_API_URL=https://api.production.com
    REACT_APP_ENV=production

    静的ホスティングサービスへのデプロイ
    ----------------------------------

    .. code-block:: bash

    # Netlifyへのデプロイ
    npm install -g netlify-cli
    netlify deploy --prod --dir=build

    # Vercelへのデプロイ
    npm install -g vercel
    vercel --prod

    # GitHub Pagesへのデプロイ
    npm install --save-dev gh-pages
    
    # package.jsonに追加：
    # "homepage": "https://username.github.io/repository-name",
    # "scripts": {
    #   "predeploy": "npm run build",
    #   "deploy": "gh-pages -d build"
    # }
    
    npm run deploy

    まとめ
    ======

    学習のポイント
    --------------

    Reactを効果的に学習し、活用するためのポイント：

    1. **基礎をしっかりと理解する**
    - JSXの記法とJavaScriptとの違い
    - コンポーネントの概念と再利用性
    - PropsとStateの使い分け

    2. **実践的なプロジェクトを作る**
    - Todoアプリやカウンターから始める
    - 段階的に機能を追加していく
    - 実際に動くものを作ることで理解を深める

    3. **Reactの思想を理解する**
    - 一方向データフロー
    - 宣言的UI
    - コンポーネントの責任分割

    4. **モダンなReactを学ぶ**
    - Hooksを中心とした関数コンポーネント
    - useEffectによる副作用の管理
    - Context APIによる状態管理

    5. **パフォーマンスを意識する**
    - 不要なレンダリングを避ける
    - メモ化の適切な使用
    - バンドルサイズの最適化

    次のステップ
    ------------

    さらに学習を進めるための推奨事項：

    - **状態管理ライブラリ**: Redux、Zustand、Recoilなど
    - **ルーティング**: React Router
    - **スタイリング**: Styled Components、Emotion、Tailwind CSS
    - **フォーム管理**: React Hook Form、Formik
    - **テスト**: Jest、React Testing Library
    - **TypeScript**: 型安全性の向上
    - **Next.js**: サーバーサイドレンダリングとフルスタック開発

    参考リソース
    ------------

    - **公式ドキュメント**: https://react.dev/
    - **React Tutorial**: https://react.dev/learn/tutorial-tic-tac-toe
    - **Create React App**: https://create-react-app.dev/
    - **React Developer Tools**: ブラウザ拡張機能