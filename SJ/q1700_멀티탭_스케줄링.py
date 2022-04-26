# <처음 나의 풀이> : 뒤에 몇 개 남았는지 확인 후 가장 적게 등장하는 것을 빼는 방식. 틀림.
# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# n, k = map(int, input().split())
# order = list(map(int, input().split()))
# storage = [0] * n
# cnt = 0
    
# for i in range(n):
#     storage[i] = order[i]
# print(storage)

# for j in range(n, k):
#     if order[j] in storage:
#         continue
    
#     # else:
#     if order[j] not in storage:
#         min_value = sys.maxsize
#         min_idx = 0
#         for k in range(n):
#             tmp = order[j:].count(storage[k])
#             if tmp < min_value:
#                 min_value = tmp
#                 min_idx = k
        
#         storage[min_idx] = order[j]
#         print(storage)
#         cnt += 1
        
# print(cnt)


# 현재 멀티탭에 끼워져 있는 것들 중 가장 멀리 있는 것을 빼게 하는 방식이다.
# 만약 멀티탭에 끼워져 있지 않은 제품을 만난다면 가장 나중에 사용되는 멀티탭의 플러그를 뽑는 방식.

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
orders = list(map(int, input().split()))
multitab = [0] * n
cnt = 0
idx = 0
max_idx = 0
tmp = 0

for order in orders:
    if order in multitab:
        idx += 1
        continue
    
    elif 0 in multitab:
        multitab[multitab.index(0)] = order
        
    else:
        for x in multitab:
            if x not in orders[idx:]:
                tmp = x
                break
            
            elif orders[idx:].index(x) > max_idx:
                tmp = x
                max_idx = orders[idx:].index(x)
                
        multitab[multitab.index(tmp)] = order
        cnt += 1
        tmp = 0
        max_idx = 0
    idx += 1
    
print(cnt)

        
        