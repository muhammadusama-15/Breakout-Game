from turtle import Turtle
import random

colors = ['red','green','blue','indianred','firebrick','ForestGreen','SteelBlue1']

#Creating a "Ball" class with "Turtle" as its superclass

class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.color("grey80",random.choice(colors))
        self.shapesize(stretch_wid=0.5,stretch_len=1.5)

#Creating a "Boundry" class with "Turtle" as its superclass
class Boundry(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=40,stretch_wid=31)
        self.color("black")
        self.teleport(0,-100)
        
