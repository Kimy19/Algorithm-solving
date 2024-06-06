import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int,sys.stdin.readline().split())
board = []
wall = deque()
for i in range(n):
	row = list(map(int,sys.stdin.readline().strip()))
	for j in range(len(row)):
		if row[j] == 1:
			wall.append((i,j))
	board.append(row)

area = [[0 for _ in range(m)] for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
q = deque()
idx = 1
area_size = [0]
for i in range(n):
	for j in range(m):
		if board[i][j] == 1 or visit[i][j] == 1:
			continue
		q.append((i,j))
		visit[i][j] = 1
		area[i][j] = idx
		size = 1
		while q:
			cur = q.popleft()
			for dir in range(4):
				x = cur[0] + dx[dir]
				y = cur[1] + dy[dir]
				if x < 0 or x>=n or y<0 or y>=m:
					continue
				if board[x][y] == 1 or visit[x][y] == 1:
					continue
				visit[x][y] = 1
				q.append((x,y))
				area[x][y] = idx
				size += 1
		idx += 1
		area_size.append(size)

ans = [[0 for _ in range(m)] for _ in range(n)]

while wall:
	cur = wall.popleft()
	size = 1
	added = []
	for i in range(4):
		x = cur[0] + dx[i]
		y = cur[1] + dy[i]
		if x < 0 or x>=n or y<0 or y>=m:
			continue
		if board[x][y] == 1:
			continue
		if area[x][y] != 0:
			if area[x][y] not in added:
				size += area_size[area[x][y]]
				added.append(area[x][y])
	ans[cur[0]][cur[1]] = size%10

for row in ans:
	for i in row:
		print(i,end = '')
	print()
