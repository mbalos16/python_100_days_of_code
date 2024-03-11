from turtle import Screen
from constants import SCREEN_BG_COLOR


def build_main_screen():
    screen = Screen()
    screen.screensize(400, 600)
    screen.title = "· Space invaders ·"
    screen.bgcolor = SCREEN_BG_COLOR
    return screen

if __name__ == "__main__":
    screen = build_main_screen()
