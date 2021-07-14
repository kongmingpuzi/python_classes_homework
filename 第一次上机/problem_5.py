from turtle import *
class Problem5:
    def __init__(self,pensize_,speed_) -> None:
        setup(1080,1080,0,0)
        pensize(pensize_)
        speed(speed_)
    def draw(self,width):
        for i in range(3,11):
            for j in range(i):
                fd(width)
                left(180-180*(i-2)/i)
        done()
homework=Problem5(1,15)
homework.draw(100)