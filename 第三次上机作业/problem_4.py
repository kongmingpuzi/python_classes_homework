from random import *
for i in range(6):
    password=''
    for j in range(12):
        temp=0
        while(not ord('0')<=temp<=ord('9') and not ord('A')<=temp<=ord('Z') and not ord('a')<=temp<=ord('z')):
            temp=randint(30,122)
        password+=chr(temp)
    print(password)