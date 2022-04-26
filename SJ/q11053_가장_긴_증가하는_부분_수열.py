# 각 항을 마지막으로 생각했을 때 얼마나 긴 증가수열을 만들 수 있는지 생각한다.
# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# n = int(input())
# seq = list(map(int, input().split()))
# seq.insert(0, 0)
# dp = [0] * (n + 1)
# dp[1] = 1

# for i in range(1, n + 1):
#     max_value = 0
    
#     for j in range(i - 1, -1, -1):
#         if seq[i] > seq[j]:
#             if dp[j] > max_value:
#                 max_value = dp[j]
                
#     dp[i] = max_value + 1
    
# print(max(dp))



# 구글링 풀이
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(dp)
