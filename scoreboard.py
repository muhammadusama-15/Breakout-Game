from turtle import Turtle

#Creating a "ScoreBoard" class with "Turtle" as its superclass

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.shape("square")
        self.shapesize(stretch_len=40,stretch_wid=9)
        self.teleport(0,250)
        self.score = 0
        self.lives = 3
        self.highscore = ""
        
    def update(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  |  Lives: {self.lives}  |  Highscore: {self.highscore}", font=("Calibri",24,"normal"),align="center")

    def game_over(self):
        self.teleport(0,0)
        self.color("white")
        self.write(arg="Game Over!!!", font=("Calibri",24,"normal"),align="center")
