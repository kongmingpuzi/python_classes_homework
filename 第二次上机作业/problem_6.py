from turtle import *
def draw(n,length):
    for i in range(n):
        fd(length)
        left(180-(n-2)*180/n)
speed(5)
for i in range(3,11):
    draw(i,100)
done()