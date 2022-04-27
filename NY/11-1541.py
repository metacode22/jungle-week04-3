import sys

input=sys.stdin.readline

# -를 기준으로 나누어서 괄호를 침 // 55-(50+40) 기준으로 이렇게
n = input().strip().split('-') # ['55', '50+40']

res= 0

for i in n[0].split('+'): 
    res+=int(i) #0번째 인덱스를 res에 담음 

for i in n[1:]: #1인데스 이후 >> 50+40
    for j in i.split('+'): #for문으로 뽑은 i(50+40)를 + 기준 나눔 >> 그럼 j[0]=50 j[1]=40
        res-=int(j) #하나씩 빼줘 -50 and -40

print(res)