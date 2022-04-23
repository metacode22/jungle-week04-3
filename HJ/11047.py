# 10. 동전 0(#11047)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

maxVal = coins[0]
maxIdx = 0
for idx, coin in enumerate(coins):
    if coin <= K:
        maxVal = coin
        maxIdx = idx
    else:
        break

total = maxVal
count = 1

while total != K:
    if total < K:
        n = (K - total) // maxVal # K를 넘지 않으려면 몇개까지 채울 수 있는지
        total += maxVal * (n + 1) # n+1개만큼 곱해서 더해줌, 여기서 n개만큼만 곱해서 더해주면 계속 total < K이기 때문에 무한루프에 빠져버림
        count += (n + 1) # n+1개만큼 더해줌
    elif total > K:
        count -= 1
        total -= maxVal
        maxIdx -= 1
        maxVal = coins[maxIdx]
print(count)