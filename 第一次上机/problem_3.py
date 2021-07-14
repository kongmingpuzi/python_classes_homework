from turtle import *
class Problem3:
    def __init__(self,pensize_,speed_) -> None:
        setup(1080,1080,0,0)
        pensize(pensize_)
        speed(speed_)
    def draw(self,big_r,interval):
        for i in ['red','blue','green','yellow']:
            pencolor(i)
            for j in range(big_r,0,-interval):
                circle(j,360)
                right(float(90/(big_r/interval)))
        done()
homework=Problem3(1,15)
homework.draw(200,10)