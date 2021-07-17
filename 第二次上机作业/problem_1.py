try:
    n=int(input('Please input an even number. '))
except:
    print("input error.")
for i in range(2,n+1):
    if i%2==0:
        print(('*'*i).center(n,' '))