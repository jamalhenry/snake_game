from turtle import Turtle
#Creating the snake positions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#Class that creates the snake
class Snake:

    def __init__(self):
        #Creates an empty list to store the postions that create the snake
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        # Loop through the starting positons tuple to create the snake
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    #Method that adds to the body of the snake
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    #Adds a new segment to the snake
    def extend(self):
        #Gets a hold of the last segment in the list
       self.add_segment(self.segments[-1].position())


    #Method that enables the movement of the snake
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    #Methods that enable the keyboard control of the snake
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

