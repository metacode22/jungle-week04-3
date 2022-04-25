# 바텀업방식
# 한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력

import sys

input=sys.stdin.readline

n,k =map(int,input().split()) #4,7
item = [[0,0]] #표 0,0을 0처리
knapsack = [[0]*(k+1) for i in range(n+1)] #[0]이 8개 배치된 걸 5개 만들라고 

for i in range(n):
    item.append(list(map(int,input().split()))) #무게와 가치 item에 넣어줌
    # [[0, 0], [6, 13], [4, 8], [3, 6], [5, 12]]

for i in range(1,n+1):
    for j in range(1,k+1): #하나씩 다 탐색
        weight = item[i][0]
        value = item[i][1]

        if j<weight: #weight보다 작으면 위의 값을 그대로 가져옴
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(value+knapsack[i-1][j-weight],knapsack[i-1][j])
            # 차례대로 현재물건과 다른 물건으로 채우는 값 중 비교해서 큰 값을 저장해준다.
            # 이는 현재까지 물건들로 구성할 수 있는 가장 가치 높은 구성이다!

print(knapsack[n][k])