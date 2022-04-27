# 8. 외판원 순회(#2098)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
cost = []
for _ in range(N):
    cost.append(list(map(int, input().split())))

DP = [[sys.maxsize for _ in range(N)] for _ in range((1<<N) - 1)] # DP 테이블, R: 방문체크(2진수 -> 10진수), C: 현재 도시 번호

def TSP(visited, current):
    print(bin(visited), current)
    visited |= (1<<current) # 현재 위치 방문 체크

    if visited == ((1<<N) - 1): # 모든 도시 방문 했으면, 0b1111..11(1이 N개)
        # print('다 돌았다 ', bin(visited), bin((1<<N - 1)))
        if cost[current][0] > 0: # 출발도시로 갈 수 있는지 확인
            return cost[current][0] # 출발도시로 갈 수 있으면 이동비용 반환
        return sys.maxsize # 출발 도시로 갈 수 없으면 무한대 반환

    if DP[visited][current] != sys.maxsize:
        return DP[visited][current] # 이미 계산된 DP값 있으면 바로 반환

    for i in range(N): 
        if i != current and (visited & (1<<i)) == 0 and cost[current][i] > 0: # 현재 도시 아니고, 아직 방문 안했고, 갈 수 있는 도시면
            temp = TSP(visited, i) + cost[current][i]
            if DP[visited][current] > temp: # 이동 비용 더 작으면 갱신
                DP[visited][current] = temp # DP테이블 갱신

    return DP[visited][current]

result = TSP(0, 0)

if result == sys.maxsize:
    print(-1)
else:
    print(result)