import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

s1 = list(input().rstrip())
s2 = list(input().rstrip())
s1.insert(0, '-')
s2.insert(0, '-')
# print(s1)
# print(s2)
board = [[0] * (len(s2)) for _ in range(len(s1))]

for i in range(len(s1)):
    for j in range(len(s2)):
        if i == 0 or j == 0:
            board[i][j] = 0
            
        elif s1[i] == s2[j]:
            board[i][j] = board[i - 1][j - 1] + 1
        
        else:
            board[i][j] = max(board[i - 1][j], board[i][j - 1])

for k in board:
    print(k)

print(board[len(s1) - 1][len(s2) - 1])