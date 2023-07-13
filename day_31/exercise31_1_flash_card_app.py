# Exercise 31.1. Flash Card app

from tkinter import *
from tkinter import messagebox
import pandas as pd
import random



BACKGROWND_COLOR = "#B1DDC6"



# -------------- ACCESS DATA AND CREATE NEW FLASH CARD -------------- #
try:
    with open("day_31/exercise31_1_flash_card_words_to_learn.csv") as file:
        to_learn = file.to_dict(orient="records")
except FileNotFoundError:
    df = pd.read_csv("day_31/exercise31_1_flash_card_french_words.csv")
    to_learn = df.to_dict(orient="records")


current_card = {}


def random_selection():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.randint(0, len(to_learn))
    french_word = to_learn[current_card]['French']
    canvas.itemconfig(card_title, text="French", fill = "black")
    canvas.itemconfig(card_word, text=french_word, fill = "black")
    canvas.itemconfig(canvas_image, image = card_front)
    flip_timer = window.after(3000, func=flip_card)


# -------------- TURN THE CARD AND SHOW CORRECT ANSWER -------------- #
def flip_card():
    english_word = to_learn[current_card]['English']
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")
    canvas.itemconfig(canvas_image, image = card_back)


def known_word():
    global current_card
    random_selection()
    to_learn.remove(to_learn[current_card])
    new_list = pd.DataFrame(to_learn)
    new_list.to_csv("day_31/exercise31_1_flash_card_words_to_learn.csv", index = False)
    
    
def unknown_word():
    random_selection()


# ---------------------------- UI SETUP ------------------------------- #
# Create the window
window = Tk()
window.title("BMM • Flashy")
window.config(padx=50, pady=50, bg=BACKGROWND_COLOR)

flip_timer = window.after(3000, flip_card)


# Create the canvas and upload the image
canvas = Canvas(width=800, height=526, bg=BACKGROWND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="day_31/exercise31_1_flash_card_card_front.png")
card_back = PhotoImage(file="day_31/exercise31_1_flash_card_card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)



# Buttons
error_button_img = PhotoImage(file="day_31/exercise31_1_flash_card_wrong.png")
error_button = Button(image=error_button_img, highlightthickness=0, bg=BACKGROWND_COLOR, command=unknown_word)
error_button.grid(row=1, column=0)

ok_button_img = PhotoImage(file="day_31/exercise31_1_flash_card_right.png")
ok_button = Button(image=ok_button_img, highlightthickness=0, bg=BACKGROWND_COLOR, command=known_word)
ok_button.grid(row=1, column=1)


random_selection()


window.mainloop()