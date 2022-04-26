# 6. 행렬 곱셈 순서(#11049)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
R = []
C = []
for _ in range(N):
    a, b = map(int, input().split())
    R.append(a) # 행
    C.append(b) # 열
    
DP = [[0 for _ in range(N)] for _ in range(N)]

def calc_matrix(x, y):
    if DP[x][y]:
        return DP[x][y]
    if y - x <= 0:
        return 0
    mm = sys.maxsize
    for k in range(x, y):
        print(x, y, k)
        mm = min(mm, calc_matrix(x, k) + calc_matrix(k + 1, y) + R[x] * C[k] * C[y])
    DP[x][y] = mm
    return DP[x][y]

print(calc_matrix(0, N - 1))
