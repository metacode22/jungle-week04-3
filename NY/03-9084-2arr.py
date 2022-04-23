import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    coin = list(map(int,input().split()))
    coin.insert(0,0) # 리스트 coin[0]에 0을 삽입
    m = int(input())

    # for i in range(n+1):
    #     dp=[[0]*(m+1)] #list ? -> 물어본다는게..

    dp = [[0] * (m+1) for i in range(n+1)]

    for i in range(n+1): #3번째까지의 인덱스[0]은 다 '1가지수'니까
        dp[i][0] = 1

    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = dp[i-1][j] 
            if j-coin[i] >= 0: 
                dp[i][j] += dp[i][j-coin[i]]
    print(dp[n][m])

# 2차원 dp table 코드