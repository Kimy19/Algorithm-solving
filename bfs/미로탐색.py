#백준 2178
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int,input().split())
dist = [[0 for i in range(m)] for _ in range(n)]
# print(dist)
board = []

for i in range(n):
	board.append(list(map(int,input())))

# print(board)
q = deque()
q.append((0,0))
dist[0][0] = 1

while q:
	cur = q.popleft()
	for dir in range(4):
		x = cur[0] + dx[dir]
		y = cur[1] + dy[dir]
		if x<0 or x>=n or y<0 or y>=m or dist[x][y]>0 or board[x][y]!=1:
			continue
		q.append((x,y))
		dist[x][y] = dist[cur[0]][cur[1]] +1

print(dist[n-1][m-1])
