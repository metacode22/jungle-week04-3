# 13. 신입사원(#1946)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    people = []
    for n in range(N):
        p, i = map(int, input().split())
        people.append((p, i))
    people.sort()
    checked = [False for _ in range(N)]
    maxVal = people[0][1]
    for i in range(N):
        if not checked[i] and maxVal < people[i][1]:
            checked[i] = True
        elif maxVal > people[i][1]:
            maxVal = people[i][1]
    print(checked.count(False))