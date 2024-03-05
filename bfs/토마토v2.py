#백준 7576
from collections import deque

board = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque()

m, n = map(int,input().split())
dist = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
	board.append(list(map(int,input().split())))


for i in range(n):
	for j in range(m):
		if board[i][j] == 1:
			q.append((i,j))
		elif board[i][j] == 0:
			dist[i][j] = -1


while q:
	cur = q.popleft()
	for i in range(4):
		x = cur[0] + dx[i]
		y = cur[1] + dy[i]
		if(x<0 or x>=n or y<0 or y>=m or board[x][y]!= 0):
			continue
		if dist[x][y] > 0:
			continue
		q.append((x,y))
		dist[x][y] = dist[cur[0]][cur[1]] + 1

ans = 0
for i in range(n):
	for j in range(m):
		if dist[i][j] == -1 :
			print(-1)
			exit()
		ans = max(ans,dist[i][j])

print(ans)