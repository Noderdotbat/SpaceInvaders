class Player:

    player = None
    PlayerSpeed = 15

    def __init__(self, turtle):

        player = turtle.Turtle()
        player.color("blue")
        player.shape("circle")
        player.penup()
        player.speed(0)
        player.setposition(0, -250)
        self.player = player

        turtle.listen()
        turtle.onkey(self.moveRight, "Right")
        turtle.onkey(self.moveLeft, "Left")
        
    def moveRight(self):
        player = self.player
        x = self.player.xcor() + self.PlayerSpeed
        player.setx(x)
    def moveLeft(self):
        player = self.player
        x = self.player.xcor() - self.PlayerSpeed
        player.setx(x)