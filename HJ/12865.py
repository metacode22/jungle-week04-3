# 5. 아주 평범한 배낭(#12865)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
items = []
arr = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))
# items.sort()
print(items)

maxVal = 0
for i, item in enumerate(items):
    for j in range(1, K + 1):
        if item[0] <= j:
            arr[i + 1][j] = max(arr[i][j], arr[i][j - item[0]] + item[1])
            if maxVal < arr[i + 1][j]:
                maxVal = arr[i + 1][j]
        else:
            arr[i + 1][j] = arr[i][j]
    print(item, i, arr)
print(maxVal)