from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())

class solution:
    dp = defaultdict(int)

    def fibo(self, n): #약속같은 거래
        if n<=1:
            return n
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fibo(n-1)+self.fibo(n-2)
        return self.dp[n]

sol = solution().fibo(n) # 클래스 호출할 때
print(sol)