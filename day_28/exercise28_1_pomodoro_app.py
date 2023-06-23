# Exercise28.1 Pomodoro app

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
NAVY = "#263032"
FONT_NAME = "Times New Roman"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)

    # timer_text(00:00)
    canvas.itemconfig(timer_text, text="00:00")

    # title_label "Timer"
    title["text"] = "Timer"

    # reset check_marks
    check_marks.config(text="")

    # reset REPS
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 8th rep:
    if REPS % 8 == 0:
        count_down(long_break_sec)
        title["text"] = "Break"
        title["fg"] = RED

    # If it's the 2nd/4th/6th rep:
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        title["text"] = "Break"
        title["fg"] = PINK

    # If it's the 1st/3rd/5th/7th rep:
    else:
        count_down(work_sec)
        title["text"] = "Work"
        title["fg"] = GREEN


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    global REPS

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

# Create the screen.
window = Tk()
window.title("BMM • Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title
title = Label(text="Timer", font=(FONT_NAME, 26, "bold"), fg=GREEN, bg=YELLOW)
title.grid(column=1, row=0)

# Tomato and timer.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="day_28/exercise28_1_pomodoro_app_tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold")
)
canvas.grid(column=1, row=1)

# Start button
start_button = Button(
    text="Start",
    font=(FONT_NAME, 14, "bold"),
    bg=GREEN,
    highlightthickness=0,
    fg="green",
    command=start_timer,
)
start_button.grid(column=0, row=2)

# Timer
check_marks = Label(font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

# Reset button
reset_button = Button(
    text="Reset",
    font=(FONT_NAME, 14, "bold"),
    command=reset_timer,
    bg=GREEN,
    highlightthickness=0,
    fg="green",
)

reset_button.grid(column=2, row=2)

window.mainloop()
