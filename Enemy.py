class Enemy:
    enemy = None
    EnemySpeed = 2

    def __init__(self, turtle):
        enemy = turtle.Turtle()
        enemy.color("red")
        enemy.shape("circle")
        enemy.penup()
        enemy.speed(0)
        enemy.setposition(0, 0)

        self.enemy = enemy
        self.moveEnemy()

    def moveEnemy(self):
        enemy = self.enemy
        while (enemy != None):
            x = enemy.xcor() + self.EnemySpeed
            enemy.setx(x)

            if (enemy.xcor() > 280):
                y = enemy.ycor() - 40
                enemy.sety(y)
                self.EnemySpeed = -self.EnemySpeed

            if(enemy.xcor() < -280):
                y = enemy.ycor() - 40
                enemy.sety(y)
                self.EnemySpeed = -self.EnemySpeed