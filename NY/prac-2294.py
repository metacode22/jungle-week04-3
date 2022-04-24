import sys

input=sys.stdin.readline

n,k=map(int,input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

# 최소 코인 갯수를 저장할 dp배열을 만들어 10,001로 초기화해줌 10,000+1
dp = [10001]*(k+1)
dp[0] = 0

# 현재 값에서 가져온 코인 값을 빼주었을 때의 코인 사용 개수에
# 지금 코인 개수 하나를 더한 값과 이전 코인들로만 조합했을 때 
# 사용된 코인 개수를 비교하여 더 작은 값을 dp배열에 담는다.

for i in coin:
    for j in range(i,k+1):
        dp[j]=min(dp[j],dp[j-i]+1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])

