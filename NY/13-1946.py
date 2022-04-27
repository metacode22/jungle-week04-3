import sys

input=sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    ziwon = []
    cnt=1 # 면접 순위가 1위인 사람은 무조건 채용이니까
    for j in range(n):
        ziwon.append(list(map(int,input().split())))
    
    ziwon.sort() #서류 기준 오름차순 정렬해주는 거고 
    compare = ziwon[0][1] # 서류는 오름차순으로 비교해줄 필요가 x / 오름차순된 서류의 면접을 비교

    print(ziwon)

    for k in range(1,n): #1인덱스부터 비교
        if compare > ziwon[k][1]: # compare보다 큰 인덱스부터 비교
            cnt+=1
            compare = ziwon[k][1] #값 갱신해주기

    print(cnt)