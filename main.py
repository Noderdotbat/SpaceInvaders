import turtle
import math
import sys
#Create objects(Player, Border, Score Counter, Enemy)
from Player import Player
from Border import Border
from Enemy import Enemy

#Set up the screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")
window.setup(600, 600, None, None)

isRunning = True

player = Player(turtle)
border = Border(turtle)
enemy = Enemy(turtle)

def isCollision(obj1, obj2):
    distance = math.sqrt(math.pow(obj1.xcor()-obj2.xcor(),2) + math.pow(obj1.ycor()-obj2.ycor(), 2))
    if(distance < 15):
        return(True)
    else:
        return(False)

while(isRunning):
    if(isCollision(player, enemy)):
        print("Game Over")
        sys.exist("Game Over!")
turtle.done()