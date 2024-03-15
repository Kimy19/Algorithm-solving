#백준 토마토 7569
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
dz = [1,-1]

m,n,h = map(int,input().split())
board = []
tomato =[]
q =deque()
visit = [[[0 for _ in range(m)] for _ in range(n)]for _ in range(h)]

for i in range(h):
    temp = []
    for j in range(n):
        row = list(map(int,input().split()))
        for k in range(len(row)):
            if row[k] == 1:
                q.append((j,k,i))#행,열,높
            if row[k] == -1:
                visit[i][j][k] = -1
        temp.append(row)
    board.append(temp)

def OOB(x,y,z):
    global n,m,h
    if x<0 or x>=n or y<0 or y>=m or z<0 or z>=h:
        return True
    return False

ans = 0
while q:
    cur = q.popleft()
    x,y,z = cur
    if visit[z][x][y] <= 0:
        visit[z][x][y] = 1
    for dir in range(6):
        if dir<4:
            tx = x+dx[dir]
            ty = y+dy[dir]
            tz = z
        else:
            tx = x
            ty = y
            tz = z+dz[dir%2]
        if OOB(tx,ty,tz):
            continue
        if visit[tz][tx][ty] or board[tz][tx][ty] !=0:
            continue
        visit[tz][tx][ty] = visit[z][x][y] + 1
        q.append((tx,ty,tz))
        ans = max(ans,visit[tz][tx][ty])

for i in range(h):
    for j in range(n):
        for k in range(m):
            if 0 == visit[i][j][k]:
                print(-1)
                exit()
# print(visit)
if ans>0:
    print(ans-1)
else:
    print(ans)
