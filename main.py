"""
Leila Lopez Marks
11/10/2020
Snake Game
"""
import turtle

# Create screen
sc = turtle.Screen()
sc.title("Snake game")
sc.bgcolor("#FFFFFF")
sc.setup(width=1000, height=600)
turtle.done()


# Functions to move paddle vertically
def up_move():
    y = snake_head.ycor()
    y += 20
    snake_head.sety(y)


def down_move():
    y = snake_head.ycor()
    y += 20
    snake_head.sety(y)


def left_move():
    x = snake_head.ycor()
    x += 20
    snake_head.sety(x)



def right_move():
    x = snake_head.ycor()
    x += 20
    snake_head.sety(x)

def food_circles():
    eat_food = turtle.Turtle()
    eat_food.speed(40)
    eat_food.shape("circle")
    eat_food.color("blue")
    eat_food.penup()
    eat_food.goto(0, 0)
    eat_food.dx = 5
    eat_food.dy = -5

def Initialize_score():
    snake_head = 0

def Displays_score():
    sketch = turtle.Turtle()
    sketch.speed(0)
    sketch.color("blue")
    sketch.penup()
    sketch.hideturtle()
    sketch.goto(0, 260)
    sketch.write("Left_player : 0    Right_player: 0",
             align="center", font=("Courier", 24, "normal"))

def Keyboard_bindings():
    sc.listen()
    sc.onkeypress(up_move, "w")
    sc.onkeypress(down_move, "s")
    sc.onkeypress(left_move, "a")
    sc.onkeypress(right_move, "d")

def snake_head():
    snake_head = turtle.Turtle()
    snake_head.speed(0)
    snake_head.shape("square")
    snake_head.color("black")
    snake_head.shapesize(stretch_wid=1, stretch_len=1)
    snake_head.penup()
    snake_head.goto(200, 200)

while True:
    sc.update()

    eat_food.setx(eat_food.xcor() + eat_food.dx)
    eat_food.sety(eat_food.ycor() + eat_food.dy)

def check_borders():
    if eat_food.ycor() > 280:
        eat_food.sety(280)
        eat_food.dy *= -1

    if eat_food.ycor() < -280:
        eat_food.sety(-280)
        eat_food.dy *= -1

    if eat_food.xcor() > 500:
        eat_food.goto(0, 0)
        eat_food.dy *= -1
        snake_head += 1
        sketch.clear()
        sketch.write("snake_head : {}".format(
        snake_head), align="center",
        font=("Courier", 24, "normal"))




