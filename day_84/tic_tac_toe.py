# TIC TAC TOE
from tic_tac_toe_ascii import LOGO
import random as rd
import numpy as np
import os

class TicTacToe():
    def __init__(self):
        print(LOGO)
        self.board = None
        self.player_character = None
        self.start_player = None
        self.reset_game()
        self.ask_if_play()
        self.choose_player()
        self.random_start_player()
        self.run_turns()
        self.end_game()
    

    def reset_game(self):
        self.board = np.array([["_","_","_"],["_","_","_"],["_","_","_"]])


    def ask_if_play(self):
        start = None
        while start not in ("yes","no"):
            start = (str(input("Would you like to play the TicTacToe ? Type 'yes' or 'no': "))).lower()
            if start == "no":
                self.end_game()
            elif start == "yes":
                break
            else:
                print(f"Sorry, '{start}' is not a valid option.")


    def run_game(self):
        player_character = self.choose_player()
        print(f"Amazing! Your character is: {player_character}. Wish you luck!")
    

    def choose_player(self):
        player_character = None
        while player_character is None: 
            player_option = (str(input("Do you want to go with X, O or random? Type 'X','O' or 'random':\n"))).upper()
            if player_option in ("X", "O"):
                player_character = player_option
            elif player_option == "RANDOM":
                player_character = rd.choice(["X", "O"])
            else:
                print(f"Sorry, '{player_option}' is not a valid option.")
        self.player_character = player_character


    def random_start_player(self):
        self.start_player = rd.choice(["X", "O"])
        if self.start_player == self.player_character:
            print("You start first!")
        else:
            print("🤖: I start first!")
    

    def run_turns(self):
        done = False
        winner = ''
        is_player_turn = self.start_player == self.player_character
        while not done:
            if is_player_turn:
                os.system("clear")
                print(LOGO)
                self.display_board()
                self.move_player()
            else:
                self.move_robot()
            is_player_turn = not is_player_turn
            done, winner = self.win_or_loose()
        self.celebrate_winner(winner)

    def move_player(self):
        update_user = True  
        while update_user:
            try:
                user_movement = input("\nPlease choose a position for this movement in format: row,column. \n") 
                row, col = [int(item) for item in user_movement.split(",")]
                if self.board[row][col] != "_":
                    print("Sorry this is not a valid possition, please try with other.")
                else:
                    self.board[row][col] = self.player_character
                    update_user = False
            except ValueError:
                print("Invalid input. Please enter the valid format.")
            except IndexError:
                print("Please add an existing position. King reminder that columns and rows start in 0 index.")


    def move_robot(self):
        positions = list(zip(*np.where(self.board == "_")))
        if positions:
            row, col = rd.choice(positions)
        if self.board[row][col] != "_":
            raise ValueError("The robot tried to play in a not available position")
        self.board[row][col] = "O" if self.player_character == "X" else "X"


    def display_board(self):
        print(0, 1, 2, "Columns")
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])


    def win_or_loose(self):
        for player in ("O", "X"):
            for available_axis in (1, 0):
                if (np.sum(self.board == player, axis = available_axis) == 3).any():
                    return True, player
                if (np.sum(self.board == '_', axis = available_axis) == 0).any():
                    player = "DRAW"
                    return True, player
            if np.sum(np.diag(self.board) == player) == 3 or np.sum(np.diag(np.flip(self.board)) == player) == 3:
                return True, player
        return False, ''


    def celebrate_winner(self, player):
        player_celebration = ["\n🎊 Congratulation, you're the winner!", 
                              "\n🎊 You saved yourself this time, see you the next time!",
                              "\n🎊 You're amazing! Well done on winning this round!",
                              "\n🎊 You rock!",
                              "\n🎊 I knew you could do it!"
                              ]
        robot_celebration = ["🤖: I win, MUAHAHAHAHA!", 
                              "🤖: Go home, train and return when you're at my level!", 
                              "🤖: I ROCK and I win!",
                              "🤖: Oh yeah, Robot time!"
                            ]
        self.display_board()
        if self.player_character == player:
            print(rd.choice(player_celebration))
        elif player == "DRAW":
            ("The Result is DRAW!!! Games too competitive!!!")
        else:
            print(rd.choice(robot_celebration))
    

    def end_game(self):
        print("\nThank you for playing the TicTacToe game.")
        print("I would love to improve this program.\nDrop me an email at: mariabalos16@gmail.com if you have any feedback 🤗.")
        quit()


    def display_board(self):
        '''A function to show the board'''
        print(self.board)


if __name__ == "__main__":
    game = TicTacToe()
