from turtle import *
def init__():
    setup(800,800,200,200)
    penup()
    seth(0)
    pensize(5)
    pencolor('black')
    pendown()
def draw_side(distance):
    fd(distance)
    right(60)
init__()
for i in range(6):
    draw_side(100)
down()