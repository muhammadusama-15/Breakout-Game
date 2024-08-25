#Importing required libraries
from turtle import Screen
import random
from player import Player
from ball import Ball
from brick import Brick, Boundry
from scoreboard import ScoreBoard


#Creating a screen
screen = Screen()
screen.title("Breakout")
screen.screensize(canvheight=500, canvwidth=500,bg="white")

#Creating a boundry of game
boundry = Boundry()

#Creating a player at initial point
player = Player()

#Creating a scoreboard
scoreboard = ScoreBoard()
with open("highscore.txt") as file:
    data = file.read()
    highscore = int(data)
    scoreboard.highscore = highscore
scoreboard.update()

#Creating a wall of bricks
bricks = []
for ycor in range(200,150,-10):
    for xcor in range(-365,370,30):
        brick = Brick()
        brick.teleport(xcor,ycor)
        brick.showturtle()
        bricks.append(brick)

#Creating a ball 
ball = Ball()

#Starting screen listening
screen.listen()

#Game behaviour
game_is_on = True
while game_is_on:
    ball.speed(ball.velocity)
    ball.move()
    #Controlling player movement
    screen.onkeypress(key="Left", fun=player.move_left)
    screen.onkeypress(key="Right", fun=player.move_right)

    x1,y1 = ball.position() #Getting the ball's co-ordinates
    x2,y2 = player.position() #Getting the player's co-ordinates

    #Checking if the ball collided with the player
    if abs(x1-x2)<=60 and abs(y1-y2)<=20:
        ball.speed("fastest")
        ball.right(random.randint(90,270))
        ball.speed(ball.velocity)

    #Checking if the ball collided with the walls
    if x1>=350 or x1<=-360 or y1>=200:
        ball.speed("fastest")
        if x1<=-360:
            ball.right(random.randint(90,180))
        elif x1>350:
            ball.left(random.randint(90,180))
        elif y1>=200:
            ball.right(random.randint(90,270))    
        ball.speed(ball.velocity)  

    #Checking if the ball collided with a brick
    for brick in bricks:
        if ball.distance(brick) <= 15:
            bricks.remove(brick)
            brick.hideturtle()
            brick.teleport(-1000,-1000)

            #Changing the direction of ball as it hits a brick
            ball.speed("fastest")
            ball.right(random.randint(90,270))
            ball.speed(ball.velocity)
            scoreboard.score += 1 
            scoreboard.update() #Updating the scoreboard to help user keep track of their score

    #Checking if player missed the ball
    if y1 < y2:
        scoreboard.lives -= 1
        scoreboard.update()
        if scoreboard.lives > 0:
            ball.reset()

        else:
            if scoreboard.score > scoreboard.highscore:
                with open("highscore.txt", mode="w") as file:
                    file.write(f"{scoreboard.score}")
            scoreboard.game_over()

            game_is_on = False


screen.mainloop()