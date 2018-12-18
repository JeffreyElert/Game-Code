# Space invaders - BIM Creators
# Set up the screen
# Python 3.7.1 on Windows

import turtle
import winsound
import math
import random

# Set up the Screen
wn = turtle.Screen()
wn.bgcolor("Black")
wn.title("BIM Invaders")
wn.bgpic("space_invaders_background_bim.gif")

#Register the shapes
turtle.register_shape("player.gif")
turtle.register_shape("invader3.gif")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score = 0

#Draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("White")
score_pen.penup()
score_pen.setposition(-290, 270)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 22.5

#Choose number of enemies
number_of_enemies = 5
#Create an empty list of enemies
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
    #Create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("Red")
    enemy.shape("invader3.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 3

#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("Yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.4, 0.4)
bullet.hideturtle()

bulletspeed = 20

# Define bullet state
# ready - ready to fire
# fire- bullet is firing
bulletstate = "ready"

# Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = - 280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #Declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        winsound.PlaySound("laser", winsound.SND_ASYNC)
        bulletstate = "fire"
        #Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y + 10)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2)+ math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Main game loop
while True:

    for enemy in enemies:
        #Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        assert isinstance(x, object)
        enemy.setx(x)

        # Move the enemy back and down
        if enemy.xcor() > 280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1

        #Check for a collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            winsound.PlaySound("explosion", winsound.SND_ASYNC)
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #Update the score
            score += 10
            scorestring = "Score: %s" % score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            score_pen.hideturtle()


        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print ("Game Over")


    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bulletstate = "ready"
        bullet.hideturtle()




wn.mainloop()




