from turtle import *
import math
class Problem4:
    def __init__(self,pensize_,speed_) -> None:
        setup(1080,600,0,0)
        pensize(pensize_)
        speed(speed_)
        penup()
        seth(0)
        fd(300)
        seth(-72)
        pendown()
    def draw_5(self):
        pencolor('blue')
        for i in range(5):
            fd(100/math.sin(72/180*3.141592653))
            left(72)
        seth(180)
        penup()
        fd(100)
        pendown()
    def draw_4(self):
        pencolor('green')
        for i in range(4):
            fd(100)
            left(90)
        penup()
        fd(200)
        seth(-90)
        fd(100)
        seth(180)
        pendown()
    def draw_3(self):
        pencolor('red')
        for i in range(3):
            fd(100)
            right(120)
        penup()
        seth(180)
        fd(300)
        pendown()
    def write_(self,string):
        pencolor("black")
        write(string,font=("arial",20))
        done()
homework=Problem4(3,5)
homework.draw_5()
homework.draw_4()
homework.draw_3()
homework.write_("绘制完成！")