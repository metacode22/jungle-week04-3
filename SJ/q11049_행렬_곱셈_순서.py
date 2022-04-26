# Bottom-Up
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for diagonal in range(1, n):                # 대각선을 따라서 이동한다. (0, 0), (1, 1), (2, 2)는 초기화 해둔 0 그대로 이므로 돌 필요가 없으니 1부터 시작한다.
    for i in range(0, n - diagonal):        # 행의 범위    
        j = i + diagonal                    # 열의 범위
        
        if diagonal == 1:                   # 행과 열의 차이가 1밖에 나지 않는다면 바로 그 둘을 곱한 것이 최소 연산 횟수가 된다. 어차피 그 2개 밖에 없으니 2개 안에서 최소 연산 횟수를 구하는 방법은 단 1가지, 그대로 2개를 곱하는 것이다.
            dp[i][j] = data[i][0] * data[j][0] * data[j][1]
            continue
        
        dp[i][j] = sys.maxsize              # 초반 최솟값 갱신을 위한 장치
        for k in range(i, j):               # 대각선을 기준으로 왼쪽 아래는 돌지 않게 된다.
            # 우리가 원하는 답이 0에서 3까지, 즉 dp[0][3]이라고 한다면 A0 A1 A2 A3라는 행렬이 있을 때 A0(A1A2A3), (A0A1)(A2A3), (A0A1A2)A3로 나눌 수 있다.(k를 나눌 수 있다)
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + data[i][0] * data[k + 1][0] * data[j][1])

print(dp[0][n - 1])



# Top-Down, 재귀
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
row = list()
col = list()
for _ in range(n):
    r, c = map(int, input().split())
    row.append(r)
    col.append(c)
dp = [[0] * n for _ in range(n)]

    
def DFS(x, y):
    if dp[x][y] != 0:
        return dp[x][y]
    
    if x - y == 0:
        return 0
        
    dp[x][y] = sys.maxsize
    for k in range(x, y):
        dp[x][y] = min(dp[x][y], DFS(x, k) + DFS(k + 1, y) + row[x] * row[k + 1] * col[y])
    return dp[x][y]
    
DFS(0, n - 1)
print(dp[0][n - 1])

