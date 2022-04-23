import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

arr = list(input().split('-'))
res = 0

for i in arr[0].split('+'):
    res += int(i)
    
for j in arr[1:]:
    for k in j.split('+'):
        res -= int(k)
    
print(res)