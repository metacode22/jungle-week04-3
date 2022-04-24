import sys

input=sys.stdin.readline

a = int(input())
b = list(map(int,input().split()))
# [10, 20, 10, 30, 20, 50]

dp = [1]*(a) #초기값이 1부터니까!
# [1, 1, 1, 1, 1, 1]

for i in range(a):
    for j in range(i):
        if b[j]<b[i]:
            dp[i] = max(dp[i],dp[j]+1) #1을 더해서 max값을 지금 dp[i]에 넣으며 길이 갱신

print(max(dp))