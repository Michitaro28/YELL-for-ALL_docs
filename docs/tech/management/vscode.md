# Visual Studio Code入門ガイド

Visual Studio Code（VS Code）は、Microsoftが開発した無料のソースコードエディタです。軽量でありながら強力な機能を持ち、幅広いプログラミング言語をサポートしています。

## VS Codeとは

VS Codeは、現代的なWeb技術（Electron）で構築されたクロスプラットフォームなコードエディタです。拡張機能により機能を追加でき、統合開発環境（IDE）に近い機能を提供します。

### VS Codeの特徴

- **軽量で高速**: 起動が早く、大きなファイルもスムーズに処理
- **豊富な拡張機能**: マーケットプレイスから様々な機能を追加可能
- **統合ターミナル**: エディタ内でコマンドライン操作が可能
- **Git統合**: バージョン管理が標準で統合
- **IntelliSense**: 強力なコード補完とエラー検出
- **デバッグ機能**: 多言語対応のデバッガー
- **カスタマイズ性**: 細かい設定変更が可能

## インストールと初期設定

### インストール方法

```bash
# 公式サイトからダウンロード
# https://code.visualstudio.com/

# macOS（Homebrew使用）
brew install --cask visual-studio-code

# Windows（Chocolatey使用）
choco install vscode

# Linux（Ubuntu/Debian）
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install code
```

### 初回起動と基本設定

1. **Welcome画面**: VS Codeを初めて起動すると表示される
2. **テーマの選択**: カラーテーマの設定
3. **言語設定**: 日本語化したい場合は Japanese Language Pack をインストール

## インターフェースの概要

### 基本的なレイアウト

```
┌─────────────────────────────────────────────────────────┐
│ [メニューバー]                                            │
├───────────┬─────────────────────────────────────────────┤
│           │ [エディタ]                                    │
│ [サイド   │                                             │
│  バー]    │                                             │
│           │                                             │
├───────────┼─────────────────────────────────────────────┤
│           │ [ターミナル/パネル]                           │
└───────────┴─────────────────────────────────────────────┘
```

### 主要な要素

- **アクティビティバー**: 左端の縦のメニュー
- **サイドバー**: ファイルエクスプローラー、検索、Git などの表示
- **エディタ**: コードを編集するメイン領域
- **パネル**: ターミナル、出力、問題、デバッグコンソール
- **ステータスバー**: 下部の情報表示バー

## 基本的な使い方

### ファイルとフォルダーの操作

```bash
# ファイルを開く
Ctrl+O (Windows/Linux)
Cmd+O (macOS)

# フォルダーを開く
Ctrl+K Ctrl+O (Windows/Linux)
Cmd+K Cmd+O (macOS)

# 新しいファイル
Ctrl+N (Windows/Linux)
Cmd+N (macOS)

# ファイル保存
Ctrl+S (Windows/Linux)
Cmd+S (macOS)

# すべて保存
Ctrl+K S (Windows/Linux)
Cmd+Alt+S (macOS)
```

### エディタの基本操作

```bash
# カーソル移動
Home/End: 行の先頭/末尾
Ctrl+Home/End: ファイルの先頭/末尾
Ctrl+G: 指定行にジャンプ
Ctrl+P: ファイルを素早く開く

# 選択操作
Shift+矢印キー: 選択範囲を拡張
Ctrl+A: 全選択
Ctrl+L: 行全体を選択
Alt+クリック: 複数カーソル

# 編集操作
Ctrl+Z: 元に戻す
Ctrl+Y: やり直し
Ctrl+X: 切り取り
Ctrl+C: コピー
Ctrl+V: 貼り付け
Ctrl+D: 同じ単語を次々選択
```

### 検索と置換

```bash
# 検索
Ctrl+F: ファイル内検索
Ctrl+H: 置換
Ctrl+Shift+F: 全ファイル検索
Ctrl+Shift+H: 全ファイル置換

# 検索オプション
Alt+C: 大文字小文字を区別
Alt+W: 単語全体をマッチ
Alt+R: 正規表現を使用
```

## 重要なショートカットキー

### ファイル操作
```bash
Ctrl+P: クイックオープン（ファイル名で検索）
Ctrl+Shift+P: コマンドパレット
Ctrl+Shift+E: エクスプローラー表示
Ctrl+Shift+N: 新しいウィンドウ
Ctrl+W: タブを閉じる
Ctrl+Shift+T: 閉じたタブを再度開く
```

### 編集操作
```bash
Ctrl+/: コメントアウト/解除
Ctrl+]: インデント追加
Ctrl+[: インデント削除
Alt+Up/Down: 行を上下に移動
Shift+Alt+Up/Down: 行を複製
Ctrl+Shift+K: 行削除
Ctrl+Enter: 下に新しい行を挿入
Ctrl+Shift+Enter: 上に新しい行を挿入
```

### 表示操作
```bash
Ctrl++: ズームイン
Ctrl+-: ズームアウト
Ctrl+`: ターミナル表示/非表示
Ctrl+B: サイドバー表示/非表示
F11: フルスクリーン
Ctrl+Shift+`: 新しいターミナル
```

### ナビゲーション
```bash
Ctrl+G: 行番号指定ジャンプ
Ctrl+M: 対応する括弧にジャンプ
F12: 定義に移動
Alt+F12: 定義をここに表示
Shift+F12: 参照を表示
Ctrl+T: シンボル検索
```

## 拡張機能（Extensions）

### 必須の拡張機能

#### 言語サポート
```json
{
  "extensions": [
    "ms-python.python",              // Python
    "ms-vscode.vscode-typescript-next", // TypeScript
    "bradlc.vscode-tailwindcss",     // Tailwind CSS
    "esbenp.prettier-vscode",        // Prettier
    "ms-vscode.vscode-eslint",       // ESLint
    "ms-python.pylint"               // Pylint
  ]
}
```

#### 開発支援
```json
{
  "extensions": [
    "ms-vscode.vscode-git",          // Git
    "eamodio.gitlens",               // GitLens
    "ms-vscode-remote.remote-ssh",   // Remote SSH
    "ms-vscode.live-server",         // Live Server
    "formulahendry.auto-rename-tag", // Auto Rename Tag
    "christian-kohler.path-intellisense" // Path Intellisense
  ]
}
```

#### テーマとアイコン
```json
{
  "extensions": [
    "zhuangtongfa.Material-theme",   // Material Theme
    "PKief.material-icon-theme",     // Material Icon Theme
    "dracula-theme.theme-dracula",   // Dracula Theme
    "ms-vscode.Theme-OneDarkPro"     // One Dark Pro
  ]
}
```

### 拡張機能のインストール

```bash
# GUI操作
1. Ctrl+Shift+X で拡張機能パネルを開く
2. 検索ボックスで拡張機能を検索
3. Install ボタンをクリック

# コマンドライン
code --install-extension ms-python.python
code --list-extensions  # インストール済み拡張機能の一覧
```

## settings.json の設定

### settings.json の場所

```bash
# Windows
%APPDATA%\Code\User\settings.json

# macOS
~/Library/Application Support/Code/User/settings.json

# Linux
~/.config/Code/User/settings.json
```

### 基本的なsettings.json設定

```json
{
  // エディタの基本設定
  "editor.fontSize": 14,
  "editor.fontFamily": "'Fira Code', 'Consolas', 'Monaco', monospace",
  "editor.fontLigatures": true,
  "editor.lineHeight": 1.5,
  "editor.tabSize": 2,
  "editor.insertSpaces": true,
  "editor.detectIndentation": false,
  "editor.wordWrap": "on",
  "editor.minimap.enabled": true,
  "editor.minimap.maxColumn": 120,
  
  // 行番号とルーラー
  "editor.lineNumbers": "on",
  "editor.rulers": [80, 120],
  "editor.renderWhitespace": "boundary",
  "editor.renderControlCharacters": true,
  
  // カーソルとスクロール
  "editor.cursorStyle": "line",
  "editor.cursorBlinking": "blink",
  "editor.smoothScrolling": true,
  "editor.scrollBeyondLastLine": false,
  
  // IntelliSense とサジェスト
  "editor.quickSuggestions": {
    "other": true,
    "comments": false,
    "strings": false
  },
  "editor.parameterHints.enabled": true,
  "editor.suggestOnTriggerCharacters": true,
  "editor.acceptSuggestionOnEnter": "on",
  
  // 自動保存と自動フォーマット
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000,
  "editor.formatOnSave": true,
  "editor.formatOnPaste": true,
  "editor.formatOnType": true,
  
  // ワークベンチ（テーマ・アイコン）
  "workbench.colorTheme": "One Dark Pro",
  "workbench.iconTheme": "material-icon-theme",
  "workbench.activityBar.visible": true,
  "workbench.sideBar.location": "left",
  
  // エクスプローラー
  "explorer.confirmDelete": false,
  "explorer.confirmDragAndDrop": false,
  "explorer.compactFolders": false,
  
  // ターミナル
  "terminal.integrated.fontSize": 13,
  "terminal.integrated.fontFamily": "'Fira Code', monospace",
  "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
  "terminal.integrated.cursorStyle": "line",
  "terminal.integrated.cursorBlinking": true,
  
  // Git設定
  "git.enableSmartCommit": true,
  "git.confirmSync": false,
  "git.autofetch": true,
  "git.decorations.enabled": true,
  
  // ファイル関連
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "files.trimFinalNewlines": true,
  "files.exclude": {
    "**/.git": true,
    "**/.DS_Store": true,
    "**/node_modules": true,
    "**/__pycache__": true,
    "**/*.pyc": true
  },
  
  // 検索設定
  "search.exclude": {
    "**/node_modules": true,
    "**/bower_components": true,
    "**/*.code-search": true,
    "**/dist": true,
    "**/build": true
  }
}
```

### 言語固有の設定

```json
{
  // Python設定
  "[python]": {
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.black-formatter"
  },
  "python.defaultInterpreterPath": "/usr/bin/python3",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  
  // JavaScript/TypeScript設定
  "[javascript]": {
    "editor.tabSize": 2,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescript]": {
    "editor.tabSize": 2,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[json]": {
    "editor.tabSize": 2,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  
  // HTML/CSS設定
  "[html]": {
    "editor.tabSize": 2,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[css]": {
    "editor.tabSize": 2,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  
  // Markdown設定
  "[markdown]": {
    "editor.wordWrap": "on",
    "editor.quickSuggestions": false
  },
  
  // Prettier設定
  "prettier.singleQuote": true,
  "prettier.semi": true,
  "prettier.tabWidth": 2,
  "prettier.trailingComma": "es5",
  "prettier.printWidth": 80,
  
  // ESLint設定
  "eslint.validate": [
    "javascript",
    "javascriptreact",
    "typescript",
    "typescriptreact"
  ],
  "eslint.format.enable": true
}
```

### 高度な設定例

```json
{
  // Emmet設定
  "emmet.includeLanguages": {
    "javascript": "javascriptreact",
    "typescript": "typescriptreact"
  },
  "emmet.triggerExpansionOnTab": true,
  
  // ブラケットペア設定
  "editor.bracketPairColorization.enabled": true,
  "editor.guides.bracketPairs": "active",
  
  // インデントガイド
  "editor.guides.indentation": true,
  "editor.renderIndentGuides": true,
  
  // コードレンズ
  "editor.codeLens": true,
  "diffEditor.codeLens": true,
  
  // 折りたたみ
  "editor.foldingStrategy": "indentation",
  "editor.showFoldingControls": "mouseover",
  
  // スクロールバー
  "editor.scrollbar.vertical": "visible",
  "editor.scrollbar.horizontal": "visible",
  "editor.scrollbar.verticalScrollbarSize": 18,
  "editor.scrollbar.horizontalScrollbarSize": 18,
  
  // ワードハイライト
  "editor.occurrencesHighlight": true,
  "editor.selectionHighlight": true,
  
  // セキュリティ設定
  "security.workspace.trust.untrustedFiles": "prompt",
  "extensions.ignoreRecommendations": false,
  
  // パフォーマンス設定
  "files.watcherExclude": {
    "**/.git/objects/**": true,
    "**/.git/subtree-cache/**": true,
    "**/node_modules/*/**": true,
    "**/.hg/store/**": true
  }
}
```

## ワークスペース設定

### .vscode/settings.json

プロジェクト固有の設定はワークスペースルートの`.vscode/settings.json`に記述します。

```json
{
  // プロジェクト固有のPython設定
  "python.defaultInterpreterPath": "./venv/bin/python",
  "python.terminal.activateEnvironment": true,
  
  // プロジェクト固有のフォーマット設定
  "editor.tabSize": 4,
  "[javascript]": {
    "editor.tabSize": 2
  },
  
  // プロジェクト固有の除外設定
  "files.exclude": {
    "**/dist": true,
    "**/build": true,
    "**/.venv": true
  },
  
  // プロジェクト固有のタスク設定
  "terminal.integrated.env.osx": {
    "PYTHONPATH": "${workspaceFolder}"
  },
  "terminal.integrated.env.linux": {
    "PYTHONPATH": "${workspaceFolder}"
  },
  "terminal.integrated.env.windows": {
    "PYTHONPATH": "${workspaceFolder}"
  }
}
```

### tasks.json（タスク設定）

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Python: Run Current File",
      "type": "shell",
      "command": "${config:python.defaultInterpreterPath}",
      "args": ["${file}"],
      "group": {
        "kind": "build",
        "isDefault": true
      },
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      },
      "problemMatcher": []
    },
    {
      "label": "npm: install",
      "type": "shell",
      "command": "npm",
      "args": ["install"],
      "group": "build",
      "presentation": {
        "reveal": "always",
        "panel": "new"
      }
    },
    {
      "label": "npm: start",
      "type": "shell",
      "command": "npm",
      "args": ["start"],
      "group": "build",
      "presentation": {
        "reveal": "always",
        "panel": "new"
      }
    }
  ]
}
```

### launch.json（デバッグ設定）

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "Python: Django",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/manage.py",
      "args": ["runserver"],
      "django": true,
      "justMyCode": true
    },
    {
      "name": "Node.js: Launch Program",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/app.js",
      "skipFiles": ["<node_internals>/**"]
    },
    {
      "name": "Node.js: Attach",
      "type": "node",
      "request": "attach",
      "port": 9229,
      "skipFiles": ["<node_internals>/**"]
    }
  ]
}
```

## Git統合機能

### 基本的なGit操作

```bash
# VS Code内でのGit操作
Ctrl+Shift+G: Git パネルを開く
Ctrl+Shift+P → "Git: "で始まるコマンドを検索

# ステージング
ファイル横の + ボタン: ステージング
ファイル横の - ボタン: アンステージ

# コミット
Ctrl+Enter: コミットメッセージを入力してコミット

# ブランチ操作
左下のブランチ名をクリック: ブランチ切り替え
```

### GitLens設定

```json
{
  "gitlens.views.repositories.files.layout": "tree",
  "gitlens.views.fileHistory.enabled": true,
  "gitlens.views.lineHistory.enabled": true,
  "gitlens.currentLine.enabled": true,
  "gitlens.currentLine.pullRequests.enabled": true,
  "gitlens.codeLens.enabled": true,
  "gitlens.codeLens.authors.enabled": false,
  "gitlens.codeLens.recentChange.enabled": true,
  "gitlens.hovers.currentLine.over": "line",
  "gitlens.blame.compact": false,
  "gitlens.blame.heatmap.enabled": true
}
```

## デバッグ機能

### デバッグの基本操作

```bash
F5: デバッグ開始
F9: ブレークポイント設定/解除
F10: ステップオーバー
F11: ステップイン
Shift+F11: ステップアウト
Ctrl+Shift+F5: デバッグ再開
Shift+F5: デバッグ停止
```

### デバッグ設定例

```json
{
  "name": "Python: Flask",
  "type": "python",
  "request": "launch",
  "module": "flask",
  "env": {
    "FLASK_APP": "app.py",
    "FLASK_ENV": "development"
  },
  "args": ["run", "--host=0.0.0.0", "--port=5000"],
  "jinja": true,
  "justMyCode": true
}
```

## 便利なスニペット

### ユーザースニペット作成

```bash
# スニペット作成
Ctrl+Shift+P → "Preferences: Configure User Snippets"
```

### Python スニペット例

```json
{
  "Print to console": {
    "prefix": "log",
    "body": ["print(f\"${1:message}: {${2:variable}}\")"],
    "description": "Log output to console"
  },
  "Python main": {
    "prefix": "main",
    "body": [
      "def main():",
      "    ${1:pass}",
      "",
      "",
      "if __name__ == \"__main__\":",
      "    main()"
    ],
    "description": "Main function template"
  },
  "Python class": {
    "prefix": "class",
    "body": [
      "class ${1:ClassName}:",
      "    \"\"\"${2:Class description}\"\"\"",
      "    ",
      "    def __init__(self${3:, param}):",
      "        \"\"\"Initialize the class.\"\"\"",
      "        ${4:pass}"
    ],
    "description": "Class template"
  }
}
```

### JavaScript スニペット例

```json
{
  "Console log": {
    "prefix": "log",
    "body": ["console.log('${1:message}:', ${2:variable});"],
    "description": "Log output to console"
  },
  "Arrow function": {
    "prefix": "af",
    "body": ["const ${1:functionName} = (${2:params}) => {", "  ${3:// body}", "};"],
    "description": "Arrow function"
  },
  "React component": {
    "prefix": "rfc",
    "body": [
      "import React from 'react';",
      "",
      "const ${1:ComponentName} = () => {",
      "  return (",
      "    <div>",
      "      ${2:content}",
      "    </div>",
      "  );",
      "};",
      "",
      "export default ${1:ComponentName};"
    ],
    "description": "React functional component"
  }
}
```

## キーボードショートカットのカスタマイズ

### keybindings.json

```json
[
  {
    "key": "ctrl+k ctrl+d",
    "command": "editor.action.formatDocument"
  },
  {
    "key": "ctrl+shift+alt+f",
    "command": "workbench.action.findInFiles"
  },
  {
    "key": "ctrl+alt+n",
    "command": "explorer.newFile"
  },
  {
    "key": "ctrl+alt+shift+n",
    "command": "explorer.newFolder"
  },
  {
    "key": "ctrl+shift+c",
    "command": "workbench.action.terminal.openNativeConsole"
  },
  {
    "key": "alt+z",
    "command": "editor.action.toggleWordWrap"
  }
]
```

## パフォーマンス最適化

### 大きなプロジェクトでの設定

```json
{
  // ファイル監視の除外
  "files.watcherExclude": {
    "**/.git/objects/**": true,
    "**/.git/subtree-cache/**": true,
    "**/node_modules/*/**": true,
    "**/.hg/store/**": true,
    "**/dist/**": true,
    "**/build/**": true
  },
  
  // 検索除外
  "search.exclude": {
    "**/node_modules": true,
    "**/bower_components": true,
    "**/dist": true,
    "**/build": true,
    "**/.venv": true,
    "**/__pycache__": true
  },
  
  // IntelliSenseの最適化
  "typescript.suggest.autoImports": false,
  "typescript.updateImportsOnFileMove.enabled": "never",
  "javascript.suggest.autoImports": false,
  
  // 拡張機能の制限
  "extensions.autoUpdate": false,
  "extensions.autoCheckUpdates": false,
  
  // メモリ使用量の制限
  "typescript.tsserver.maxTsServerMemory": 4096,
  "files.exclude": {
    "**/node_modules": true,
    "**/.git": true,
    "**/.DS_Store": true
  }
}
```

## トラブルシューティング

### よくある問題と解決法

```bash
# 拡張機能が動作しない
1. 拡張機能を無効化して再度有効化
2. VS Codeを再起動
3. 拡張機能を再インストール

# IntelliSenseが動作しない
1. Ctrl+Shift+P → "Developer: Reload Window"
2. 言語サーバーを再起動
3. settings.jsonの言語設定を確認

# パフォーマンスが悪い
1. 不要な拡張機能を無効化
2. files.watcherExcludeの設定を追加
3. 大きなファイルの除外設定

# Git が認識されない
1. Gitのパスを確認
2. "git.path" 設定を追加
3. 環境変数PATHにGitのパスを追加
```

### 設定のリセット

```bash
# ユーザー設定のリセット
1. Ctrl+Shift+P → "Preferences: Open Settings (JSON)"
2. settings.jsonの内容を削除または必要な部分のみ残す

# 拡張機能のリセット
1. すべての拡張機能を無効化
2. 必要なもののみ再度有効化

# ワークスペース設定のリセット
1. .vscode フォルダを削除
2. 必要に応じて再設定
```

## まとめ

VS Codeは非常に柔軟で強力なエディタです。この章で学習した内容：

- **基本操作**: ファイル操作、編集、ナビゲーション
- **ショートカットキー**: 効率的な操作のためのキーボードショートカット
- **拡張機能**: 機能拡張によるカスタマイズ
- **settings.json**: 詳細な設定カスタマイズ
- **ワークスペース設定**: プロジェクト固有の設定
- **Git統合**: バージョン管理の統合機能
- **デバッグ機能**: コードのデバッグとテスト
- **スニペット**: コード入力の効率化
- **パフォーマンス最適化**: 大規模プロジェクトでの最適化

VS Codeを効果的に使うことで、開発効率を大幅に向上させることができます。設定は段階的に行い、必要に応じてカスタマイズしていくことをお勧めします。

## 次のステップ

1. **高度な拡張機能**: Docker、Kubernetes、AWS 関連の拡張機能
2. **Remote Development**: SSH、Containers、WSL を使った開発
3. **Live Share**: リアルタイムでのコラボレーション
4. **Notebook機能**: Jupyter Notebook の統合
5. **GitHub Codespaces**: クラウドベースの開発環境

毎日の開発業務でVS Codeを使いながら、徐々に便利な機能を覚えていくことで、より効率的な開発環境を構築できます。