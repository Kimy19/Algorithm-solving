#baekjoon 14940

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

n,m = map(int,input().split())
q = deque()
dist = [[-1 for _ in range(m)]for _ in range(n)]
board = []
for i in range(n):
	row = list(map(int,input().split()))
	for j in range(len(row)):
		if row[j] == 2:
			q.append((i,j))
			dist[i][j] = 0
		if row[j] == 0:
			dist[i][j] = 0
	board.append(row)

while q:
	cur = q.popleft()
	for i in range(4):
		x = cur[0] + dx[i]
		y = cur[1] + dy[i]
		if x<0 or x>=n or y<0 or y>=m:
			continue
		if board[x][y] == 0:
			continue
		if dist[x][y] >= 0:
			continue
		dist[x][y] = dist[cur[0]][cur[1]] +1
		q.append((x,y))
for i in dist:
	print(*i)