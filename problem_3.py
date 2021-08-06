from random import *
try:
    n=int(input('Please input the length of passwprds. '))
except:
    print("Input error.")
seed(15)
for i in range(3):
    password=''
    for j in range(n):
        password+=str(randint(0,9))
    print(password)