# 작은 문제부터 해결해서 큰 문제를 해결하는 것이 다이나믹 프로그래밍이다. 이게 근본이다.
# 작은 단위로도 만들 수 있으므로 다음 단위로 추가된다.
# 이 문제에서 주어진 금액을 세는 데에 드는 동전의 갯수는 중요하지 않다. 동전 종류 몇 개를 사용했는지가 중요하다.
# 만약 1, 5, 10 으로 12원을 만든다고 생각하자. 다이나믹 프로그래밍이므로 1원부터 빌드업해보자.
# 1, 5, 10으로 1원을 만드는 방법은 1원 짜리 1개를 써서 1가지이다.
# 2, 3, 4도 마찬가지이다. 1 ~ 4까지는 1원으로 1가지
# 5부터는 1원으로 5개, 5원으로 1개 총 2가지가 있다.
# 6에서 1원으로 6개, 5원으로 1개하고 1원으로 1개 총 2가지가 있다.
# 이렇듯 동전의 갯수는 전혀 상관없다. 동전 종류가 몇 개 사용되었는지에 따라 답이 나뉜다.
# 즉 1원만으로 만들 수 밖에 없으면 1가지, 5뭔으로 만들 수 있는 것은 1원으로도 혹은 섞어서 만들 수 있으므로 2가지, 10원으로 만들 수 있는 것은 1원 혹은 5원 혹은 10원으로 만들 수 있으므로 3가지이다.
# 주의할 점은, 0원을 만들 때이다. 1원으로 0원을 만드는 방법은 1가지, 5원으로 0원 혹은 10원으로 0원을 만드는 방법도 1가지라는 점을 기억하자.
# 5원으로 x원을 만들고 싶다면 5원으로 x-5원에다가 5원을 더하는 것과 같다.
# 즉 5원으로 x원을 만들 수 있는 가짓수는 x-5에다가 5원을 더하는 가짓수랑 같은 셈이다.
# 5원 밖에 없다고 치자. 이 때 15원을 만드는 가짓수는 10원을 만드는 가짓수와 같다. 동전의 갯수는 상관없다.

# <2차원 배열>
# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     coins = list(map(int, input().split()))
#     coins.insert(0, 0)
#     m = int(input())
    
#     dp = [[0] * (m + 1) for i in range(n + 1)]
#     for i in range(n + 1):
#         dp[i][0] = 1
        
#     for j in range(1, n + 1):
#         for k in range(1, m + 1):
#             dp[j][k] = dp[j - 1][k]
#             if k - coins[j] >= 0:
#                 dp[j][k] += dp[j][k - coins[j]]
    
#     for l in dp:
#         print(l)
    


# <1차원 배열>
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    
    dp = [0] * (m + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(1, m + 1):
            if i >= coin:
                dp[i] += dp[i - coin]
                
    print(dp)