#ملف الجوايز و الكورة
from turtle import Turtle

#كورة التكسير
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.8)
        self.x_move = 12
        self.y_move = 12

    # الانتقال باستخدام x_move و y_move
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # لعكس الاتجاه بعد الاصطدام
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

