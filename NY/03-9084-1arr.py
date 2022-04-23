import sys

input=sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    coin = list(map(int,input().split()))
    m = int(input())

    dp = [0]*(m+1) #범위가 1000이면 +1만큼의 배열만 생성하게
    dp[0] = 1 # 1로 초기화해주기

    for j in coin:
        for k in range(1,m+1):
            if k >= j:
                dp[k] += dp[k-j] #dp[k-j]한 값을 dp[k]에 저장해주면서 반복
    print(dp[m])

# 1차원 dp table 코드
# 이게 시복도 메모리도 더 낮음~ (좋다는거)