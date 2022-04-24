import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
coins = list()
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)
cnt = 0

for coin in coins:
    cnt += k // coin
    k = k % coin
    
print(cnt)

