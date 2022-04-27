import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
orders = list(map(int, input().split()))
multitab = [0] * n
cnt = 0
idx = 0

for order in orders:
    if order in multitab:
        pass
    
    elif 0 in multitab:
        multitab[multitab.index(0)] = order
        
    else:
        max_idx = 0
        tmp = 0
        for tab in multitab:
            if tab not in orders[idx:]:
                tmp = tab
                break
            
            else:
                if orders[idx:].index(tab) > max_idx:
                    max_idx = orders[idx:].index(tab)
                    tmp = tab
            
        multitab[multitab.index(tmp)] = order        
        cnt += 1
        
    idx += 1
    
print(cnt)


