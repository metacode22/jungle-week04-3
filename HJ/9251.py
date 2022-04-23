# 4. LCS(#9251) 최장 공통 부분 수열
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

text1 = input().strip()
text2 = input().strip()

LCS = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
maxLen = 0
for idx1, t1 in enumerate(text1):
    for idx2, t2 in enumerate(text2):
        if t1 == t2:
            LCS[idx1][idx2] = LCS[idx1 - 1][idx2 - 1] + 1
        else:
            LCS[idx1][idx2] = max(LCS[idx1][idx2 - 1], LCS[idx1 - 1][idx2])
        if LCS[idx1][idx2] > maxLen:
            maxLen = LCS[idx1][idx2]
print(LCS)
print(maxLen)
