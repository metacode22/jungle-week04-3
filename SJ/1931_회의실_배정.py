# 끝나는 시간을 기준으로 정렬을 하면 된다.
# 회의 잡을 때 생각해보자. 앞의 것들이 언제 끝나는지 알아보곤 한다.
# 끝나는 시간을 기준으로 정렬하면 맨 처음 것은 가장 빨리 끝나는 회의가 된다.
# 그 다음부터 가장 빨리 끝나는 회의를 잡으면 될 것이다.
# 그 순간 순간 가장 빨리 끝나는 회의를 생각하게 되므로 그리디 알고리즘이라고 할 수 있다.
# 끝나는 시간을 기준으로 정렬했다면 이번에는 시작하는 시간을 기준으로 정렬한다.
# 시작하는 시간을 기준으로 정렬하는 단계를 하지 않아 틀렸었다.

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
meeting = list()
for _ in range(n):
    start, end = map(int, input().split())
    meeting.append([start, end])
res = list()
meeting.sort(key = lambda x:[x[1], x[0]])
res.append(meeting[0])

for i in range(1, n):
    if meeting[i][0] >= res[-1][1]:
        res.append(meeting[i])
        
print(len(res))

# 유용한 반례
# 15
# 1 4
# 7 7
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 7 7
# 7 7
# 7 7
# 2 13
# 12 14
# 끝나는 시간으로 정렬 후 시작하는 시간으로 정렬을 해두지 않는다면
# 1 4 이후에 5 7이 아니라 7 7이 들어가게 된다.


# 강의 풀이
# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# n = int(input())
# meeting = list()
# for _ in range(n):
#     start, end = map(int, input().split())
#     meeting.append([start, end])
# meeting.sort(key = lambda x:[x[1], x[0]])
# cnt = 0
# end = 0

# for s, e in meeting:
#     if s >= end:
#         end = e
#         cnt += 1
        
# print(cnt)