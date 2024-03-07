from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]

q = deque()
board = []


n = int(input())
visit = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
	row = list(map(str,input()))
	board.append(row)

count = 0
for i in range(n):
	for j in range(n):
		q = deque()
		if visit[i][j] == 1:
			continue
		q.append((i,j))
		visit[i][j] = 1
		count += 1
		while q:
			cur = q.popleft()
			for dir in range(4):
				x = cur[0] + dx[dir]
				y = cur[1] + dy[dir]
				if(x<0 or x>=n or y<0 or y>=n):
					continue
				if(visit[x][y] or board[x][y]!= board[cur[0]][cur[1]]):
					continue
				visit[x][y] = 1
				q.append((x,y))

count2 = 0
visit = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
	for j in range(n):
		q = deque()
		if(board[i][j] == 'R'):
			board[i][j] = 'G'
		if visit[i][j] == 1:
			continue
		q.append((i,j))
		visit[i][j] = 1
		count2 += 1
		while q:
			cur = q.popleft()
			for dir in range(4):
				x = cur[0] + dx[dir]
				y = cur[1] + dy[dir]
				if(x<0 or x>=n or y<0 or y>=n):
					continue
				if(board[x][y] == 'R'):
					board[x][y] = 'G'
				if(visit[x][y] or board[x][y]!= board[cur[0]][cur[1]]):
					continue
				visit[x][y] = 1
				q.append((x,y))
print(count,count2)				
