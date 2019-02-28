import turtle
from Player import Player
from Border import Border

#Set up the screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")
window.setup(600, 600, None, None)

isRunning = True

player = Player(turtle)
border = Border(turtle)

turtle.done()