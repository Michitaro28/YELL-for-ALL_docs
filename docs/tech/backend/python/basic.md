# Pythonの基本文法

Pythonは読みやすく、書きやすいプログラミング言語です。ここではPythonの基本的な文法について解説します。

## はじめに：print文とコメント

### print文の基本

プログラミングの基本として、まず画面に文字を表示する`print`文から始めましょう。

```python
# 基本的な文字列の出力
print("Hello, World!")
print('こんにちは、世界！')

# 複数の値を出力
print("私の名前は", "太郎", "です")
print("私の年齢は", 25, "歳です")

# 改行なしで出力
print("Hello", end=" ")
print("World")  # "Hello World"と表示される

# 区切り文字を変更
print("apple", "banana", "orange", sep="-")  # apple-banana-orange
```

### コメントの書き方

```python
# これは一行コメントです
print("Hello")  # 行末にもコメントを書けます

"""
これは複数行コメント（docstring）です。
関数やクラスの説明によく使われます。
"""

'''
シングルクォート3つでも
複数行コメントが書けます。
'''
```

## 変数と基本データ型

### 変数の宣言と代入

Pythonでは変数の型を明示的に宣言する必要がありません。

```python
# 文字列
name = "太郎"
message = 'こんにちは'

# 数値
age = 25
height = 175.5

# 真偽値
is_student = True
has_license = False
```

### 基本データ型

```python
# 整数 (int)
number = 42
print(type(number))  # <class 'int'>

# 浮動小数点数 (float)
pi = 3.14159
print(type(pi))  # <class 'float'>

# 文字列 (str)
greeting = "Hello, World!"
print(type(greeting))  # <class 'str'>

# 真偽値 (bool)
is_true = True
print(type(is_true))  # <class 'bool'>
```

## 文字列操作

### 文字列の結合と書式設定

```python
# 文字列の結合
first_name = "山田"
last_name = "太郎"
full_name = first_name + " " + last_name
print(full_name)  # 山田 太郎

# f-string（推奨）
age = 25
message = f"私の名前は{full_name}で、年齢は{age}歳です。"
print(message)

# format()メソッド
message2 = "私の名前は{}で、年齢は{}歳です。".format(full_name, age)
print(message2)
```

### 文字列メソッド

```python
text = "  Hello, Python!  "

# 文字列の長さ
print(len(text))  # 18

# 大文字・小文字変換
print(text.upper())    # "  HELLO, PYTHON!  "
print(text.lower())    # "  hello, python!  "

# 空白の除去
print(text.strip())    # "Hello, Python!"

# 文字列の置換
print(text.replace("Python", "World"))  # "  Hello, World!  "

# 文字列の分割
words = "apple,banana,orange".split(",")
print(words)  # ['apple', 'banana', 'orange']
```

## リスト（配列）

### リストの作成と操作

```python
# リストの作成
fruits = ["りんご", "バナナ", "オレンジ"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]

# 要素へのアクセス
print(fruits[0])    # りんご
print(fruits[-1])   # オレンジ（最後の要素）

# 要素の追加
fruits.append("ぶどう")
print(fruits)  # ['りんご', 'バナナ', 'オレンジ', 'ぶどう']

# 要素の挿入
fruits.insert(1, "いちご")
print(fruits)  # ['りんご', 'いちご', 'バナナ', 'オレンジ', 'ぶどう']

# 要素の削除
fruits.remove("バナナ")
print(fruits)  # ['りんご', 'いちご', 'オレンジ', 'ぶどう']

# リストの長さ
print(len(fruits))  # 4
```

### リストのスライス

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# スライス操作
print(numbers[2:5])    # [2, 3, 4]
print(numbers[:3])     # [0, 1, 2]
print(numbers[7:])     # [7, 8, 9]
print(numbers[::2])    # [0, 2, 4, 6, 8]（2つおき）
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]（逆順）
```

## 辞書（Dictionary）

### 辞書の作成と操作

```python
# 辞書の作成
person = {
    "name": "田中太郎",
    "age": 30,
    "city": "東京"
}

# 値へのアクセス
print(person["name"])  # 田中太郎
print(person.get("age"))  # 30

# 新しいキーと値の追加
person["job"] = "エンジニア"
print(person)

# 値の更新
person["age"] = 31

# キーの削除
del person["city"]
print(person)

# すべてのキーと値を取得
print(person.keys())    # dict_keys(['name', 'age', 'job'])
print(person.values())  # dict_values(['田中太郎', 31, 'エンジニア'])
print(person.items())   # dict_items([('name', '田中太郎'), ('age', 31), ('job', 'エンジニア')])
```

## 条件分岐（if文）

### 基本的なif文

```python
age = 18

if age >= 20:
    print("成人です")
elif age >= 18:
    print("18歳以上です")
else:
    print("未成年です")

# 複数条件
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"

print(f"成績: {grade}")
```

### 論理演算子

```python
age = 25
has_license = True

# and演算子
if age >= 18 and has_license:
    print("運転できます")

# or演算子
weather = "雨"
if weather == "雨" or weather == "雪":
    print("傘が必要です")

# not演算子
is_weekend = False
if not is_weekend:
    print("平日です")

# in演算子
fruits = ["りんご", "バナナ", "オレンジ"]
if "りんご" in fruits:
    print("りんごがあります")
```

## ループ処理

### forループ

```python
# リストの反復
fruits = ["りんご", "バナナ", "オレンジ"]
for fruit in fruits:
    print(f"フルーツ: {fruit}")

# range()を使った数値の反復
for i in range(5):
    print(f"数値: {i}")  # 0から4まで

for i in range(1, 6):
    print(f"数値: {i}")  # 1から5まで

for i in range(0, 10, 2):
    print(f"偶数: {i}")  # 0, 2, 4, 6, 8

# 辞書の反復
person = {"name": "太郎", "age": 25, "city": "東京"}
for key, value in person.items():
    print(f"{key}: {value}")

# enumerateを使ったインデックス付きループ
fruits = ["りんご", "バナナ", "オレンジ"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

### whileループ

```python
# 基本的なwhileループ
count = 0
while count < 5:
    print(f"カウント: {count}")
    count += 1

# ユーザー入力を使った例
password = ""
while password != "secret":
    password = input("パスワードを入力してください: ")
    if password != "secret":
        print("パスワードが違います")

print("ログイン成功！")
```

### ループ制御（break, continue）

```python
# break文
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# continue文
for i in range(10):
    if i % 2 == 0:  # 偶数をスキップ
        continue
    print(i)  # 1, 3, 5, 7, 9
```

## 関数

### 関数とは

関数は、特定の処理をまとめて名前を付けたものです。同じ処理を何度も書く代わりに、関数として定義しておくことで再利用できます。

### 基本的な関数の定義と呼び出し

```python
# 最もシンプルな関数
def say_hello():
    print("こんにちは！")

# 関数の呼び出し
say_hello()  # "こんにちは！"が表示される

# 引数を持つ関数
def greet_person(name):
    print(f"こんにちは、{name}さん！")

greet_person("太郎")  # "こんにちは、太郎さん！"

# 複数の引数を持つ関数
def introduce(name, age):
    print(f"私の名前は{name}で、{age}歳です。")

introduce("花子", 22)
```

### 戻り値を持つ関数

```python
# 戻り値を持つ関数
def add(a, b):
    result = a + b
    return result  # 計算結果を返す

# 関数の戻り値を変数に代入
sum_result = add(5, 3)
print(sum_result)  # 8

# 直接print文で使用
print(add(10, 20))  # 30

# 複雑な計算をする関数
def calculate_area(width, height):
    area = width * height
    return area

room_area = calculate_area(5, 4)
print(f"部屋の面積は{room_area}平方メートルです")
```

### デフォルト引数とキーワード引数

```python
# デフォルト引数を持つ関数
def greet_with_title(name, title="さん"):
    return f"こんにちは、{name}{title}！"

print(greet_with_title("田中"))        # こんにちは、田中さん！
print(greet_with_title("田中", "先生"))  # こんにちは、田中先生！

# キーワード引数を使った呼び出し
def create_profile(name, age, city="未設定"):
    return f"名前: {name}, 年齢: {age}, 住所: {city}"

# 通常の呼び出し
print(create_profile("太郎", 25))

# キーワードを指定した呼び出し
print(create_profile(age=30, name="花子", city="大阪"))
```

### 複数の戻り値

```python
def calculate_all(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else 0
    return addition, subtraction, multiplication, division

# 複数の戻り値を受け取る
add_result, sub_result, mul_result, div_result = calculate_all(10, 2)
print(f"足し算: {add_result}")
print(f"引き算: {sub_result}")
print(f"掛け算: {mul_result}")
print(f"割り算: {div_result}")

# タプルとして受け取ることも可能
results = calculate_all(15, 3)
print(results)  # (18, 12, 45, 5.0)
```

### 関数内関数とラムダ関数

```python
# 関数の中に関数を定義
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_five = outer_function(5)
print(add_five(3))  # 8

# ラムダ関数（無名関数）
square = lambda x: x ** 2
print(square(4))  # 16

# リストと組み合わせて使用
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]
```

## クラスとオブジェクト指向プログラミング

### クラスとは

クラスは、関連するデータ（属性）と処理（メソッド）をまとめたものです。オブジェクト指向プログラミングの基本概念です。

### 基本的なクラスの定義

```python
# シンプルなクラスの定義
class Person:
    def __init__(self, name, age):
        """コンストラクタ：オブジェクトが作られるときに呼ばれる"""
        self.name = name  # インスタンス変数
        self.age = age

    def greet(self):
        """メソッド：クラス内で定義された関数"""
        print(f"こんにちは、私は{self.name}です。")

    def celebrate_birthday(self):
        """誕生日を祝うメソッド"""
        self.age += 1
        print(f"誕生日おめでとう！{self.age}歳になりました。")

# クラスからオブジェクト（インスタンス）を作成
person1 = Person("太郎", 25)
person2 = Person("花子", 22)

# メソッドの呼び出し
person1.greet()  # こんにちは、私は太郎です。
person2.greet()  # こんにちは、私は花子です。

# 属性にアクセス
print(f"{person1.name}は{person1.age}歳です")

# メソッドでデータを変更
person1.celebrate_birthday()  # 誕生日おめでとう！26歳になりました。
```

### より実用的なクラスの例

```python
class BankAccount:
    """銀行口座を表すクラス"""
    
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        """入金"""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"入金: +{amount}円")
            print(f"{amount}円を入金しました。残高: {self.balance}円")
        else:
            print("入金額は0円より大きくする必要があります。")

    def withdraw(self, amount):
        """出金"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"出金: -{amount}円")
            print(f"{amount}円を出金しました。残高: {self.balance}円")
        else:
            print("出金できません。残高不足または無効な金額です。")

    def get_balance(self):
        """残高照会"""
        return self.balance

    def show_history(self):
        """取引履歴表示"""
        print(f"\n{self.owner}さんの取引履歴:")
        for transaction in self.transaction_history:
            print(f"  {transaction}")
        print(f"現在の残高: {self.balance}円\n")

# 銀行口座オブジェクトの作成と使用
account = BankAccount("田中太郎", 1000)

account.deposit(500)   # 500円を入金
account.withdraw(200)  # 200円を出金
account.deposit(1000)  # 1000円を入金

print(f"現在の残高: {account.get_balance()}円")
account.show_history()
```

### クラス変数とインスタンス変数

```python
class Student:
    # クラス変数：すべてのインスタンスで共有される
    school_name = "〇〇高等学校"
    student_count = 0

    def __init__(self, name, grade):
        # インスタンス変数：各インスタンス固有のデータ
        self.name = name
        self.grade = grade
        Student.student_count += 1  # 生徒数をカウント

    def introduce(self):
        print(f"私は{Student.school_name}の{self.grade}年生、{self.name}です。")

    @classmethod
    def get_student_count(cls):
        """クラスメソッド：クラス全体に関する情報を扱う"""
        return cls.student_count

# 生徒オブジェクトの作成
student1 = Student("太郎", 2)
student2 = Student("花子", 3)

student1.introduce()
student2.introduce()

print(f"全生徒数: {Student.get_student_count()}人")
```

### 継承

```python
# 基底クラス（親クラス）
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}が鳴いています。")

    def move(self):
        print(f"{self.name}が移動しています。")

# 派生クラス（子クラス）
class Dog(Animal):
    def speak(self):
        """メソッドのオーバーライド"""
        print(f"{self.name}がワンワン鳴いています。")

    def fetch(self):
        """犬特有のメソッド"""
        print(f"{self.name}がボールを取ってきました。")

class Cat(Animal):
    def speak(self):
        print(f"{self.name}がニャーニャー鳴いています。")

    def climb(self):
        print(f"{self.name}が木に登りました。")

# 継承を使ったオブジェクトの作成
dog = Dog("ポチ")
cat = Cat("タマ")

dog.speak()  # ポチがワンワン鳴いています。
dog.move()   # ポチが移動しています。（親クラスのメソッド）
dog.fetch()  # ポチがボールを取ってきました。

cat.speak()  # タマがニャーニャー鳴いています。
cat.climb()  # タマが木に登りました。
```

## エラーハンドリング

### try-except文

```python
# 基本的なエラーハンドリング
try:
    number = int(input("数値を入力してください: "))
    result = 10 / number
    print(f"結果: {result}")
except ValueError:
    print("数値を入力してください")
except ZeroDivisionError:
    print("0で割ることはできません")
except Exception as e:
    print(f"予期しないエラーが発生しました: {e}")
else:
    print("エラーは発生しませんでした")
finally:
    print("処理が完了しました")
```

### ファイル操作でのエラーハンドリング

```python
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("ファイルが見つかりません")
except PermissionError:
    print("ファイルの読み取り権限がありません")
```

## まとめ

この章では、Pythonの基本的な文法について学習しました：

- **print文とコメント**: プログラムの基本的な出力とコードの説明方法
- **変数とデータ型**: 文字列、数値、真偽値の扱い方
- **文字列操作**: 結合、書式設定、メソッドの活用
- **リスト**: 配列の作成、操作、スライス
- **辞書**: キーと値のペアでデータを管理
- **条件分岐**: if文と論理演算子
- **ループ処理**: forループとwhileループ
- **関数**: 再利用可能なコードブロックの作成と詳細な使い方
- **クラスとオブジェクト指向**: データと処理をまとめて管理する方法
- **エラーハンドリング**: 例外処理でプログラムの安定性を向上

これらの基本的な概念を理解することで、より複雑なPythonプログラムを書くための土台が身につきます。特に関数とクラスは、大きなプログラムを書く際に重要な概念となりますので、しっかりと理解しておきましょう。

## 練習問題

学習内容を定着させるために、以下の練習問題にチャレンジしてみてください：

1. **基本的な関数**: 2つの数値を引数として受け取り、より大きい数値を返す関数を作成してください。

2. **クラスの作成**: 図書館の本を管理するBookクラスを作成してください。タイトル、著者、出版年を属性として持ち、本の情報を表示するメソッドを実装してください。

3. **リストと関数の組み合わせ**: 数値のリストを受け取り、その平均値を計算して返す関数を作成してください。

これらの練習を通じて、Pythonの基本的な概念をより深く理解することができます。