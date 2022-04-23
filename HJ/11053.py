# 7. 가장 긴 증가하는 부분 수열(#11053)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

DP = [1 for _ in range(N)]

for idx, a in enumerate(A):
    for i in range(0, idx):
        if A[idx] > A[i]:
            DP[idx] = max(DP[idx], DP[i] + 1)
print(DP)
print(max(DP))
