# 11. 잃어버린 괄호(#1541)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

line = input().strip()

temp = ''
group = 0
flag = False
result = 0
for l in line:
    if l == '+':
        if flag:
            group += int(temp)
        else:
            result += int(temp)
        temp = ''
    elif l == '-':
        if flag:
            result -= (group + int(temp))
            group = 0
        else:
            result += int(temp)
        temp = ''
        flag = True
    else:
        temp += l
        
if group:
    group += int(temp)
    result -= group
    temp = ''
    group = 0

if temp:
    if flag:
        result -= int(temp)
    else:
        result += int(temp)
print(result)

