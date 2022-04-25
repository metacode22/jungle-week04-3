import sys

input=sys.stdin.readline

n = int(input())

dp = [[0]*(n) for i in range(n)] #3*3

# print(dp)

mul = [list(map(int,input().split())) for i in range(n)]
# [[5, 3], [3, 2], [2, 6]]

# print(mul)

for i in range(1,n): #i번째 대각선
    for j in range(n-i): #i번째 대각선의 j번째 열
        dp[j][j+i] = 2**31
        for k in range(j,j+i): #이전 단계 부분문제에서 현재 문제를 푸는 k가지 방법 비교
            dp[j][j+i] = min(dp[j][j+i], dp[j][k]+dp[k+1][j+i] + mul[j][0]*mul[k][1]*mul[j+i][1])

print(dp[0][n-1])