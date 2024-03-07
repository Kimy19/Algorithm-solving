from collections import deque

n, k = map(int,input().split())
time = [-1 for i in range(200000)]
q= deque()
q.append(n)
time[n] = 0
if n == k:
    print(0)
    exit()
while q:
    cur = q.popleft()
    for i in range(3):
        if i == 0:
            x = cur + 1
        elif i == 1:
            x = cur - 1
        else:
            x = cur * 2
        if x == k:
            print(time[cur]+1)
            exit()
        if x<0 or x>=200000 or time[x]>-1:
            continue
        time[x] = time[cur] + 1
        q.append(x)

