import sys

input=sys.stdin.readline

n =int(input()) # 11

time = [[0]*2 for i in range(n)]

for i in range(n):
    s,e = map(int,input().split())
    time[i][0] = s #i번째의 0인덱스들은 다 start값
    time[i][1] = e #i번째의 1인덱스들은 다 end값

# 1인덱스로 정렬하고 다음으론 0인덱스를 정렬하라는
time.sort(key=lambda x: (x[1], x[0]))

# print(time)

cnt = 1
endTime = time[0][1]
for i in range(1,n):
    if time[i][0]>= endTime:
        cnt+=1
        endTime = time[i][1]

print(cnt)

# 빨리 끝나는 회의 순서대로 정렬
# 만약 끝나는 시간이 같을 경우엔 빨리 시작하는 순서대로 정렬
# >> 즉 1. 끝나는 시간의 오름차순, 2. 시작하는 시간의 오름차순 으로 해주어야 함