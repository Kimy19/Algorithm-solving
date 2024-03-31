#백준2583
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
m,n,k = map(int,input().split())

board = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            board[i][j] = -1

# print(board)

ans = []
for i in range(n):
    for j in range(m):
        if board[i][j]:
            continue
        board[i][j] = 1
        q = deque()
        q.append((i,j))
        size = 1
        while q:
            cur = q.popleft()
            for dir in range(4):
                x = cur[0] + dx[dir]
                y = cur[1] + dy[dir]
                if x<0 or x>=n or y<0 or y>=m:
                    continue
                if board[x][y] != 0:
                    continue
                board[x][y] = board[cur[0]][cur[1]]+1
                q.append((x,y))
                size+=1
        ans.append(size)

ans = sorted(ans)
print(len(ans))
print(*ans)

