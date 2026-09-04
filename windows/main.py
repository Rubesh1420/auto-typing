import time
import random
import threading
import tkinter as tk
from tkinter import ttk
import keyboard
import pyperclip
from pynput.keyboard import Controller


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
            variation = random.uniform(0.65, 1.35)
            return base_delay * variation

        return base_delay

    def type_text(self, text):
        self.stop_requested = False
        self.typing = True

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

        if self.stop_requested:
            update_status("Stopped")
        else:
            update_status("Finished")

    def stop(self):
        self.stop_requested = True
        self.paused = False

    def pause_resume(self):
        if not self.typing:
            return

        self.paused = not self.paused

        if self.paused:
            update_status("Paused")
        else:
            update_status("Typing...")


amy = AmyTypingEngine(wpm=45)


def start_typing():
    if amy.typing:
        return

    text = pyperclip.paste()

    if not text:
        update_status("Clipboard is empty")
        return

    update_status("Starting...")

    time.sleep(1)

    threading.Thread(
        target=amy.type_text,
        args=(text,),
        daemon=True
    ).start()


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
    wpm_label.config(text=f"Current WPM: {amy.wpm}")


def update_status(status):
    root.after(
        0,
        lambda: status_label.config(text=f"Status: {status}")
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

root = tk.Tk()

root.title("Amy v0.2 - Human-Like Typing Agent")
root.geometry("450x400")
root.resizable(False, False)


title_label = tk.Label(
    root,
    text="AMY v0.2",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=(20, 5))


subtitle_label = tk.Label(
    root,
    text="Human-Like Typing Agent",
    font=("Arial", 11)
)
subtitle_label.pack()


wpm_label = tk.Label(
    root,
    text="Current WPM: 45",
    font=("Arial", 14, "bold")
)
wpm_label.pack(pady=(20, 5))


speed_slider = ttk.Scale(
    root,
    from_=20,
    to=120,
    orient="horizontal",
    length=300,
    command=slider_changed
)

speed_slider.set(45)
speed_slider.pack(pady=5)


speed_range = tk.Label(
    root,
    text="20 WPM                 120 WPM"
)
speed_range.pack()


button_frame = tk.Frame(root)
button_frame.pack(pady=20)


start_button = tk.Button(
    button_frame,
    text="▶ Start",
    width=12,
    command=start_typing
)
start_button.grid(row=0, column=0, padx=5)


pause_button = tk.Button(
    button_frame,
    text="⏸ Pause / Resume",
    width=15,
    command=pause_resume
)
pause_button.grid(row=0, column=1, padx=5)


stop_button = tk.Button(
    button_frame,
    text="■ Stop",
    width=12,
    command=stop_typing
)
stop_button.grid(row=0, column=2, padx=5)


human_var = tk.BooleanVar(value=True)

human_checkbox = tk.Checkbutton(
    root,
    text="Human-like variation",
    variable=human_var,
    command=toggle_human_variation
)
human_checkbox.pack()


punctuation_var = tk.BooleanVar(value=True)

punctuation_checkbox = tk.Checkbutton(
    root,
    text="Punctuation pauses",
    variable=punctuation_var,
    command=toggle_punctuation
)
punctuation_checkbox.pack()


status_label = tk.Label(
    root,
    text="Status: Ready",
    font=("Arial", 11)
)
status_label.pack(pady=15)


hotkeys_label = tk.Label(
    root,
    text=(
        "Ctrl+Shift+A  Start\n"
        "Ctrl+Shift+P  Pause / Resume\n"
        "Ctrl+Shift+X  Stop\n"
        "Ctrl+Shift+↑  +5 WPM\n"
        "Ctrl+Shift+↓  -5 WPM\n"
        "Ctrl+Shift+Q  Quit"
    ),
    justify="left"
)
hotkeys_label.pack()


# -----------------------------
# Global Hotkeys
# -----------------------------

keyboard.add_hotkey(
    "ctrl+shift+a",
    start_typing
)

keyboard.add_hotkey(
    "ctrl+shift+p",
    pause_resume
)

keyboard.add_hotkey(
    "ctrl+shift+x",
    stop_typing
)

keyboard.add_hotkey(
    "ctrl+shift+up",
    increase_wpm
)

keyboard.add_hotkey(
    "ctrl+shift+down",
    decrease_wpm
)

keyboard.add_hotkey(
    "ctrl+shift+q",
    quit_app
)


root.protocol(
    "WM_DELETE_WINDOW",
    quit_app
)

root.mainloop()

