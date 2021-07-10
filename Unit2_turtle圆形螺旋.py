from turtle import *
class Homework:
    def __init__(self,input_r,input_interval):
        self.r=input_r
        self.interval=input_interval
        setup(800,800,200,200)
        penup()
        seth(0)
        pensize(1)
        pencolor('black')
        pendown()
    def draw(self):
        for i in range(0,self.r,self.interval):
            circle(i,360)
        seth(-180)
        for i in range(0,self.r,self.interval):
            circle(i,360)
        done()
big_r=200
interval=20
a=Homework(big_r,interval)
a.draw()