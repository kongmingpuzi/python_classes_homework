def solve(m,n):
    if m==0 or n==0:
        return max(m,n)
    else:
        if m>n:
            return solve(m%n,n)
        else:
            return solve(n%m,m)
try:
    a=int(input('Please input the first number. '))
    b=int(input('Please input the second number. '))
except:
    print("Input error.")
print(str(a)+' and '+str(b)+' is '+str(solve(a,b)))