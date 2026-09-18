import json
import random
import threading
import time
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

import keyboard
import pyperclip
from pynput.keyboard import Controller


APP_VERSION = "v0.3.0"
HISTORY_FILE = Path.home() / ".amy_clipboard_history.json"
MAX_HISTORY = 50


class AmyTypingEngine:
    def __init__(self, wpm=45):
        self.keyboard = Controller()
        self.wpm = wpm
        self.stop_requested = False
        self.paused = False
        self.typing = False
        self.human_variation = True
        self.punctuation_pauses = True

    def calculate_delay(self):
        characters_per_second = (self.wpm * 5) / 60
        base_delay = 1 / characters_per_second

        if self.human_variation:
            return base_delay * random.uniform(0.65, 1.35)

        return base_delay

    def type_text(self, text):
        self.stop_requested = False
        self.typing = True
        update_status("Typing...")

        for char in text:
            if self.stop_requested:
                break

            while self.paused and not self.stop_requested:
                time.sleep(0.1)

            if self.stop_requested:
                break

            self.keyboard.type(char)
            delay = self.calculate_delay()

            if self.punctuation_pauses:
                if char in ".!?":
                    delay += random.uniform(0.15, 0.35)
                elif char in ",;:":
                    delay += random.uniform(0.05, 0.15)

            if char == " ":
                delay += random.uniform(0.02, 0.08)

            time.sleep(delay)

        self.typing = False
        update_status("Stopped" if self.stop_requested else "Finished")

    def stop(self):
        self.stop_requested = True
        self.paused = False

    def pause_resume(self):
        if not self.typing:
            return

        self.paused = not self.paused
        update_status("Paused" if self.paused else "Typing...")


amy = AmyTypingEngine(wpm=45)

clipboard_history = []
typing_history = []
text_queue = []


def load_history():
    global clipboard_history

    try:
        if HISTORY_FILE.exists():
            data = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
            if isinstance(data, list):
                clipboard_history = [str(item) for item in data][:MAX_HISTORY]
    except (OSError, json.JSONDecodeError):
        clipboard_history = []


def save_history():
    try:
        HISTORY_FILE.write_text(
            json.dumps(clipboard_history[:MAX_HISTORY], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    except OSError:
        pass


def add_to_clipboard_history(text):
    if not text:
        return

    if text in clipboard_history:
        clipboard_history.remove(text)

    clipboard_history.insert(0, text)
    del clipboard_history[MAX_HISTORY:]
    save_history()


def add_to_typing_history(text):
    if text and text not in typing_history:
        typing_history.insert(0, text)
        del typing_history[MAX_HISTORY:]


def clipboard_stats(text):
    return {
        "characters": len(text),
        "words": len(text.split()),
        "lines": len(text.splitlines()) if text else 0,
    }


def check_clipboard():
    text = pyperclip.paste()

    if not text:
        update_status("Clipboard is empty")
        messagebox.showinfo(
            "Amy - Clipboard",
            "[AMY] Clipboard is empty.\n\nCopy some text and try again.",
        )
        return

    stats = clipboard_stats(text)
    add_to_clipboard_history(text)

    duplicate = text in clipboard_history[1:]
    already_typed = text in typing_history

    message = (
        "[AMY] Checking clipboard...\n\n"
        "✓ Clipboard contains text\n"
        f"✓ Characters: {stats['characters']:,}\n"
        f"✓ Words: {stats['words']:,}\n"
        f"✓ Lines: {stats['lines']:,}\n"
        "✓ Status: Ready to type\n"
    )

    if duplicate:
        message += (
            "\n⚠ This text is already in clipboard history.\n"
            "⚠ This text may already have been checked before.\n"
        )

    if already_typed:
        message += (
            "\n⚠ This text has already been typed by Amy.\n"
            "⚠ Typing it again may create a duplicate.\n"
        )

    message += "\n[AMY] Clipboard checked."

    # Checking never starts typing.
    messagebox.showinfo("Amy - Check Clipboard", message)
    update_status("Clipboard checked")


def view_clipboard_history():
    if not clipboard_history:
        messagebox.showinfo("Clipboard History", "Clipboard history is empty.")
        return

    window = tk.Toplevel(root)
    window.title("Amy - Clipboard History")
    window.geometry("650x450")

    tk.Label(
        window,
        text="Clipboard History",
        font=("Arial", 16, "bold"),
    ).pack(pady=10)

    listbox = tk.Listbox(window, width=90, height=15)
    listbox.pack(padx=15, pady=5, fill="both", expand=True)

    for index, text in enumerate(clipboard_history, start=1):
        preview = " ".join(text.split())
        if len(preview) > 80:
            preview = preview[:77] + "..."
        listbox.insert(tk.END, f"{index}. {preview}")

    def show_selected():
        selection = listbox.curselection()
        if not selection:
            return

        text = clipboard_history[selection[0]]
        messagebox.showinfo("Clipboard Entry", text, parent=window)

    tk.Button(
        window,
        text="View Selected",
        width=15,
        command=show_selected,
    ).pack(pady=10)


def clear_clipboard_history():
    global clipboard_history

    if not clipboard_history:
        update_status("Clipboard history is already empty")
        return

    if messagebox.askyesno(
        "Clear Clipboard History",
        "Clear all clipboard history?",
    ):
        clipboard_history = []
        save_history()
        update_status("Clipboard history cleared")


def add_current_clipboard_to_queue():
    text = pyperclip.paste()

    if not text:
        update_status("Clipboard is empty")
        return

    if text in text_queue:
        messagebox.showwarning(
            "Duplicate Queue Item",
            "This text is already in the typing queue.",
        )
        return

    text_queue.append(text)
    add_to_clipboard_history(text)
    update_queue_display()
    update_status(f"Added to queue ({len(text_queue)} item(s))")


def view_queue():
    window = tk.Toplevel(root)
    window.title("Amy - Text Queue")
    window.geometry("650x450")

    tk.Label(
        window,
        text="Multiple Text Queue",
        font=("Arial", 16, "bold"),
    ).pack(pady=10)

    listbox = tk.Listbox(window, width=90, height=15)
    listbox.pack(padx=15, pady=5, fill="both", expand=True)

    def refresh():
        listbox.delete(0, tk.END)
        for index, text in enumerate(text_queue, start=1):
            preview = " ".join(text.split())
            if len(preview) > 80:
                preview = preview[:77] + "..."
            listbox.insert(tk.END, f"{index}. {preview}")

    def remove_selected():
        selection = listbox.curselection()
        if not selection:
            return
        del text_queue[selection[0]]
        refresh()
        update_queue_display()

    def type_next():
        if amy.typing:
            messagebox.showwarning("Amy", "Amy is already typing.", parent=window)
            return

        if not text_queue:
            messagebox.showinfo("Amy", "The queue is empty.", parent=window)
            return

        text = text_queue.pop(0)
        refresh()
        update_queue_display()
        start_text_typing(text)

    refresh()

    controls = tk.Frame(window)
    controls.pack(pady=10)

    tk.Button(
        controls,
        text="Type Next",
        width=12,
        command=type_next,
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        controls,
        text="Remove Selected",
        width=15,
        command=remove_selected,
    ).grid(row=0, column=1, padx=5)


def update_queue_display():
    queue_count_label.config(text=f"Queue: {len(text_queue)} item(s)")


def start_text_typing(text):
    if amy.typing:
        return

    if not text:
        update_status("No text to type")
        return

    add_to_clipboard_history(text)
    update_status("Starting...")
    time.sleep(1)

    threading.Thread(
        target=amy.type_text,
        args=(text,),
        daemon=True,
    ).start()


def start_typing():
    if amy.typing:
        return

    text = pyperclip.paste()

    if not text:
        update_status("Clipboard is empty")
        return

    add_to_clipboard_history(text)

    duplicate = text in clipboard_history[1:]
    already_typed = text in typing_history

    if duplicate or already_typed:
        reasons = []
        if duplicate:
            reasons.append("This text is already in clipboard history.")
        if already_typed:
            reasons.append("This text has already been typed by Amy.")

        choice = messagebox.askyesnocancel(
            "Amy - Duplicate Detection",
            "\n".join(reasons)
            + "\n\nType this text anyway?\n\n"
            + "Yes = Type anyway\n"
            + "No = Skip\n"
            + "Cancel = Check target application",
        )

        if choice is None:
            messagebox.showinfo(
                "Amy - Target Application",
                "Place your cursor in the target application, "
                "then press Start when you are ready.",
            )
            update_status("Waiting")
            return

        if not choice:
            update_status("Skipped duplicate")
            return

    threading.Thread(
        target=_delayed_type,
        args=(text,),
        daemon=True,
    ).start()


def _delayed_type(text):
    update_status("Starting...")
    time.sleep(1)

    if not amy.stop_requested:
        add_to_typing_history(text)
        amy.type_text(text)


def stop_typing():
    amy.stop()


def pause_resume():
    amy.pause_resume()


def increase_wpm():
    amy.wpm = min(120, amy.wpm + 5)
    update_wpm()


def decrease_wpm():
    amy.wpm = max(20, amy.wpm - 5)
    update_wpm()


def update_wpm():
    wpm_label.config(text=f"Current WPM: {amy.wpm}")


def slider_changed(value):
    amy.wpm = max(20, min(120, int(float(value))))
    update_wpm()


def update_status(status):
    root.after(
        0,
        lambda: status_label.config(text=f"Status: {status}"),
    )


def toggle_human_variation():
    amy.human_variation = human_var.get()


def toggle_punctuation():
    amy.punctuation_pauses = punctuation_var.get()


def quit_app():
    amy.stop()
    keyboard.unhook_all()
    root.destroy()


# -----------------------------
# GUI
# -----------------------------

load_history()

root = tk.Tk()
root.title("Amy v0.3.0 - Windows Typing Agent")
root.geometry("520x620")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="AMY v0.3.0",
    font=("Arial", 22, "bold"),
)
title_label.pack(pady=(18, 3))

subtitle_label = tk.Label(
    root,
    text="Windows Typing Agent • Clipboard System",
    font=("Arial", 11),
)
subtitle_label.pack()

wpm_label = tk.Label(
    root,
    text="Current WPM: 45",
    font=("Arial", 14, "bold"),
)
wpm_label.pack(pady=(15, 5))

speed_slider = ttk.Scale(
    root,
    from_=20,
    to=120,
    orient="horizontal",
    length=330,
    command=slider_changed,
)
speed_slider.set(45)
speed_slider.pack(pady=5)

speed_range = tk.Label(root, text="20 WPM                 120 WPM")
speed_range.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="Start",
    width=14,
    command=start_typing,
).grid(row=0, column=0, padx=4, pady=4)

tk.Button(
    button_frame,
    text="Check Clipboard",
    width=16,
    command=check_clipboard,
).grid(row=0, column=1, padx=4, pady=4)

tk.Button(
    button_frame,
    text="Add to Queue",
    width=14,
    command=add_current_clipboard_to_queue,
).grid(row=1, column=0, padx=4, pady=4)

tk.Button(
    button_frame,
    text="View Queue",
    width=16,
    command=view_queue,
).grid(row=1, column=1, padx=4, pady=4)

tk.Button(
    button_frame,
    text="Clipboard History",
    width=14,
    command=view_clipboard_history,
).grid(row=2, column=0, padx=4, pady=4)

tk.Button(
    button_frame,
    text="Clear History",
    width=16,
    command=clear_clipboard_history,
).grid(row=2, column=1, padx=4, pady=4)

tk.Button(
    button_frame,
    text="Pause / Resume",
    width=14,
    command=pause_resume,
).grid(row=3, column=0, padx=4, pady=4)

tk.Button(
    button_frame,
    text="Stop",
    width=16,
    command=stop_typing,
).grid(row=3, column=1, padx=4, pady=4)

human_var = tk.BooleanVar(value=True)
tk.Checkbutton(
    root,
    text="Human-like variation",
    variable=human_var,
    command=toggle_human_variation,
).pack()

punctuation_var = tk.BooleanVar(value=True)
tk.Checkbutton(
    root,
    text="Punctuation pauses",
    variable=punctuation_var,
    command=toggle_punctuation,
).pack()

queue_count_label = tk.Label(
    root,
    text="Queue: 0 item(s)",
    font=("Arial", 10, "bold"),
)
queue_count_label.pack(pady=(8, 2))

status_label = tk.Label(
    root,
    text="Status: Ready",
    font=("Arial", 11),
)
status_label.pack(pady=8)

hotkeys_label = tk.Label(
    root,
    text=(
        "Ctrl+Shift+A  Start / Duplicate Check\n"
        "Ctrl+Shift+C  Check Clipboard\n"
        "Ctrl+Shift+P  Pause / Resume\n"
        "Ctrl+Shift+X  Stop\n"
        "Ctrl+Shift+↑  +5 WPM\n"
        "Ctrl+Shift+↓  -5 WPM\n"
        "Ctrl+Shift+Q  Quit"
    ),
    justify="left",
)
hotkeys_label.pack(pady=5)

keyboard.add_hotkey("ctrl+shift+a", start_typing)
keyboard.add_hotkey("ctrl+shift+c", check_clipboard)
keyboard.add_hotkey("ctrl+shift+p", pause_resume)
keyboard.add_hotkey("ctrl+shift+x", stop_typing)
keyboard.add_hotkey("ctrl+shift+up", increase_wpm)
keyboard.add_hotkey("ctrl+shift+down", decrease_wpm)
keyboard.add_hotkey("ctrl+shift+q", quit_app)

root.protocol("WM_DELETE_WINDOW", quit_app)
root.mainloop()
