# split으로 나누려는 문자가 없는 경우 그대로 반환한다.
# 전혀 감이 잡히지 않아 구글링하여 풀이를 참고하였다.
# 나눠서 받아야 하는 입력값이 있을 때 그저 input().split()만 생각했는데 이렇게도 나눌 수 있다는 걸 알게 되었다.
# 이 문제를 푸는 방법은, -이후의 수들을 모두 빼버리는 것이다.
# 40+20-20+10000+90+10 이렇게 되었다고 가정하면 -를 만난 뒤의 수를 모두 빼버리면 된다.
# 40+20-20-10-90+80 이렇게 되었어도 90과 80을 괄호로 묶는다고 치면 결국 -뒤의 수들은 모두 빼면 되는 셈이다.
# +로만 이루어진 예제도 통과할 수 있도록 로직을 구현해야 한다.
# 그렇다면 처음 for문에서 모든 계산을 끝내고 다음 for문은 돌지 않을 것이다.
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

arr = input().split('-')

res = 0
for i in arr[0].split('+'):
    res += int(i)
    
for i in arr[1:]:
    for j in i.split('+'):
        res -= int(j)
        
print(res)



# <몇 일 후, 나의 풀이>
# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# datum = input().split('-')
# res = 0

# for j in datum[0].split('+'):
#     res += int(j)

# for i in range(1, len(datum)):
#     tmps = datum[i].split('+')
    
#     for tmp in tmps:
#         res -= int(tmp)    
        
# print(res)
    