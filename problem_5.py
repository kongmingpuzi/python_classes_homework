def judge(m):
    for i in range(2,int(m**0.5)):
        if m%i==0:
            return False
    return True
try:
    n=int(input('Please input the number. '))
except:
    print("Input error.")
start=n+1
count=0
while(count<3):
    if(judge(start)):
        print(start)
        count+=1    
    start+=1
