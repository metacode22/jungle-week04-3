# 12. 회의실 배정(#1931)
import sys
from heapq import heappush, heappop
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
schedules = []
for _ in range(N):
    s, e = map(int, input().split())
    schedules.append((s, e))
schedules.sort()

count = 0
maxHeap = []
for schedule in schedules:
    start, end = schedule
    if not maxHeap:
        heappush(maxHeap, (-end, (start, end)))
        continue

    while maxHeap and maxHeap[0][1][1] > end:
        heappop(maxHeap)
    
    if not maxHeap or maxHeap[0][1][1] <= start:
        # print(maxHeap, 'push ', start, end)
        heappush(maxHeap, (-end, (start, end)))

print(len(maxHeap))