import sys

input=sys.stdin.readline

n, k = map(int,input().split())

coin=[]
for i in range(n):
    coin.append(int(input().strip())) #이거 처음에 split 쓰고 있었네;;

print(coin)

# A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수 → 이 조건 때문에 그리디 알고리즘을 사용할 수 있다

cnt = 0

# i가 9~0까지 = 가장 큰 동전부터 시작해서 몫을 카운트, 나머지 동전은 내림차순으로 반복
for i in reversed(range(n)):
    cnt += k//coin[i] #처음범위는 = 4200//9 , 카운트 값에 k를 동전으로 나눈 몫을 더함
    k = k%coin[i] # k는 동전으로 나눈 나머지로 계속 반복

print(cnt)