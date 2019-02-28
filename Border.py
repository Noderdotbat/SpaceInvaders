class Border:

    scoretext = None

    def __init__(self, turtle):
        #Creates the border
        border = turtle.Turtle()
        border.speed(0)
        border.color("white")
        border.penup()
        border.setposition(-300, -300)
        border.pendown()
        border.pensize(3)
        border.hideturtle()
        for size in range(4):
            border.fd(600)
            border.lt(90)

        #Creates the score text
        scoretext = turtle.Turtle()
        scoretext.color("white")
        scoretext.speed(0)
        scoretext.penup()
        scoretext.setposition(-290, 280)
        scoretext.write("Score: ", False, align="Left", font=("Arial", 14, "normal"))
        scoretext.hideturtle()
        self.scoretext = scoretext

    def updateScore(self, score):
        self.scoretext = "Score: " + score