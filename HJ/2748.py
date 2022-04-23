# 1. 피보나치 수2(#2748)
import sys

N = int(sys.stdin.readline())
piboMemo = { 0:0, 1:1 }

def pibo(n):
    if n in piboMemo:
        return piboMemo[n]
    result = pibo(n - 1) + pibo(n - 2)
    piboMemo[n] = result
    return result

print(pibo(N))