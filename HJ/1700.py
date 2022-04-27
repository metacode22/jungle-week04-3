# 14. 멀티탭 스케줄링(#1700)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
uselist = list(map(int, input().split()))

multitab = []
totalUse = [0 for _ in range(K + 1)]

for i in range(1, K + 1):
    totalUse[i] = uselist.count(i)
# print(totalUse)
count = 0
for idx, use in enumerate(uselist):
    # print(f'--------{use}----------')
    if len(multitab) < N:
        if use not in multitab:
            multitab.append(use)
        totalUse[use] -= 1
    else:
        if use in multitab:
            totalUse[use] -= 1
            continue
        nextArr = []
        flag = True
        for idx2, item in enumerate(multitab):
            if totalUse[item] == 0:
                # print(item, '이제 안씀1', idx2, multitab, use)
                multitab[idx2] = use
                totalUse[use] -= 1
                count += 1
                flag = False
                break
            else:
                nextIdx = uselist[idx:].index(item)
                # print('find index ', uselist[idx:], item, nextIdx)
                if nextIdx == -1:
                    # print(item, '이제 안씀2', idx2, multitab, use)
                    multitab[idx2] = use
                    totalUse[use] -= 1
                    count += 1
                    flag = False
                    break
                # print('next idx ', nextIdx, item)
                nextArr.append((nextIdx, idx2, item))
            # print('nextArr', nextArr)
        if flag:
            next, now, item = max(nextArr)
            # print(nextArr, next, now, item, uselist[idx:])
            # print(item, '젤 나중에 등장', now, multitab, use)
            multitab[now] = use
            totalUse[use] -= 1
            count += 1

    # print(multitab, count)
print(count)