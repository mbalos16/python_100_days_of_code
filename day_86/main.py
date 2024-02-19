from tkinter import Label, Button, END, Canvas
import tkinter as tk
import math


class Typing:
    def __init__(self, window):
        self.blush_color = "#C96480"
        self.black_olive_color = "#363732"
        self.isabelline_color = "#f1e8e6"
        self.mint_green_color = "#3EB489"
        self.sunglow_color = "#FFD166"
        self.title_font_name = "Impact"
        self.text_font_name = "Avenir"
        self.type_minutes = 1
        self.min = math.floor(self.type_minutes / 60)
        self.sec = self.type_minutes * 60
        self.setup_tkinter(window)

    def setup_tkinter(self, window):
        self.window = window
        window.title("Typing speed test")
        window.configure(background=self.black_olive_color)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        # Title label
        self.label = Label(
            window,
            text="              ⚡     Typing Thunder     ⚡             ",
            bd=0,
            fg=self.black_olive_color,
            bg=self.blush_color,
            font=(self.title_font_name, 56, "bold"),
        )
        self.label.pack(pady=20)

        # Subtitle label
        self.subtitle_label = Label(
            window,
            text=f"A speed typing app where you can test your typing velocity for {self.type_minutes} minute!",
            bd=0,
            fg=self.sunglow_color,
            bg=self.black_olive_color,
            font=(self.text_font_name, 16, "bold"),
        )
        self.subtitle_label.pack(padx=5, pady=5)

        # Explanation label
        self.explanation_label = Label(
            window,
            text=f"When time ends, the words and characters will be count.\n Your score will be checks against other users in the app.\nIf you are the one with the highest score we will let you know.\n Wish you luck!",
            bd=0,
            fg=self.isabelline_color,
            bg=self.black_olive_color,
            font=(self.text_font_name, 14),
        )
        self.explanation_label.pack(padx=5, pady=5)

        # Timer
        self.canvas = Canvas(
            width=600,
            height=40,
            highlightthickness=0,
            background=self.black_olive_color,
        )
        self.timer_text = self.canvas.create_text(
            300,
            20,
            text="00:00",
            fill=self.mint_green_color,
            font=(self.text_font_name, 28, "bold"),
            justify="center",
        )
        self.canvas.pack()

        # Subtitle label
        self.write_text = Label(
            window,
            text="When you feel prepared, hit the start to turn on the timer and start writing.",
            bd=0,
            fg="White",
            bg=self.black_olive_color,
            font=(self.text_font_name, 12),
        )

        # Start speed counter button
        self.calculate_speed_btn = Button(
            window,
            border=0,
            borderwidth=0,
            highlightbackground=self.black_olive_color,
            fg="#543c52",
            text="START",
            command=lambda: self.count_down_time(
                self.timer_text, self.min, self.sec, self.user_text
            ),
            font=(self.text_font_name, 16, "bold"),
        )
        self.calculate_speed_btn.pack()

        # User input label
        self.user_text = tk.Text(
            window,
            height=15,
            width=85,
            bg=self.isabelline_color,
            fg=self.black_olive_color,
        )
        self.user_text.pack(padx=40, pady=20)

        # Title label
        self.results_label = Label(
            window,
            text="",
            bd=0,
            fg=self.mint_green_color,
            bg=self.black_olive_color,
            font=(self.title_font_name, 16),
        )
        self.results_label.pack(padx=60, pady=20)

    def count_down_time(self, timer_text, min, sec, user_text):
        if sec > 0:
            if sec < 11:
                sec -= 1
                clock_text_sec = f"0{sec}"
                clock_text_min = f"{min}"
            else:
                sec -= 1
                clock_text_sec = f"{sec}"
            if min < 10:
                clock_text_min = f"0{min}"
            else:
                clock_text_min = f"{min}"
            self.canvas.itemconfig(
                timer_text, text=f"{clock_text_min}:{clock_text_sec}"
            )
            self.window.after(
                1000, self.count_down_time, timer_text, min, sec, user_text
            )
        elif min > 0:
            min -= 1
            sec = 60
            if min < 10:
                clock_text_min = f"0{min}"
            else:
                clock_text_min = f"{min}"
            clock_text_sec = f"{sec}"
            self.canvas.itemconfig(
                timer_text, text=f"{clock_text_min}:{clock_text_sec}"
            )
            self.window.after(
                1000, self.count_down_time, timer_text, min, sec, user_text
            )
        else:
            self.results_label["text"] = self.count_characters(user_text)

    def count_characters(self, user_text):
        words_per_min = user_text.get("1.0", END).split()
        characters_per_min = [
            element.split() for element in user_text.get("1.0", END).strip()
        ]
        return f"✨ Well done! ✨\n In 1 minute, you have writen {len(words_per_min)} words and {len(characters_per_min)} characters (including white spaces)."


if __name__ == "__main__":
    root = tk.Tk()
    typing = Typing(root)
    root.mainloop()
