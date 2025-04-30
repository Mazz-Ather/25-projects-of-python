import os   
import turtle 
import sys

wn = turtle.Screen()
wn.title("Pong by Mazz Ather")
wn.bgcolor("black")
wn.setup(width=800, height=600) 
wn.tracer(0)

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball 
paddle_ball = turtle.Turtle()
paddle_ball.speed(0)
paddle_ball.shape("square")
paddle_ball.color("white")
paddle_ball.penup()
paddle_ball.goto(0, 0)
paddle_ball.dx = 0.3  # Reduced from 2 to 0.3
paddle_ball.dy = 0.3  # Reduced from 2 to 0.3

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#score
score_a = 0
score_b = 0


#function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# def b 
# Fix paddle B movement functions
def paddle_b_up():
    y = paddle_b.ycor()  # Changed from paddle_a to paddle_b
    y += 20
    paddle_b.sety(y)    # Changed from paddle_a to paddle_b

def paddle_b_down():
    y = paddle_b.ycor()  # Changed from paddle_a to paddle_b
    y -= 20
    paddle_b.sety(y)    # Changed from paddle_a to paddle_b

#keyword binding
wn.listen()
wn.onkeypress(paddle_a_up, "w") #when the user presses w, call the function paddle_a_up
wn.onkeypress(paddle_a_down, "s") #when the user presses s, call the function paddle_a_down
wn.onkeypress(paddle_b_up, "Up") #when the user presses w, call the function paddle_a_up
wn.onkeypress(paddle_b_down, "Down") #when the user presses s, call the function paddle_a_down


# Add this function for clean exit
def on_close():
    global running
    running = False
    wn.bye()
    sys.exit()

# Register the close handler
wn.onkey(on_close, "Escape")  # Press Escape to exit
wn.listen()

# Add running variable
running = True

# Modify the main game loop
while running:
    try:
        wn.update()
        
        # move the ball
        paddle_ball.setx(paddle_ball.xcor() + paddle_ball.dx)
        paddle_ball.sety(paddle_ball.ycor() + paddle_ball.dy)
        
        #border checking
        if paddle_ball.ycor() > 290:
            paddle_ball.sety(290)
            paddle_ball.dy *= -1
            os.system("afplay bounce.wav&")
        
        if paddle_ball.ycor() < -290:
            paddle_ball.sety(-290)
            paddle_ball.dy *= -1
    
        if paddle_ball.xcor() > 390:
            paddle_ball.goto(0, 0)
            paddle_ball.dx *= -1
            score_a += 1    
            pen.clear() #clear the scor
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        
        if paddle_ball.xcor() < -390:
            paddle_ball.goto(0, 0)
            paddle_ball.dx *= -1
            score_b += 1    
            pen.clear() #clear the score    
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    
    
        # paddle and ball collision
        if paddle_ball.xcor() > 340 and paddle_ball.xcor() < 350 and (paddle_ball.ycor() < paddle_b.ycor() + 40 and paddle_ball.ycor() > paddle_b.ycor() -40):
            paddle_ball.setx(340)
            paddle_ball.dx *= -1
            os.system("afplay bounce.wav&")
        
        if paddle_ball.xcor() < -340 and paddle_ball.xcor() > -350 and (paddle_ball.ycor() < paddle_a.ycor() + 40 and paddle_ball.ycor() > paddle_a.ycor() -40):
            paddle_ball.setx(-340)
            paddle_ball.dx *= -1
            os.system("afplay bounce.wav&")
    except:
        break