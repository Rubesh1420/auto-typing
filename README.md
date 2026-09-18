# Amy v0.3.0 — Windows Smart Typing Agent

Amy is a Windows-based human-like typing and text automation agent designed to make text input more reliable, controlled, and intelligent.

## ✨ Features

* Human-like character-by-character typing
* Adjustable typing speed (WPM)
* Start, pause, resume, and stop typing
* Emergency stop
* Clipboard monitoring
* Multiple copied-text handling
* Clipboard history
* Clipboard check option
* Duplicate clipboard detection
* Already-typed text detection
* Large-text handling
* Line-break and multi-line text support
* Prevention of multiple typing sessions
* Error handling and logging
* Active Windows application awareness

## 🔄 How Amy Works

```text
Clipboard
    ↓
Clipboard Manager
    ↓
Duplicate Detection
    ↓
Already-Typed Detection
    ↓
Text Queue
    ↓
Typing Engine
    ↓
Windows Input
    ↓
Target Application
```

Amy checks copied text before typing to help prevent accidentally typing the same content multiple times.

## 📋 Clipboard Check

Amy can check the current clipboard without automatically typing anything.

Example:

```text
[AMY] Checking clipboard...

✓ Clipboard contains text
✓ Characters: 248
✓ Words: 42
✓ Lines: 5
✓ Status: Ready
```

If the clipboard is empty:

```text
[AMY] Clipboard is empty.
```

The clipboard check only analyzes the current clipboard content. It does **not** automatically start typing.

## 📚 Multiple Clipboard Texts

Amy can handle different copied texts while a typing operation is in progress.

Example:

```text
Text 1 → Currently typing
Text 2 → Waiting
Text 3 → Waiting
```

This allows copied content to be managed without interrupting the current typing operation.

## 🔁 Duplicate Detection

If the same text is copied multiple times, Amy can detect the duplicate and prevent unnecessary repeated processing.

Example:

```text
[AMY] Duplicate clipboard text detected.
[AMY] Skipping duplicate text.
```

Amy can also detect text that has already been processed or typed and prevent unnecessary repetition.

## ⌨️ Human-Like Typing

Amy types text character by character instead of instantly pasting the complete text.

Typing speed is controlled using **WPM (Words Per Minute)**, with small variations in timing to create more natural input.

Punctuation and spaces can introduce slightly longer pauses.

## 🪟 Windows Compatibility

Amy is designed for use with Windows applications that accept normal keyboard input, including:

* Visual Studio Code
* Notepad
* Google Chrome
* Microsoft Edge
* Firefox
* Command Prompt
* PowerShell
* Microsoft Word
* Other Windows applications

Compatibility may vary depending on how an application handles keyboard input.

## 🚀 Installation

### Requirements

* Windows
* Python 3.x
* Git

### 1. Clone the repository

```bash
git clone https://github.com/Rubesh1420/Amy.git
```

### 2. Navigate to the project

```bash
cd Amy
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Running Amy

Start Amy using:

```bash
python apps/windows/main.py
```

Make sure the intended target application and input field are focused before starting a typing operation.

## 📝 Basic Workflow

1. Copy your text.
2. Start Amy.
3. Check the clipboard if needed.
4. Focus the target application.
5. Start the typing operation.
6. Amy checks the clipboard content.
7. Amy detects duplicates or already-typed text.
8. The text is added to the typing queue.
9. Amy types the content character by character.
10. Amy reports the result.

## 🛑 Safety

Amy is an automation tool. Always make sure the correct application and input field are focused before starting a typing operation.

If Amy begins typing into the wrong application, use the **emergency stop** to immediately stop the current operation.

## 📌 Project Status

**Amy v0.3.0 — Windows**

Focus:

* Reliable typing
* Intelligent clipboard handling
* Duplicate prevention
* Already-typed text detection
* Multiple clipboard text handling
* Windows application awareness

## 👨‍💻 Author

Created by **Rubesh**

GitHub:
https://github.com/Rubesh1420/Amy
