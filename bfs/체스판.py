#softeer 부트캠프 코테
from collections import deque

dx = [2,1,1,2,-2,-1,-1,-2]
dy = [1,2,-2,-1,1,2,-2,-1]

n,m = map(int,input().split())
visit = [[-1 for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0,0))
visit[0][0] = 0
count = 0
while q:
    cur = q.popleft()
    for i in range(8):
        x = cur[0] + dx[i]
        y = cur[1] + dy[i]
        if (x<0 or x>=n or y<0 or y>=m):
            continue
        if visit[x][y] > -1:
            continue
        visit[x][y] = visit[cur[0]][cur[1]] + 1
        count += 1
        q.append((x,y))

ans = -1
for i in range(len(visit)):
    ans = max(ans,max(visit[i]))

if (count == m*n):
    print(f"T{ans}")
else:
    print(f"F{ans}")

