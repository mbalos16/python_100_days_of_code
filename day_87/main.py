"""
Breakout was a hit game originally coded up by Steve Wozniak before he and Jobs started Apple. 
It's a simple game that is similar to Pong where you use a ball and paddle to break down a wall.

Breakout Wikipedia Page: https://en.wikipedia.org/wiki/Breakout_(video_game) 
You can try out the gameplay here: https://elgoog.im/breakout/

A good starting point is to review the lessons on Day 22 when we built the Pong game. 
But you will have plenty of things to Google, figure out and struggle through to complete this project. 
Try to avoid going to a tutorial on how to build breakout, instead spec out the project, figure out how 
it's going to work. Write down a checklist of todos and draw out a flow chart (if it helps).
"""

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard
from blocks import Block
import tkinter as tk
import math

TURTLE_PX =  21
class Breakout:
    def __init__(self) -> None:
        self.screen_width = 800
        self.screen_height = 600
        self.background_color = "#302030"
        self.game_is_on()

    def create_screen(self, screen_obj):
        screen_obj.tracer(0)
        screen_obj.setup(self.screen_width, self.screen_height)
        screen_obj.title("Breakout Game")
        screen_obj.bgcolor(self.background_color)
        return screen_obj

    def create_blocks(self):
        blocks = []
        x_pos, y_pos = -380, 240
        for block in range(16):
            block = Block(x_pos=x_pos, y_pos=y_pos).draw()
            blocks.append([block.xcor(), block.ycor()])
            x_pos += 50

        # Second line of blocks coord
        y_pos -= 50
        x_pos -= 50
        for block in range(16):
            block = Block(x_pos=x_pos, y_pos=y_pos).draw()
            blocks.append([block.xcor(), block.ycor()])
            x_pos -= 50

        # Third line of blocks coord
        y_pos -= 50
        x_pos += 50
        for block in range(16):
            block = Block(x_pos=x_pos, y_pos=y_pos).draw()
            blocks.append([block.xcor(), block.ycor()])
            x_pos += 50

        # Create the main blocks
        blocks = [
            Block(x_pos=position[0], y_pos=position[1]).draw() for position in blocks
        ]
        return blocks

    def update_direction(self, paddle, ball):
        """ Compute the new collision angle asumming that the shape of the paddle is a semicircle.

        Args:
            paddle (Turtle): Instanced object of the paddle.
            ball (Turtle): Instanced object of the ball.
        """
        R = paddle.width / 2 * TURTLE_PX # Defie the radius
        if ball.x_direction == 0: 
            alpha = math.pi / 2
        else:
            alpha = math.atan(abs(ball.y_direction / ball.x_direction))
                    
        Dx = ball.xcor() - paddle.xcor()
        if Dx <= -R:
            Dx = -R
        elif Dx > R:
            Dx = R
            
        theta = math.acos(Dx / R)
        new_alpha = 2 * theta - alpha
        ball.x_direction = int(round(5 * math.cos(new_alpha)))
        ball.y_direction = max(int(round(5 * abs(math.sin(new_alpha)))), 1)
        
    def detect_collision_with_block(self, block, ball):
        """Detect whether there is a collision between the ball and the paddle and bance depending on direction.

        Args:
            block (Turtle): Instanced object of the block.
            ball (Turtle): Instanced object of the ball.

        Returns:
            int: Return 1 for y collision, 0 for no collision and -1 for x collision.
        """
        R = ball.width / 2 * TURTLE_PX
        distance_collision = block.width * TURTLE_PX / 2 + R
        Dx = abs(ball.xcor() - block.xcor())
        Dy = abs(ball.ycor() - block.ycor())
        if Dx < distance_collision and Dy < distance_collision:
            if Dx > Dy:
                return -1
            else:
                return 1
        else:
            return 0
     
    def game_over(self, blocks, score, ball):
        if len(blocks) <= 0:
            game_is_played = False
            msg = tk.messagebox.showinfo(
                "alert",
                f"Well done 🎉! \nYou win with the maximum score available: {score.score}!",
            )
            exit()  # Exit the game
        elif ball.ycor() <= -320:
            msg = tk.messagebox.showinfo(
                "alert",
                f"GAME OVER!\n Your final score is: {score.score}",
            )
            exit()  # Exit the game

    def game_is_on(self):
        screen = Screen()  # Initiate a screen
        self.create_screen(screen)  # Create the screen
        paddle = Paddle(x_pos=0, y_pos=-270)  # Initiate the paddle
        score = Scoreboard()  # Initiate the score
        blocks = self.create_blocks()  # create all blocks
        ball = Ball(x_pos=0, y_pos=-250)  # Initiate the Ball
        game_is_played = True  # game condition
        vertical_distance_coision = (ball.height + paddle.height) * 0.5 * TURTLE_PX
        horizontal_distance_coision = (ball.width + paddle.width) * 0.5 * TURTLE_PX


        while game_is_played:
            screen.update()  # Update the screen
            ball.movement()  # Move the ball
            # Paddle movement
            screen.onkeypress(paddle.go_right, "Right")  # Control the paddle to the right
            screen.onkeypress(paddle.go_left, "Left")  # Control the paddle to the left
            screen.listen()  # Make the screen to listen to the keyboard
        
        
            # Condition of the ball baunce when touching the paddle
            if (ball.ycor() - paddle.ycor()) < vertical_distance_coision:
                if abs(ball.xcor() - paddle.xcor()) < horizontal_distance_coision:
                    if ball.y_direction < 0:
                        # Update ther direction of the ball when collisioning with the paddle
                        self.update_direction(paddle, ball)
                        
            # Define the app walls
            if ball.ycor() > 285:
                ball.baunce_y()
            if ball.xcor() > 380 or ball.xcor() < -385:
                ball.baunce_x()
                
            for block in blocks:
                # Detect collision with the block
                collision_detected = self.detect_collision_with_block(block, ball)
                if collision_detected != 0: # Not collision
                    if collision_detected == 1: # Vertical collision
                        ball.baunce_y()  # Baunce ball y
                    else: # Horizontal collision
                        ball.baunce_x()  # Baunce ball x
                    block.color(self.background_color)  # Delete block
                    blocks.remove(block)  # Remove it from the list of balls
                    score.point()  # Add a new point to the score
                    score.update_text()  # Update score
            self.game_over(blocks, score=score, ball=ball)

if __name__ == "__main__":
    GAME = Breakout()