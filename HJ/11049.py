# 6. 행렬 곱셈 순서(#11049)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
matrices = []
for _ in range(N):
    a, b = map(int, input().split())
    matrices.append((a, b))
    
DP = [[0 for _ in range(N)] for _ in range(N)]

for i in range(1, N):
    for j in range(0, N - i):
        print(i, j, DP)
        if i == 1: # 바로 붙어 있는 칸, 그냥 단순 행렬 곱셈 연산수 계산
            DP[j][j + i] = matrices[j][0] * matrices[j][1] * matrices[j + 1][1]
            continue
        DP[j][j + i] = sys.maxsize
        for k in range(j, j + i):
            print('min' ,DP[j][j + i] ,' || ',DP[j][k],'+', DP[k + 1][j + i] ,'+', matrices[j][0] ,'*', matrices[k][1] ,'*', matrices[j + i][1],'=', DP[j][k] + DP[k + 1][j + i] + matrices[j][0] * matrices[k][1] * matrices[j + i][1])
            DP[j][j + i] = min(DP[j][j + i], DP[j][k] + DP[k + 1][j + i] + matrices[j][0] * matrices[k][1] * matrices[j + i][1])
            print(i, j, k, DP)
print(DP[0][N - 1])