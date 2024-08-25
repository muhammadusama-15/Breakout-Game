from turtle import Turtle
import random
import time

#Creating a "Ball" class with "Turtle" as its superclass

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("goldenrod2")
        self.shape("circle")
        self.shapesize(stretch_len=0.75,stretch_wid=0.75)
        self.setheading(random.randint(250,300))
        self.velocity = 5

        self.reset() 

    def move(self):
        self.forward(10)

    def reset(self):
        self.teleport(0,0)
        time.sleep(1)
