# 백준 2468
from collections import deque


dx = [1,-1,0,0]
dy = [0,0,1,-1]

n = int(input())
board = []
max_h = 1
for _ in range(n):
    row = list(map(int,input().split()))
    max_h = max(max_h, max(row))
    board.append(row)

ans = 0
for h in range(max_h+1):
    #높이 확인
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] <= h:
                temp[i][j] = -1
    #탐색
    visit = [[0 for _ in range(n)] for _ in range(n)]
    q = deque()
    num = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 1 or temp[i][j] == -1:
                continue
            q.append((i,j))
            visit[i][j] = 1
            num += 1
            while q:
                cur = q.popleft()
                for dir in range(4):
                    x = cur[0] + dx[dir]
                    y = cur[1] + dy[dir]
                    if x<0 or x>=n or y<0 or y>=n:
                        continue
                    if visit[x][y] or temp[x][y] == -1:
                        continue
                    q.append((x,y))
                    visit[x][y] = 1
    ans = max(ans,num)

print(ans)