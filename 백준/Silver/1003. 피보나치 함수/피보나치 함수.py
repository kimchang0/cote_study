import sys
input = sys.stdin.readline

def fibo(n):
    if n <= 1:
        return n
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

t = int(input().strip())
for _ in range(t):
    fibo_arr = []
    
    n = int(input().strip())
    
    for i in range(n + 1):
        fibo_arr.append(fibo(i))
        
    if n == 0:
        print(fibo_arr.count(0), 0)
        
    elif n == 1:
        print(0, fibo_arr.count(1))
        
    else:
        print(fibo_arr[-2], fibo_arr[-1])