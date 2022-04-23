# 탑다운 방식

import sys

input = sys.stdin.readline

n= int(input())

# 저장값도 안 만들어줬고..
dp = [0]*100

def fibo(s):
    if s == 1 or s == 2:
        return 1
    if dp[s] != 0:
        return dp[s]
    dp[s] = fibo(s-1)+fibo(s-2)
    return dp[s]

print(fibo(n))