from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

#Class that controls the scoreboard based off the amount off food the snake eats
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    #Method that displays the score on the screen
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    #Method that displays "GAME OVER" once the user loses the game
    def game_over(self):
        self.goto(0 , 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    #Method that increase the score as the snake eats more food
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

