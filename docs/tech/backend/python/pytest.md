# pytest入門ガイド

pytestは、Pythonのテストフレームワークの中でも最も人気が高く、使いやすいツールです。シンプルな構文でテストを書くことができ、豊富な機能を提供します。

## pytestとは

pytestは、Python用の成熟したフル機能のテストフレームワークです。小さなユニットテストから複雑な機能テストまで、幅広いテストをサポートします。

### pytestの特徴

- **シンプルな構文**: assert文を使った直感的なテスト記述
- **自動発見**: テストファイルとテスト関数の自動検出
- **豊富なプラグイン**: 拡張機能による機能追加
- **詳細なレポート**: テスト失敗時の詳細な情報表示
- **フィクスチャ**: テストデータの効率的な管理

## pytestのインストール

### pipを使用したインストール

```bash
# pytestのインストール
pip install pytest

# バージョン確認
pytest --version

# 追加で便利なプラグインもインストール
pip install pytest-cov pytest-mock pytest-html
```

### 仮想環境での使用（推奨）

```bash
# 仮想環境の作成
python -m venv pytest_env

# 仮想環境の有効化（Windows）
pytest_env\Scripts\activate

# 仮想環境の有効化（Mac/Linux）
source pytest_env/bin/activate

# pytestのインストール
pip install pytest
```

## 基本的なテストの書き方

### 最初のテスト

まず、テスト対象のコードを作成します。

```python
# calculator.py
def add(a, b):
    """2つの数値を足し算する関数"""
    return a + b

def subtract(a, b):
    """2つの数値を引き算する関数"""
    return a - b

def multiply(a, b):
    """2つの数値を掛け算する関数"""
    return a * b

def divide(a, b):
    """2つの数値を割り算する関数"""
    if b == 0:
        raise ValueError("0で割ることはできません")
    return a / b

def is_even(number):
    """数値が偶数かどうかを判定する関数"""
    return number % 2 == 0
```

次に、テストコードを作成します。

```python
# test_calculator.py
import pytest
from calculator import add, subtract, multiply, divide, is_even

def test_add():
    """足し算のテスト"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """引き算のテスト"""
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(-1, -1) == 0

def test_multiply():
    """掛け算のテスト"""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_divide():
    """割り算のテスト"""
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5
    assert divide(-6, 2) == -3

def test_divide_by_zero():
    """0で割る場合のテスト"""
    with pytest.raises(ValueError, match="0で割ることはできません"):
        divide(5, 0)

def test_is_even():
    """偶数判定のテスト"""
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    assert is_even(-2) == True
```

### テストの実行

```bash
# すべてのテストを実行
pytest

# 詳細出力で実行
pytest -v

# 特定のファイルのテストを実行
pytest test_calculator.py

# 特定のテスト関数を実行
pytest test_calculator.py::test_add

# カバレッジと一緒に実行
pytest --cov=calculator
```

## テストの基本概念

### アサーション（assertion）

```python
# test_assertions.py
def test_basic_assertions():
    """基本的なアサーションの例"""
    # 等価性のテスト
    assert 2 + 2 == 4
    assert "hello" == "hello"
    
    # 不等式のテスト
    assert 5 > 3
    assert 2 < 10
    
    # メンバーシップのテスト
    assert "a" in "abc"
    assert 2 in [1, 2, 3]
    
    # 真偽値のテスト
    assert True
    assert not False
    
    # None のテスト
    result = None
    assert result is None

def test_string_assertions():
    """文字列のアサーション例"""
    text = "Hello, World!"
    
    assert text.startswith("Hello")
    assert text.endswith("!")
    assert "World" in text
    assert text.upper() == "HELLO, WORLD!"

def test_list_assertions():
    """リストのアサーション例"""
    numbers = [1, 2, 3, 4, 5]
    
    assert len(numbers) == 5
    assert numbers[0] == 1
    assert numbers[-1] == 5
    assert 3 in numbers
    assert max(numbers) == 5
```

### 例外のテスト

```python
# test_exceptions.py
import pytest

def divide_numbers(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    return a / b

def test_zero_division():
    """0で割る場合の例外テスト"""
    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)

def test_zero_division_with_message():
    """例外メッセージもチェック"""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide_numbers(10, 0)

def test_type_error():
    """型エラーのテスト"""
    with pytest.raises(TypeError):
        divide_numbers("10", 2)
    
    with pytest.raises(TypeError):
        divide_numbers(10, "2")

def test_exception_info():
    """例外情報を詳しく調べる"""
    with pytest.raises(ZeroDivisionError) as exc_info:
        divide_numbers(10, 0)
    
    assert str(exc_info.value) == "Cannot divide by zero"
    assert exc_info.type == ZeroDivisionError
```

## パラメータ化テスト

### 基本的なパラメータ化

```python
# test_parameterized.py
import pytest
from calculator import add, multiply, is_even

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5),
    (2.5, 1.5, 4.0),
])
def test_add_parametrized(a, b, expected):
    """パラメータ化された足し算テスト"""
    assert add(a, b) == expected

@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, False),
    (0, True),
    (-2, True),
    (-3, False),
    (100, True),
    (101, False),
])
def test_is_even_parametrized(number, expected):
    """パラメータ化された偶数判定テスト"""
    assert is_even(number) == expected

@pytest.mark.parametrize("a, b", [
    (2, 3),
    (4, 5),
    (1, 7),
])
def test_multiply_commutative(a, b):
    """掛け算の交換法則のテスト"""
    assert multiply(a, b) == multiply(b, a)
```

### 複雑なパラメータ化

```python
# test_complex_parametrized.py
import pytest

# テストデータを辞書で定義
test_data = [
    {"input": "hello", "expected": "HELLO", "desc": "小文字を大文字に"},
    {"input": "WORLD", "expected": "WORLD", "desc": "大文字はそのまま"},
    {"input": "Hello World", "expected": "HELLO WORLD", "desc": "混在文字列"},
    {"input": "", "expected": "", "desc": "空文字列"},
]

@pytest.mark.parametrize("test_case", test_data)
def test_upper_case(test_case):
    """大文字変換のテスト"""
    result = test_case["input"].upper()
    assert result == test_case["expected"], f"Failed: {test_case['desc']}"

# 複数のパラメータを組み合わせ
@pytest.mark.parametrize("operation", ["add", "multiply"])
@pytest.mark.parametrize("a, b", [(1, 2), (3, 4), (5, 6)])
def test_operations(operation, a, b):
    """複数の演算の組み合わせテスト"""
    if operation == "add":
        result = add(a, b)
        expected = a + b
    elif operation == "multiply":
        result = multiply(a, b)
        expected = a * b
    
    assert result == expected
```

## フィクスチャ（Fixture）

### 基本的なフィクスチャ

```python
# test_fixtures.py
import pytest

# テスト用のサンプルクラス
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.balance

@pytest.fixture
def empty_account():
    """残高0の口座を作成するフィクスチャ"""
    return BankAccount()

@pytest.fixture
def account_with_money():
    """残高1000の口座を作成するフィクスチャ"""
    return BankAccount(1000)

def test_empty_account_balance(empty_account):
    """空口座の残高テスト"""
    assert empty_account.get_balance() == 0

def test_deposit(empty_account):
    """入金テスト"""
    assert empty_account.deposit(100) == True
    assert empty_account.get_balance() == 100

def test_withdraw_success(account_with_money):
    """出金成功テスト"""
    assert account_with_money.withdraw(500) == True
    assert account_with_money.get_balance() == 500

def test_withdraw_insufficient_funds(account_with_money):
    """残高不足での出金テスト"""
    assert account_with_money.withdraw(1500) == False
    assert account_with_money.get_balance() == 1000
```

### セットアップとティアダウン

```python
# test_setup_teardown.py
import pytest
import tempfile
import os

@pytest.fixture
def temp_file():
    """一時ファイルを作成・削除するフィクスチャ"""
    # セットアップ: 一時ファイルを作成
    fd, temp_path = tempfile.mkstemp(suffix='.txt')
    os.close(fd)
    
    # テスト関数にファイルパスを渡す
    yield temp_path
    
    # ティアダウン: ファイルを削除
    if os.path.exists(temp_path):
        os.remove(temp_path)

def test_file_operations(temp_file):
    """ファイル操作のテスト"""
    # ファイルに書き込み
    with open(temp_file, 'w') as f:
        f.write("Hello, World!")
    
    # ファイルから読み込み
    with open(temp_file, 'r') as f:
        content = f.read()
    
    assert content == "Hello, World!"
    assert os.path.exists(temp_file)

@pytest.fixture(scope="module")
def database_connection():
    """モジュール全体で使用するデータベース接続"""
    print("\nデータベースに接続中...")
    connection = {"connected": True, "data": []}
    
    yield connection
    
    print("\nデータベース接続を閉じています...")
    connection["connected"] = False

def test_database_insert(database_connection):
    """データベース挿入テスト"""
    database_connection["data"].append({"id": 1, "name": "Test"})
    assert len(database_connection["data"]) == 1

def test_database_query(database_connection):
    """データベース照会テスト"""
    # 前のテストのデータが残っている
    assert len(database_connection["data"]) >= 0
    assert database_connection["connected"] == True
```

## モック（Mock）とパッチ

### 基本的なモック

```python
# test_mocking.py
import pytest
from unittest.mock import Mock, patch
import requests

# テスト対象のコード
def get_user_data(user_id):
    """外部APIからユーザーデータを取得"""
    response = requests.get(f"https://api.example.com/users/{user_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def send_notification(message):
    """通知を送信する関数"""
    print(f"通知送信: {message}")
    return True

class EmailService:
    def send_email(self, to, subject, body):
        """メール送信（実際にはメールサーバーに接続）"""
        print(f"メール送信: {to}, {subject}")
        return {"status": "sent", "message_id": "12345"}

# モックを使ったテスト
@patch('requests.get')
def test_get_user_data_success(mock_get):
    """APIアクセス成功のテスト"""
    # モックの戻り値を設定
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    mock_get.return_value = mock_response
    
    # テスト実行
    result = get_user_data(1)
    
    # アサーション
    assert result == {"id": 1, "name": "John Doe"}
    mock_get.assert_called_once_with("https://api.example.com/users/1")

@patch('requests.get')
def test_get_user_data_failure(mock_get):
    """APIアクセス失敗のテスト"""
    # 404エラーをモック
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response
    
    result = get_user_data(999)
    
    assert result is None
    mock_get.assert_called_once_with("https://api.example.com/users/999")

def test_email_service_mock():
    """EmailServiceのモックテスト"""
    # EmailServiceをモック化
    email_service = Mock()
    email_service.send_email.return_value = {"status": "sent", "message_id": "mock123"}
    
    # テスト実行
    result = email_service.send_email("test@example.com", "Test Subject", "Test Body")
    
    # アサーション
    assert result["status"] == "sent"
    email_service.send_email.assert_called_once_with(
        "test@example.com", "Test Subject", "Test Body"
    )
```

### pytest-mockを使用したモック

```python
# test_pytest_mock.py
import pytest

def external_api_call():
    """外部API呼び出しをシミュレート"""
    import time
    time.sleep(2)  # 2秒待機
    return {"data": "real_api_response"}

def process_data():
    """データ処理関数"""
    api_result = external_api_call()
    return f"Processed: {api_result['data']}"

def test_process_data_with_mock(mocker):
    """pytest-mockを使用したテスト"""
    # external_api_callをモック化
    mock_api = mocker.patch('__main__.external_api_call')
    mock_api.return_value = {"data": "mocked_response"}
    
    # テスト実行
    result = process_data()
    
    # アサーション
    assert result == "Processed: mocked_response"
    mock_api.assert_called_once()

def test_with_spy(mocker):
    """スパイ機能のテスト"""
    # 実際の関数を呼び出しつつ、呼び出しを監視
    spy = mocker.spy(__main__, 'external_api_call')
    
    # 実際の関数が呼ばれる（時間がかかる）
    # result = process_data()
    
    # 呼び出し回数を確認
    # spy.assert_called_once()
```

## テストの組織化とマーキング

### テストマーク

```python
# test_marks.py
import pytest

@pytest.mark.slow
def test_slow_operation():
    """時間のかかるテスト"""
    import time
    time.sleep(1)
    assert True

@pytest.mark.unit
def test_unit_test():
    """ユニットテスト"""
    assert 2 + 2 == 4

@pytest.mark.integration
def test_integration_test():
    """統合テスト"""
    # 複数のコンポーネントをテスト
    assert True

@pytest.mark.smoke
def test_smoke_test():
    """スモークテスト"""
    # 基本的な機能が動作するかの確認
    assert True

@pytest.mark.parametrize("env", ["dev", "staging", "prod"])
@pytest.mark.environment
def test_environment_specific(env):
    """環境固有のテスト"""
    assert env in ["dev", "staging", "prod"]

@pytest.mark.skip(reason="まだ実装されていない機能")
def test_future_feature():
    """スキップされるテスト"""
    assert False

@pytest.mark.skipif(
    condition=True,  # 実際の条件を設定
    reason="特定の条件下でスキップ"
)
def test_conditional_skip():
    """条件付きでスキップされるテスト"""
    assert True

@pytest.mark.xfail(reason="既知のバグ")
def test_known_failure():
    """失敗が予期されるテスト"""
    assert False
```

```bash
# 特定のマークのテストのみ実行
pytest -m "unit"                    # ユニットテストのみ
pytest -m "slow"                    # スローテストのみ
pytest -m "unit and not slow"       # ユニットテストでスローでないもの
pytest -m "smoke or unit"           # スモークテストまたはユニットテスト

# スキップされたテストの詳細表示
pytest -v -rs

# 失敗が予期されるテストの詳細表示
pytest -v -rx
```

## 設定ファイル

### pytest.ini

```ini
# pytest.ini
[tool:pytest]
# テストディレクトリ
testpaths = tests

# テストファイルのパターン
python_files = test_*.py *_test.py

# テストクラスのパターン
python_classes = Test*

# テスト関数のパターン
python_functions = test_*

# 追加のコマンドラインオプション
addopts = 
    -v
    --strict-markers
    --disable-warnings
    --cov=src
    --cov-report=html
    --cov-report=term-missing

# カスタムマークの定義
markers =
    slow: marks tests as slow
    unit: unit tests
    integration: integration tests
    smoke: smoke tests
    environment: environment specific tests

# 最小バージョン
minversion = 6.0
```

### conftest.py

```python
# conftest.py
import pytest
import sys
import os

# プロジェクトルートをパスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(scope="session")
def test_config():
    """テスト設定"""
    return {
        "database_url": "sqlite:///:memory:",
        "api_base_url": "https://api.test.example.com",
        "timeout": 30
    }

@pytest.fixture(autouse=True)
def setup_test_environment():
    """すべてのテストで自動実行されるフィクスチャ"""
    print("\nテスト環境をセットアップ中...")
    yield
    print("\nテスト環境をクリーンアップ中...")

@pytest.fixture
def sample_data():
    """テスト用のサンプルデータ"""
    return {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"},
        ],
        "products": [
            {"id": 1, "name": "Product A", "price": 100},
            {"id": 2, "name": "Product B", "price": 200},
        ]
    }

def pytest_configure(config):
    """pytest設定時に呼ばれる関数"""
    config.addinivalue_line(
        "markers", "api: marks tests as API tests"
    )

def pytest_collection_modifyitems(config, items):
    """テスト収集後に呼ばれる関数"""
    # 'slow'マークのないテストに'fast'マークを追加
    for item in items:
        if "slow" not in item.keywords:
            item.add_marker(pytest.mark.fast)
```

## 実践例：完全なテストスイート

### テスト対象のコード

```python
# user_manager.py
import json
import os
from typing import List, Optional, Dict

class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.id = user_id
        self.name = name
        self.email = email
        self.active = True
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "active": self.active
        }

class UserManager:
    def __init__(self, data_file: str = "users.json"):
        self.data_file = data_file
        self.users: List[User] = []
        self.load_users()
    
    def load_users(self):
        """ファイルからユーザーデータを読み込む"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.users = [
                        User(u['id'], u['name'], u['email']) 
                        for u in data
                    ]
            except (json.JSONDecodeError, KeyError):
                self.users = []
    
    def save_users(self):
        """ユーザーデータをファイルに保存"""
        data = [user.to_dict() for user in self.users]
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def add_user(self, name: str, email: str) -> User:
        """新しいユーザーを追加"""
        if self.get_user_by_email(email):
            raise ValueError(f"Email {email} is already registered")
        
        user_id = max([u.id for u in self.users], default=0) + 1
        user = User(user_id, name, email)
        self.users.append(user)
        return user
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """IDでユーザーを取得"""
        return next((u for u in self.users if u.id == user_id), None)
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """メールアドレスでユーザーを取得"""
        return next((u for u in self.users if u.email == email), None)
    
    def update_user(self, user_id: int, name: str = None, email: str = None) -> bool:
        """ユーザー情報を更新"""
        user = self.get_user_by_id(user_id)
        if not user:
            return False
        
        if email and email != user.email:
            if self.get_user_by_email(email):
                raise ValueError(f"Email {email} is already registered")
            user.email = email
        
        if name:
            user.name = name
        
        return True
    
    def delete_user(self, user_id: int) -> bool:
        """ユーザーを削除"""
        user = self.get_user_by_id(user_id)
        if user:
            self.users.remove(user)
            return True
        return False
    
    def get_active_users(self) -> List[User]:
        """アクティブなユーザーのリストを取得"""
        return [u for u in self.users if u.active]
    
    def get_user_count(self) -> int:
        """ユーザー数を取得"""
        return len(self.users)
```

### 包括的なテストスイート

```python
# test_user_manager.py
import pytest
import json
import os
import tempfile
from user_manager import User, UserManager

class TestUser:
    """Userクラスのテスト"""
    
    def test_user_creation(self):
        """ユーザー作成のテスト"""
        user = User(1, "Alice", "alice@example.com")
        
        assert user.id == 1
        assert user.name == "Alice"
        assert user.email == "alice@example.com"
        assert user.active == True
    
    def test_user_to_dict(self):
        """ユーザーの辞書変換テスト"""
        user = User(1, "Alice", "alice@example.com")
        user_dict = user.to_dict()
        
        expected = {
            "id": 1,
            "name": "Alice",
            "email": "alice@example.com",
            "active": True
        }
        
        assert user_dict == expected

class TestUserManager:
    """UserManagerクラスのテスト"""
    
    @pytest.fixture
    def temp_file(self):
        """一時ファイルのフィクスチャ"""
        fd, temp_path = tempfile.mkstemp(suffix='.json')
        os.close(fd)
        yield temp_path
        if os.path.exists(temp_path):
            os.remove(temp_path)
    
    @pytest.fixture
    def user_manager(self, temp_file):
        """UserManagerのフィクスチャ"""
        return UserManager(temp_file)
    
    @pytest.fixture
    def sample_users_file(self, temp_file):
        """サンプルユーザーデータ付きのファイル"""
        sample_data = [
            {"id": 1, "name": "Alice", "email": "alice@example.com", "active": True},
            {"id": 2, "name": "Bob", "email": "bob@example.com", "active": True},
        ]
        
        with open(temp_file, 'w', encoding='utf-8') as f:
            json.dump(sample_data, f)
        
        return temp_file
    
    def test_initialization_empty_file(self, user_manager):
        """空ファイルでの初期化テスト"""
        assert user_manager.get_user_count() == 0
        assert user_manager.users == []
    
    def test_initialization_with_data(self, sample_users_file):
        """データ付きファイルでの初期化テスト"""
        manager = UserManager(sample_users_file)
        
        assert manager.get_user_count() == 2
        assert manager.get_user_by_id(1).name == "Alice"
        assert manager.get_user_by_id(2).name == "Bob"
    
    def test_add_user(self, user_manager):
        """ユーザー追加のテスト"""
        user = user_manager.add_user("Alice", "alice@example.com")
        
        assert user.id == 1
        assert user.name == "Alice"
        assert user.email == "alice@example.com"
        assert user_manager.get_user_count() == 1
    
    def test_add_duplicate_email(self, user_manager):
        """重複メールアドレスでの追加テスト"""
        user_manager.add_user("Alice", "alice@example.com")
        
        with pytest.raises(ValueError, match="Email alice@example.com is already registered"):
            user_manager.add_user("Another Alice", "alice@example.com")
    
    @pytest.mark.parametrize("user_id, expected_name", [
        (1, "Alice"),
        (2, "Bob"),
        (999, None),
    ])
    def test_get_user_by_id(self, sample_users_file, user_id, expected_name):
        """IDでのユーザー取得テスト"""
        manager = UserManager(sample_users_file)
        user = manager.get_user_by_id(user_id)
        
        if expected_name:
            assert user.name == expected_name
        else:
            assert user is None
    
    @pytest.mark.parametrize("email, expected_name", [
        ("alice@example.com", "Alice"),
        ("bob@example.com", "Bob"),
        ("nonexistent@example.com", None),
    ])
    def test_get_user_by_email(self, sample_users_file, email, expected_name):
        """メールでのユーザー取得テスト"""
        manager = UserManager(sample_users_file)
        user = manager.get_user_by_email(email)
        
        if expected_name:
            assert user.name == expected_name
        else:
            assert user is None
    
    def test_update_user_success(self, user_manager):
        """ユーザー更新成功のテスト"""
        user = user_manager.add_user("Alice", "alice@example.com")
        
        success = user_manager.update_user(user.id, name="Alice Smith", email="alice.smith@example.com")
        
        assert success == True
        updated_user = user_manager.get_user_by_id(user.id)
        assert updated_user.name == "Alice Smith"
        assert updated_user.email == "alice.smith@example.com"
    
    def test_update_nonexistent_user(self, user_manager):
        """存在しないユーザーの更新テスト"""
        success = user_manager.update_user(999, name="New Name")
        assert success == False
    
    def test_update_user_duplicate_email(self, user_manager):
        """重複メールでのユーザー更新テスト"""
        user1 = user_manager.add_user("Alice", "alice@example.com")
        user2 = user_manager.add_user("Bob", "bob@example.com")
        
        with pytest.raises(ValueError, match="Email alice@example.com is already registered"):
            user_manager.update_user(user2.id, email="alice@example.com")
    
    def test_delete_user_success(self, user_manager):
        """ユーザー削除成功のテスト"""
        user = user_manager.add_user("Alice", "alice@example.com")
        initial_count = user_manager.get_user_count()
        
        success = user_manager.delete_user(user.id)
        
        assert success == True
        assert user_manager.get_user_count() == initial_count - 1
        assert user_manager.get_user_by_id(user.id) is None
    
    def test_delete_nonexistent_user(self, user_manager):
        """存在しないユーザーの削除テスト"""
        success = user_manager.delete_user(999)
        assert success == False
    
    def test_save_and_load_users(self, user_manager):
        """保存と読み込みのテスト"""
        # ユーザーを追加
        user_manager.add_user("Alice", "alice@example.com")
        user_manager.add_user("Bob", "bob@example.com")
        
        # 保存
        user_manager.save_users()
        
        # 新しいインスタンスで読み込み
        new_manager = UserManager(user_manager.data_file)
        
        assert new_manager.get_user_count() == 2
        assert new_manager.get_user_by_email("alice@example.com").name == "Alice"
        assert new_manager.get_user_by_email("bob@example.com").name == "Bob"

@pytest.mark.integration
class TestUserManagerIntegration:
    """統合テスト"""
    
    @pytest.fixture
    def populated_manager(self, tmp_path):
        """データが入ったUserManagerのフィクスチャ"""
        data_file = tmp_path / "test_users.json"
        manager = UserManager(str(data_file))
        
        # テストデータを追加
        manager.add_user("Alice", "alice@example.com")
        manager.add_user("Bob", "bob@example.com")
        manager.add_user("Charlie", "charlie@example.com")
        
        return manager
    
    def test_full_user_lifecycle(self, populated_manager):
        """ユーザーのライフサイクル全体のテスト"""
        manager = populated_manager
        
        # 1. ユーザー追加
        user = manager.add_user("David", "david@example.com")
        assert manager.get_user_count() == 4
        
        # 2. ユーザー取得
        retrieved_user = manager.get_user_by_id(user.id)
        assert retrieved_user.name == "David"
        
        # 3. ユーザー更新
        manager.update_user(user.id, name="David Smith")
        updated_user = manager.get_user_by_id(user.id)
        assert updated_user.name == "David Smith"
        
        # 4. 保存
        manager.save_users()
        
        # 5. 新しいインスタンスで読み込み
        new_manager = UserManager(manager.data_file)
        assert new_manager.get_user_count() == 4
        assert new_manager.get_user_by_id(user.id).name == "David Smith"
        
        # 6. ユーザー削除
        new_manager.delete_user(user.id)
        assert new_manager.get_user_count() == 3
        assert new_manager.get_user_by_id(user.id) is None
```

## テストカバレッジ

### カバレッジレポートの生成

```bash
# カバレッジ付きでテスト実行
pytest --cov=user_manager

# HTMLレポート生成
pytest --cov=user_manager --cov-report=html

# 詳細なターミナルレポート
pytest --cov=user_manager --cov-report=term-missing

# カバレッジの閾値設定
pytest --cov=user_manager --cov-fail-under=90
```

## まとめ

pytestは、Pythonでテストを書くための非常に強力で柔軟なフレームワークです。この章で学習した内容：

- **基本的なテスト**: assert文を使った簡単なテスト記述
- **パラメータ化テスト**: 複数のテストケースを効率的に実行
- **フィクスチャ**: テストデータの準備と後処理
- **モック**: 外部依存性を排除したテスト
- **テストの組織化**: マークと設定ファイルによる管理
- **実践例**: 実際のアプリケーションでのテスト実装

pytestをマスターすることで、信頼性の高いPythonアプリケーションを開発できるようになります。テスト駆動開発（TDD）やテストファーストな開発アプローチを身につけることで、より品質の高いコードを書けるようになります。

## 次のステップ

1. **テスト駆動開発（TDD）**: テストを先に書く開発手法の習得
2. **継続的インテグレーション**: GitHub ActionsやJenkinsでの自動テスト
3. **パフォーマンステスト**: pytest-benchmarkを使った性能測定
4. **セキュリティテスト**: banditやsafetyを使ったセキュリティチェック
5. **エンドツーエンドテスト**: Seleniumを使ったWebアプリケーションのテスト

テストは、ソフトウェア開発において欠かせない要素です。今回学んだpytestの知識を活用して、より良いソフトウェアを開発してください。