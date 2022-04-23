from collections import defaultdict
import sys
input=sys.stdin.readline

n = int(input())

dp = defaultdict(int)

def tile(s):
    if s<=1:
        return s
    if dp[s]:
        return dp[s]
    dp[s] = tile(s-1)+tile(s-2)
    return dp[s]

print(tile(n)%15746)


# 이게 맞는진 모르겠는데, 일단 결과는 나와... 런타임에러가 난다