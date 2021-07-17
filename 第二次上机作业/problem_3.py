dp=[0]*1000
def f(n):
    if(n==1 or i==0):
        return 1
    if(dp[n]==0):
        dp[n]=n*f(n-1)
        return dp[n]
    if(dp[n]!=0):
        return dp[n] 
#阶乘，dp数组保存运算过的阶乘结果，避免重复计算
e=0
for i in range(1000):
    temp=f(i)
    if temp>100_0000:
        break
    e+=1/temp
print(e)