import sys
input=sys.stdin.readline

n=int(input())

dp = [0]*10000001

dp[1]=1
dp[2]=2

for i in range(3,n+1):
    dp[i] = (dp[i-1]+dp[i-2])%15746

print(dp[n])
# 결과값에서 mod하면 안되고 반복할 때마다 mod 해줘야함 = 그래야지 메모리 초과가 발생하지 않음