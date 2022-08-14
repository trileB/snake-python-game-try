import turtle
import time
import random

delay=0.1
score=0
high_score=0

wn=turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width=700,height=700)
wn.tracer(0)

head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food 
food=turtle.Turtle()
food.speed()
food.shape("circle")
food.penup()
food.goto(0,100)

segments=[]
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,310)
pen.write("Score:0 High score: 0", align="center")
def go_up():
    if head.direction!="down":
        head.direction="up"
   
def go_down():
    if head.direction!="up":
        head.direction="down"
        
def go_left():
    if head.direction!="right":
        head.direction="left"  

def go_right():
    if head.direction!="left":
        head.direction="right"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
        
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)


wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")


while True:
    wn.update()
    if head.xcor()>340 or head.xcor()<-340 or head.ycor()>310 or head.ycor()<-310:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        
        for segments in segments:
            segments.goto(1000,1000)
            
        segments.clear()
        
        score=0
        
        delay=0.1
        
        pen.clear()
        
        pen.write("score() high score()".format(score,high_score),align="center",font=("courier",24))
        
        if head.distance(food)<20:
            x=random.randint(-330,330)  
            y=random.randint(-330,290)
            food.goto(x,y)
        
            new_segment=turtle.Turtle()
            new_segmmnt=turtle.speed(0)
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            segments.append(new_segment)
        
            delay-=0.001
            score+=10
        
            if score>high_score:
                high_Score=score
            
            pen.clear()     
            pen.write("score() high score()".format(score,high_score),align="center",font=("courier",24))

    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
        
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments(0).goto(x,y)
        
    move()
    
    for segments in segments:
        if segments.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
       
        for segment in segments:
            segment.goto(1000,1000)
            
        segment.clear()
        
        score=(0)
        
        delay=0.1
        
        pen.clear()
        
        pen.write("score() high score()".format(score,high_score),align="center",font=("courier",24))
    
    time.sleep(delay)

wn.mainloop()