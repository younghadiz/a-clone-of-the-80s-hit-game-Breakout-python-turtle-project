import turtle
import random

# Set up the screen
win = turtle.Screen()
win.title("Breakout Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -240)
ball.dx = 0.2
ball.dy = 0.2

# Blocks
blocks = []

# Function to create a block
def create_block(x, y):
    block = turtle.Turtle()
    block.shape("square")
    block.color("blue")
    block.shapesize(stretch_wid=1, stretch_len=2)
    block.penup()
    block.goto(x, y)
    blocks.append(block)

# Create multiple rows of blocks
rows = 5
cols = 8
for row in range(rows):
    for col in range(cols):
        x = -230 + col * 60
        y = 200 - row * 30
        create_block(x, y)

# Move paddle
def paddle_right():
    x = paddle.xcor()
    if x < 250:
        paddle.setx(x + 20)

def paddle_left():
    x = paddle.xcor()
    if x > -250:
        paddle.setx(x - 20)

# Keyboard bindings
win.listen()
win.onkey(paddle_left, "Left")
win.onkey(paddle_right, "Right")

# Main game loop
while True:
    win.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border collision
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        print("Game Over!")
        break  # End game if ball hits the bottom

    # Paddle collision
    if (ball.ycor() > -240 and ball.ycor() < -230) and \
       (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1

    # Block collision
    for block in blocks:
        if block.distance(ball) < 30:
            ball.dy *= -1
            block.hideturtle()
            blocks.remove(block)
            break

    # Win condition
    if not blocks:
        print("You win!")
        break
