import sys

input=sys.stdin.readline

n,k=map(int,input().split())
# 17, 4

# sum=n
# cnt=0
# for i in range(n):
#     sum-=1
#     # for j in range(sum):
#     div = (sum//k)
#     if div != 1:
#         continue
#     elif div ==1:
#         cnt+=1
#         break
# print(cnt)
# 처음에 내가 생각한 것. 틀림~^^

res=0

while 1:
    #n이 k로 나누어 떨어지는 수가 될 때까지 빼는 작업
    target = (n//k)*k
    res += (n-target)
    n = target
    #n이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복 탈출
    if n<k:
        break
    #k로 나누기
    res += 1
    n //= k

# 마지막으로 남은 수에 대해 1씩 빼기
res+=(n-1)
print(res)