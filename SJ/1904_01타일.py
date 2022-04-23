import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
d = [0] * (n + 1)       # 왜 d = [0] * (n + 1)로 하면 100% 에서 IndexError가 뜰까?
d[1] = 1                # : n이 1이라면 d[2]는 없는 원소이기 때문에 에러가 발생한다.
d[2] = 2

for i in range(3, n + 1):
    d[i] = (d[i - 1] + d[i - 2]) % 15746        # print할 때 % 15746해주면 메모리 초과가 난다.
                                                # 이는 배열에는 엄청 큰 수가 담겨 있기 떄문이다.
print(d[n])                                     # 따라서 저장될 때 마다 미리미리 나누어줘야 큰 수가 들어가지 않는다.