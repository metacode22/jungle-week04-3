import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
small_rocks = list(int(input()) for _ in range(m))
dp = [[float('inf')] * (int((2*n)**0.5) + 2) for _ in range(n + 1)]     # 등차수열의 합 공식 이용
dp[1][0] = 0

for rock in range(2, n + 1):
    if rock in small_rocks:
        continue
    
    for v in range(1, int((2*n)**0.5) + 1):
        # 내가 v만큼의 속도로 rock에 도착했다고 가정해서 모든 경우의 수를 구한다.
        dp[rock][v] = min(dp[rock - v][v + 1], dp[rock - v][v], dp[rock - v][v - 1]) + 1

res = min(dp[-1])

if res == float('inf'):
    print(-1)
else:
    print(res)
    
for i in dp:
    print(i)