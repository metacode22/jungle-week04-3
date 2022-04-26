import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    junior = [list(map(int, input().split())) for _ in range(n)]
    junior.sort(key = lambda x:x[0])
    cnt = 0
    min_value = float('inf')
    
    for x, y in junior:
        if y < min_value:
            min_value = y
            
        if min_value < y:
            cnt += 1
    
    print(n - cnt)