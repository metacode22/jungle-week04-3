d = [0] * 1001

d[1] = 1
d[2] = 1
n = 1000

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
    print(d[i], i)
    
print(d[n])