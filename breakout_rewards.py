from turtle import Turtle
import random

class Reward(Turtle):
    SHAPES = ["turtle", "circle", "square", "triangle"]
    COLORS = ["red", "white", "blue", "green"]

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.set_random_properties()
        self.goto(position)
        self.hideturtle()
        self.is_active = False 

    def set_random_properties(self):
        self.shape(random.choice(self.SHAPES))
        self.color(random.choice(self.COLORS))
        self.shapesize(stretch_wid=random.uniform(0.5, 0.9))

         

    def move(self):
        if self.is_active:  
            new_y = self.ycor() - 10  
            self.sety(new_y)


class PaddleBlock(Turtle):
    COLOR_OPTIONS = ["#0436A4", "#812121", "#006400"]

    def __init__(self, position, length):
        super().__init__()
        self.shape("square")
        self.color(random.choice(self.COLOR_OPTIONS))
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=1, stretch_len=length)


class RewardManager:
    def __init__(self):

        self.paddle_positions = {
            1: [(-850 + i * 190, 470) for i in range(10)],
            2: [(-850 + i * 170, 150) for i in range(11)],
            3: [(-850 + i * 150, 310) for i in range(12)],
            4: [(-850 + i * 130, 230) for i in range(14)],
            5: [(-850 + i * 110, 390) for i in range(16)]
        }
        #تخزين الطوب و الجوايز
        self.paddles = []
        self.rewards = []
        #استدعاء الدوال
        self.create_rwards()
        self.create_paddles()
      
    
    def create_paddles(self):
        for level, positiond in self.paddle_positions.items():
            self.length_ = 8 - level #8 - 5 = 3 اقل عرض  عندنا 3 يبقا الرقم الي المفروض نطرح منو لحد ما يدينا 3 اخر حاجة

            for position  in positiond:
                self.paddles.append(PaddleBlock(position=position, length=self.length_))

    
    def create_rwards(self):
        for level_, positions_rward in self.paddle_positions.items():

            self.numpers_gift = (random.randint(15, 30)) // len(self.paddle_positions)
            sampled_positions = random.sample(positions_rward, min(self.numpers_gift, len(positions_rward)))
            self.rewards.extend(sampled_positions)  

            for position_rwardq in sampled_positions:

                reward = Reward(position_rwardq)  
                self.paddles.append(reward)  


# Paddle width in the game with different values of stretch_len

# Maximum width
# max_width = 1900

# badding_lift=50
# badding_Right=50


# If stretch_len = 7:
#   paddles = 10 * 140 = 700
#   distance = 9 * 50 = 200
#   total = 1400 + 450 = 1850px

# If stretch_len = 6:
#   paddles =  11* 120 = 1320
#   distance = 10 * 50 = 500
#   total = 1320 + 500 = 1820px

# If stretch_len = 5:
#   paddles = 12 * 100 = 600
#   distance = 11 * 50 = 250
#   total = 1200 + 550 = 1750px

# If stretch_len = 4:
#   paddles = 14 * 80 = 560
#   distance = 13 * 50 = 300
#   total = 1120 + 650 = 1770px

# If stretch_len = 3:
#   paddles = 16 * 60 = 960
#   distance = 15 * 50 = 350
#   total = 960 + 750 = 1710px