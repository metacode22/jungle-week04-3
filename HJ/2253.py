# 9. 점프(#2253)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

small = {}
for _ in range(M):
    small[int(input())] = 1
DP = [[sys.maxsize for _ in range(int((2 * N) ** 0.5) + 2)] for _ in range(N + 1)]
DP[1][0] = 0
for step in range(2, N + 1):
    if step in small:
        continue
    for speed in range(1, int((2 * step) ** 0.5) + 1):
        DP[step][speed] = min(DP[step - speed][speed - 1], DP[step - speed][speed], DP[step - speed][speed + 1]) + 1

for idx, dp in enumerate(DP):
    arr = []
    for d in dp:
        if d >= sys.maxsize:
            arr.append('-')
        else:
            arr.append(int(d))
    print(*arr)

answer = min(DP[N])
if answer == sys.maxsize:
    print(-1)
else:
    print(answer)

