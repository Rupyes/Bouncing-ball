import turtle
import random

# windows

window = turtle.Screen()
window.bgcolor('Black')
window.title("Bouncing Ball ")
window.tracer(0)


# create border

border_pen = turtle.Turtle()
border_pen.color("white")
border_pen.speed(0)
border_pen.penup()
border_pen.setposition(-350, -350)
border_pen.pendown()
border_pen.pensize(3)
for i in range(4):
    border_pen.forward(700)
    border_pen.lt(90)
border_pen.hideturtle()

# create ball

balls = []

for _ in range(130):
    balls.append(turtle.Turtle())

colors = ["red", "blue", "yellow", "green", "white", "purple"]
shapes = ["circle", "triangle", "square"]

for ball in balls:
    ball.shape(random.choice(shapes))
    ball.color(random.choice(colors))
    ball.speed(0)
    ball.penup()
    ball.goto(
        random.randint(-290, 290),
        random.randint(200, 350)
    )
    ball.dy = 0
    ball.dx = random.randint(-3, 3)
    ball.da = random.randint(-5, 5)

gravity = 0.1

while True:
    window.update()
    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)

        ball.setx(ball.xcor() + ball.dx)

        # check for wall
        if ball.xcor() > 335:
            ball.dx *= -1
            ball.da *= -1
        if ball.xcor() < -335:
            ball.dx *= -1
            ball.da *= -1

        # check for  a bounce
        if ball.ycor() < -335:
            ball.sety(-335)
            ball.dy *= -1
            ball.da *= -1
