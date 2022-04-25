# <1차원 배열 풀이> : 2차원 배열 풀이와 같은 셈이다.
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * (k + 1)
for _ in range(n):
    w, v = map(int, input().split())
    for i in range(k, w - 1, -1):       # 역방향
        dp[i] = max(dp[i], dp[i - w] + v)
        
print(dp[-1])



# <2차원 배열 풀이>
