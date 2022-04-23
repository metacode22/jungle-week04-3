# 2. 01타일(#1904)
import sys

N = int(sys.stdin.readline())
result = [0 for _ in range(1000001)]
result[0] = 1
result[1] = 1

for i in range(2, N + 1):
    result[i] = (result[i - 1] + result[i - 2]) % 15746

print(result[N])