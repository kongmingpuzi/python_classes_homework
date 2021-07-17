def judge(n):
    if n%400==0:
        return True
    if n%4==0 and n%100!=0:
        return True
    return False
print('2000~3000之间所有的非闰年:')
count=0
for i in range(2000,3001):
    if not judge(i):
        print(i,end='\t')
        count+=1
        if(count%15==0):
            print()