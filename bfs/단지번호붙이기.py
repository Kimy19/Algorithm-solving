from collections import deque

board = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())
visit = [[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
	board.append(list(map(int,input())))

count = 0
size_list = []
for i in range(n):
	for j in range(n):
		q= deque()
		if board[i][j]!=1 or visit[i][j]:
			continue
		visit[i][j] =1
		q.append((i,j))
		count += 1
		size = 1
		while q:
			cur = q.popleft()
			for dir in range(4):
				x = cur[0] +dx[dir]
				y = cur[1] +dy[dir]
				if x<0 or x>=n or y<0 or y>=n:
					continue
				if board[x][y] != 1 or visit[x][y] ==1:
					continue
				visit[x][y] = 1
				q.append((x,y))
				size += 1
		size_list.append(size)

size_list = sorted(size_list)
print(count)
for i in range(len(size_list)):
	print(size_list[i])