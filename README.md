# 🌱 Amy — Human-Like AI Typing Agent

> A Windows and Linux desktop typing agent designed to type copied text into the currently focused application at a natural, configurable speed.

**Current version: v0.1**

Amy is being built as a cross-platform desktop assistant. The first release focuses on one simple idea:

**Copy text → press a shortcut → Amy types it for you.**

The project keeps the Windows and Linux implementations separate because global keyboard input works differently across operating systems and Linux desktop environments.

---

## ✨ v0.1 Features

- 📋 Reads text from the system clipboard
- ⌨️ Types text into the currently focused application
- 🧑 Human-like variable keystroke timing
- ⚡ Default typing speed: approximately 45 WPM
- 🛑 Emergency stop shortcut
- 🌐 Separate Windows and Linux implementations
- 🧵 Background typing so the application remains responsive

### Human-like timing

Amy does not use one fixed delay for every character.

It introduces small variations between keystrokes and adds additional pauses around:

- `.`, `!`, `?`
- `,`, `;`, `:`
- spaces

This is intended to make the typing feel less mechanical.

---

## 🖥️ Platform Support

| Platform | Status | Implementation |
|---|---|---|
| Windows 10/11 | 🟢 v0.1 | `keyboard` + `pynput` |
| Linux X11 | 🟢 v0.1 | `pynput.GlobalHotKeys` |
| Linux Wayland | 🟡 Environment dependent | Additional work required |

> Linux Wayland can restrict global keyboard hooks and synthetic keyboard input. Support will be improved in a future version.

---

## 📁 Project Structure

```text
Amy/
├── linux/
│   ├── main.py
│   └── requirements.txt
│
├── windows/
│   ├── main.py
│   └── requirements.txt
│
├── docs/
│   └── development.md
│
├── .gitignore
├── LICENSE
└── README.md
```

---

# 🐧 Linux Installation

These instructions target Debian/Kali/Ubuntu-style distributions.

### 1. Install Python

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### 2. Clone the repository

```bash
git clone https://github.com/Rubesh1420/amy-ai-typing-agent.git
cd amy-ai-typing-agent
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r linux/requirements.txt
```

### 5. Run Amy

```bash
python3 linux/main.py
```

### Linux shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl + Shift + A` | Start typing clipboard |
| `Ctrl + Shift + X` | Stop typing |
| `Ctrl + Shift + Q` | Quit |

---

# 🪟 Windows Installation

### 1. Install Python

Install Python 3 from the official Python website and make sure Python is available from the command line.

### 2. Clone the repository

```powershell
git clone https://github.com/Rubesh1420/amy-ai-typing-agent.git
cd amy-ai-typing-agent
```

### 3. Create a virtual environment

```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 4. Install dependencies

```powershell
pip install -r windows/requirements.txt
```

### 5. Run Amy

```powershell
python windows/main.py
```

### Windows shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl + Shift + A` | Start typing clipboard |
| `Ctrl + Shift + X` | Stop typing |
| `Ctrl + Shift + Q` | Quit |

---

# 🧪 Testing

A simple test:

1. Copy some text.
2. Open Notepad/Text Editor.
3. Click inside the document.
4. Press `Ctrl + Shift + A`.
5. Amy types the clipboard content.

Example:

```text
Hello! I am Amy, your human-like typing assistant.

This is a test of the Amy v0.1 typing engine.
The goal is to save time by typing copied text automatically.
```

---

# 🛣️ Roadmap

## v0.1 — Human-like typing
- [x] Clipboard input
- [x] Keyboard typing
- [x] Variable typing speed
- [x] Start/stop shortcuts
- [x] Windows implementation
- [x] Linux implementation

## v0.2 — Desktop interface
- [ ] System tray application
- [ ] Speed slider
- [ ] Start/stop buttons
- [ ] Status indicator
- [ ] Configuration file

## v0.3 — AI features
- [ ] AI rewrite
- [ ] AI summarization
- [ ] AI translation
- [ ] AI question answering
- [ ] Multiple AI providers

## v0.4 — Screen intelligence
- [ ] OCR
- [ ] Screen text extraction
- [ ] Context-aware actions

## Future
- [ ] Voice commands
- [ ] Local LLM support
- [ ] Better Wayland support
- [ ] Packaging/installers
- [ ] Plugin system

---

# 🤖 Vision

Amy is intended to become more than an auto-typer.

The long-term goal is a desktop AI agent that can understand what the user is working on and help enter, transform, and generate text without constantly switching between applications.

```text
                 ┌─────────────┐
                 │     Amy     │
                 │ AI Desktop  │
                 │   Agent     │
                 └──────┬──────┘
                        │
          ┌─────────────┼─────────────┐
          │             │             │
      Clipboard       Screen         Voice
          │             │             │
          └─────────────┼─────────────┘
                        │
                     AI Model
                        │
                        ▼
                 Typing Engine
                        │
                        ▼
              Current Windows/Linux App
```

---

# 📜 License

MIT License — see `LICENSE`.

---

## ⭐ Project Status

Amy is currently an early-stage project.

**Version 0.1:** Basic human-like clipboard typing.

Contributions, ideas, bug reports, and improvements are welcome.
