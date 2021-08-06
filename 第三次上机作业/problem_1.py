try:
    n=int(input('Please input the length. '))
except:
    print("Input error.")
for i in range(n):
    for j in range(n):
        print('+'+'*'*3,end='')
    print('+')
    for j in range(n+1):
        print('|',end='   ')
    print()
for j in range(n):
    print('+'+'*'*3,end='')
print('+')