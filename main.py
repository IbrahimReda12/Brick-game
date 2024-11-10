from turtle import Screen, Turtle
from ball import Ball
from paddles import Paddels
from breakout_rewards import RewardManager, Reward
import time

screen_ = Screen()
screen_.bgcolor("black")
screen_.setup(width=800, height=600)
screen_.tracer(0)

Instructions = Turtle()
Instructions.hideturtle()
Instructions.penup()
Instructions.color("white")
Instructions.goto(-380, 100)
Instructions.write(f"Turtle Loses Lives 2\nThe circle increases the life by 2\nThe square increases the life by 1\nThe triangle increases the life by 1 \n انتظر 5 ثواني , Wait 5 seconds", align="left", font=("Arial", 24, "normal"))


screen_.update()

time.sleep(4.9)
screen_.clear()




# إعداد الشاشة
screen = Screen()
screen.bgcolor("#ADD8E6")
screen.setup(width=2000, height=1000)
screen.tracer(0)

# إنشاء كائنات
paddels_ = Paddels()
ball = Ball()
blocks_manager = RewardManager()
blocks = blocks_manager.paddles 


lives = 3  
lives_display = Turtle()  
lives_display.hideturtle()
lives_display.color("black")
lives_display.penup()
lives_display.goto(-900, 400)  
lives_display.write(f"Lives: {lives}", align="left", font=("Arial", 24, "normal"))


# حركة الأسهم
screen.listen()
screen.onkeypress(paddels_.run_Left, "Left")
screen.onkeypress(paddels_.run_Right, "Right")

# تشغيل اللعبة
time.sleep(0.2)
game_on = True
while game_on:
    
    ball.move()
    screen.update()
    time.sleep(0.01)

    # ارتداد الكرة عند التصادم
    if ball.xcor() >= 980 or ball.xcor() <= -980:
        ball.bounce_x()

    # حدود السقف
    if ball.ycor() >= 480:
        ball.bounce_y()

    # حدود الأرض
    if ball.ycor() <= -500:
        ball.goto(0, 0)
        ball.bounce_y()
        
        # تقليل عدد الحية
        lives -= 1
        lives_display.clear()
        lives_display.write(f"Lives: {lives}", align="left", font=("Arial", 24, "normal"))

        # انهاء اللعبة
        if lives <= 0:
            lives_display.clear()
            lives_display.goto(0, 0)
            lives_display.write("Game Over", align="center", font=("Arial", 36, "normal"))
            game_on = False
            break

    # الاصطدام مع المضرب
    if ball.distance(paddels_) <= 60 and ball.ycor() <= -460:
        ball.bounce_y()

    # تكرار على الطوب لإخفائه عند الاصطدام
    for block in blocks[:]:
       
        if len(blocks[:])<=0:
            break
        if ball.distance(block) < 50:
            ball.bounce_y()

            if isinstance(block, Reward):#  لو الطوبة مكافأة ==True
                block.is_active = True  

            else:
                block.hideturtle()
                blocks.remove(block)

    # تحريك الجوائز
    for block in blocks:
        if isinstance(block, Reward):
            block.move() 
            block.showturtle()
        if block.distance(paddels_) < 50 and block.shape()=="turtle":
            block.hideturtle()
            blocks.remove(block)  

            lives -= 2
            lives_display.clear()
            lives_display.write(f"Lives: {lives}", align="left", font=("Arial", 24, "normal"))


        elif block.distance(paddels_) < 50 and block.shape() == "circle":
          
            block.hideturtle()
            blocks.remove(block) 
        
            lives += 2
            lives_display.clear()
            lives_display.write(f"Lives: {lives}", align="left", font=("Arial", 24, "normal"))

            
        elif block.distance(paddels_) < 50 and block.shape() == "square":

            block.hideturtle()
            blocks.remove(block) 
        
            lives += 1
            lives_display.clear()
            lives_display.write(f"Lives: {lives}", align="left", font=("Arial", 24, "normal"))

          
        elif block.distance(paddels_) < 50 and block.shape() == "triangle":
            block.hideturtle()
            blocks.remove(block) 
        
            lives += 1
            lives_display.clear()
            lives_display.write(f"Lives: {lives}", align="left", font=("Arial", 24, "normal"))

            
        elif block.ycor() <= -500:
            block.hideturtle()
            blocks.remove(block)

screen.exitonclick()

    
