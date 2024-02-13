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
        """
        This program reset's the board of the game.
        """
        self.board = np.array([["_","_","_"],["_","_","_"],["_","_","_"]])


    def ask_if_play(self):
        """ 
        This function is a loop that ask the user if wants to play, if not the end function will be called.
        """
        start = None
        while start not in ("yes","no"):
            start = (str(input("Would you like to play the 🎲 TicTacToe 🎲 ? \nType 'yes' or 'no': "))).lower()
            if start == "no":
                self.end_game()
            elif start == "yes":
                break
            else:
                print(f"🤦 Sorry, '{start}' is not a valid option, please try again.\n")


    def choose_player(self):
        """ 
        This function allow the user to choose the character they want to play or being generated randomly.
        """
        self.clean_display()
        player_character = None
        while player_character is None: 
            player_option = (str(input("Do you want to go with X, O or random? Type 'X','O' or 'random':\n"))).upper()
            if player_option in ("X", "O"):
                player_character = player_option
            elif player_option == "RANDOM":
                player_character = rd.choice(["X", "O"])
            else:
                print(f"🤦 Sorry, '{player_option}' is not a valid option, please try again.\n")
        self.player_character = player_character
        print(f"\nAmazing! Your character is: {player_character}. Wish you luck!\n")


    def random_start_player(self):
        """ 
        This program randomly defines the first player of the game.
        """
        self.start_player = rd.choice(["X", "O"])
        if self.start_player == self.player_character:
            print("You start first!\n")
        else:
            print("🤖: I start first!\n")
    

    def run_turns(self):
        """ 
        This function will run the game until one the user or the robot wins. 
        """
        done = False
        is_player_turn = self.start_player == self.player_character
        turn_number=0
        while not done:
            current_player_character = self.player_character if is_player_turn else self.robot_character
            if is_player_turn:
                if turn_number > 1:
                    self.clean_display()
                self.display_board()
                self.move_player()
            else:
                self.move_robot()
            done, draw = self.win_condition(current_player_character)
            is_player_turn = not is_player_turn
            turn_number += 1
        self.celebrate_winner(current_player_character, draw)


    @staticmethod
    def clean_display():
        """
        This function is cleaning the terminal and printing the logo.
        """
        os.system("clear")
        print(LOGO)


    def move_player(self):
        """ 
        This program will allow the user to choose a position for the move.

        Raises:
            ValueError: When the user introduces an invalid format.
            IndexError: Used when the user adds an invalid index.
        """
        update_user = True
        while update_user:
            try:
                user_movement = input("\n✨ Please choose a position for this movement in format: row,column. \n") 
                row, col = [int(item) for item in user_movement.split(",")]
                if self.board[row][col] != "_":
                    print("🤦 Sorry this is not a valid position, please try again.")
                else:
                    self.board[row][col] = self.player_character
                    update_user = False
            except ValueError:
                print("🤦 Invalid input, please enter the valid format.")
            except IndexError:
                print("🤦 Please add an existing position, kind reminder that columns and rows start with index 0.")


    def move_robot(self):
        """
        This program will alow the user to make the move.

        Raises:
            ValueError: Raise an error when the user choose an invalid position.
        """
        positions = list(zip(*np.where(self.board == "_")))
        if positions:
            row, col = rd.choice(positions)
        if self.board[row][col] != "_":
            raise ValueError("🤦 The robot tried to play in a not available position")
        self.board[row][col] = self.robot_character


    @property
    def robot_character(self):
        """
        This function checks which is the robot characters and return it.

        Returns:
            string: The robot's character.
        """
        return "O" if self.player_character == "X" else "X"


    def win_condition(self, player):
        """
        This is the function that will determine the game winner.

        Args:
            player (string): This is the player for each movement.

        Returns:
            tuple: Wether the game is done and if there is a draw.
        """

        for axis in (1, 0):
            # Did the player win in vertical/horizontal?
            if (np.sum(self.board == player, axis = axis) == 3).any():
                return True, False
            
        # Did the player win in diagonal?
        if np.sum(np.diag(self.board) == player) == 3 or np.sum(np.diag(np.flip(self.board, axis = 0)) == player) == 3:
            return True, False
        
        # If not, is there a draw?
        if (np.sum(self.board == '_') == 0):
            return True, True
        
        # Nobody won this round
        return False, False


    def celebrate_winner(self, winner, draw):
        """ This function is the one that celebrates the game winner. 

        Args:
            winner (str): The character that wins the game.
            draw (str): The draw.
        """

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
        self.clean_display()
        self.display_board()
        if draw:
            ("The Result is DRAW!!! Games too competitive!!!")
        elif self.player_character == winner:
            print(rd.choice(player_celebration))
        else:
            print(rd.choice(robot_celebration))
    

    def end_game(self):
        """
        This program will print the end of the game.
        """
        print("\nThank you for playing the 🎲 TicTacToe 🎲 .")
        print("❣️ I would love to improve this game.\nDrop me an email at: mariabalos16@gmail.com if you have any feedback 🤗.")
        quit()


    def display_board(self):
        """
        This program prints the board. 
        """
        print("  0 ", " 1 ", " 2  ")
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])


if __name__ == "__main__":
    game = TicTacToe()
