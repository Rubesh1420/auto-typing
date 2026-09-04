# Amy — Human-Like AI Typing Agent

**Current Version: v0.2.0**

Amy is a human-like typing agent that types copied text with adjustable typing speed, natural timing variations, punctuation pauses, and keyboard controls.

> ⚠️ **v0.2.0 is currently Windows-only.**

---

## ✨ Features

* 🎚️ Adjustable typing speed: **20–120 WPM**
* 📊 Current WPM display
* ▶️ Start typing copied clipboard text
* ⏸️ Pause / Resume typing
* ■ Stop typing
* 🧑 Human-like typing variation
* ✍️ Punctuation pauses
* 📋 Clipboard-based typing
* 🖥️ Windows GUI using Tkinter
* 🧵 Background typing
* 🛑 Emergency stop
* ⌨️ Global keyboard shortcuts

---

## ⌨️ Keyboard Shortcuts

| Shortcut           | Action            |
| ------------------ | ----------------- |
| `Ctrl + Shift + A` | Start typing      |
| `Ctrl + Shift + P` | Pause / Resume    |
| `Ctrl + Shift + X` | Stop typing       |
| `Ctrl + Shift + ↑` | Increase WPM by 5 |
| `Ctrl + Shift + ↓` | Decrease WPM by 5 |
| `Ctrl + Shift + Q` | Quit Amy          |

---

## 🖥️ Requirements

* Windows 10 or Windows 11
* Python 3.10+
* Tkinter
* Python packages listed in `windows/requirements.txt`

An internet connection is **not required** while using Amy.

---

## 📁 Project Structure

```text
auto-typing/
│
├── windows/
│   ├── main.py
│   └── requirements.txt
│
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚙️ Installation

### 1. Install Python

Install Python 3.10 or newer.

Make sure **Add Python to PATH** is enabled during installation.

### 2. Clone the Repository

```bash
git clone https://github.com/Rubesh1420/auto-typing.git
```

Then:

```bash
cd auto-typing
```

### 3. Install Dependencies

```bash
python -m pip install -r windows/requirements.txt
```

---

## 🚀 Running Amy

Go into the Windows directory:

```bash
cd windows
```

Run Amy:

```bash
python main.py
```

The Amy GUI will open.

---

## 📝 How to Use

1. Start Amy with `python main.py`.
2. Copy the text you want Amy to type.
3. Choose your desired WPM using the slider.
4. Place your cursor where you want the text to appear.
5. Press **Ctrl + Shift + A**.
6. Amy will type the copied text.
7. Press **Ctrl + Shift + P** to pause or resume.
8. Press **Ctrl + Shift + X** to stop.

---

## 🎚️ Typing Speed

Amy supports typing speeds from:

```text
20 WPM ───────────────────── 120 WPM
```

You can change the speed using:

* The GUI slider
* `Ctrl + Shift + ↑`
* `Ctrl + Shift + ↓`

When human-like variation is enabled, Amy adds small random timing differences between keystrokes.

---

## 🧑 Human-Like Typing

Amy can add natural timing variations to make typing less mechanically consistent.

Additional pauses can be added around punctuation such as:

* `.`
* `!`
* `?`
* `,`
* `;`
* `:`

You can enable or disable these features from the GUI.

---

## 📋 Clipboard Support

Amy uses your Windows clipboard as its text source.

The basic workflow is:

```text
Copy text → Run Amy → Place cursor → Start typing
```

No text file is required.

---

## 🧪 Testing

You can test Amy using:

```text
Hello! My name is Amy, and I am a human-like typing agent. This is a test of the typing speed, punctuation pauses, and pause/resume features. I can type text at different speeds while adding natural variations. Let's see how well everything works!
```

Copy the text, open Amy, place your cursor in a text editor, and press:

```text
Ctrl + Shift + A
```

---

## 🛑 Emergency Stop

If Amy is typing and you need to stop immediately:

```text
Ctrl + Shift + X
```

You can also click the **Stop** button in the GUI.

---

## 🔧 Version

### v0.2.0

Amy v0.2.0 introduces:

* Windows GUI
* Adjustable WPM
* Human-like timing variation
* Punctuation pauses
* Clipboard typing
* Pause / Resume
* Stop controls
* Global keyboard shortcuts

---

## 🛣️ Future Plans

Possible future improvements:

* Better human-like typing patterns
* Typing profiles
* Custom typing behavior
* Advanced timing models
* Improved GUI
* Configuration and settings support
* Additional platform support

---

## ⚠️ Disclaimer

Amy is an experimental typing automation project created for learning, experimentation, and personal automation.

Use Amy responsibly and only where you are permitted to use typing automation.

---

## 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

## 👨‍💻 Project

**Amy — Human-Like AI Typing Agent**

**Version:** v0.2.0
**Platform:** Windows
