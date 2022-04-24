from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())

dp = defaultdict(int)

def fibo(n):
    if n<=1:
        return n
    if dp[n]:
        return dp[n]
    dp[n] = fibo(n-1)+fibo(n-2)
    return dp[n]

print(fibo(n))