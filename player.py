from turtle import Turtle

#Creating a "Player" class with "Turtle" as its superclass

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.penup()
        self.speed("fastest")
        self.goto(0,-300)
        self.showturtle()

    def move_left(self):
        x_cor = self.xcor()
        if x_cor>=-320:
            self.setx(x_cor-10)

    def move_right(self):
        x_cor = self.xcor()
        if x_cor<=319:
            self.setx(x_cor+10)