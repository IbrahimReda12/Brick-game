from turtle import Turtle

class Paddels(Turtle):
    def __init__(self):
        super().__init__()  
        # شكل المضرب
        self.color_ = ["blue", "white", "green", "braen"]
        self.shape("square")
        self.color("black")
        self.shapesize (stretch_wid=1,stretch_len=6)
        self.penup()
        self.goto(0, -475)
        self.move_distance = 50 

    def run_Left(self):
        if self.xcor() > -930:  
            self.setx(self.xcor() - self.move_distance)

    def run_Right(self):
        if self.xcor() < 930: 
            self.setx(self.xcor() + self.move_distance)
            
 
