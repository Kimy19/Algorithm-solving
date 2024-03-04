#백준 1926
from collections import deque 

board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


n, m = map(int, input().split())
vis = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
		board.append(list(map(int, input().split())))

count = 0
sizelist = [0]

for row in range(n):
	for col in range(m):
		if vis[row][col]:
			continue
		vis[row][col] = 1
		if board[row][col] != 1:
			continue
		q = deque()
		q.append((row,col))
		count += 1
		size = 1
		while q:
			cur = q.popleft()
			for i in range(4):
				x = cur[0] + dx[i]
				y = cur[1] + dy[i]
				if x<0 or x>=n or y<0 or y>=m or vis[x][y] or board[x][y]!= 1:
					continue
				vis[x][y] = 1
				q.append((x,y))
				size += 1
		sizelist.append(size)
print(count)
print(max(sizelist))