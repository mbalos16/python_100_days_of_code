from turtle import Screen, Turtle
import time

DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0


class Snake:
    # Creation of the 3 initial snake body segments
    def __init__(self):
        self.initial_size = 3
        self.segment_size = 20
        self.segment_x = 0
        self.segment_y = 0
        self.segments = []
        self.born()
        self.move_distance = 20

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("AntiqueWhite")
        new_segment.penup()
        new_segment.setposition(x=position[0], y=position[1])
        self.segments.append(new_segment)
        # self.segment_x -= self.segment_size

    def born(self):
        for i in range(self.initial_size):
            position = (-i * self.segment_size, 0)
            self.add_segment(position)
        self.head = self.segments[0]

    def move(self):
        # this is what we have as range in bellow: start = len(segments)-1, stop = 0, step = -1
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.head.forward(self.move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        # add a new segment to the snake.
        self.add_segment(self.segments[-1].position())
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.initial_size = 3
        self.segment_size = 20
        self.segment_x = 0
        self.segment_y = 0
        self.born()
        self.move_distance = 20
        
        