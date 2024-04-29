#백준 6593
from collections import deque

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

ans = []
while 1:

	l,r,c = map(int,input().split())
	if l == 0 and r == 0 and c == 0:
		break
	visit = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
	board = []
	q = deque()
	for i in range(l):
		temp = []
		for j in range(r):
			row = list(map(str,input().strip()))
			for k in range(len(row)):
				if row[k] == 'S':
					q.append((i,j,k))
					visit[i][j][k] = 1
			temp.append(row)
		input()
		board.append(temp)
	# for i in board:
	# 	for j in i:
	# 		print(j)
	# 	print()
	# print()
	flag = 0
	while q:
		cur = q.popleft()
		for dir in range(6):
			x = cur[1] + dx[dir]
			y = cur[2] + dy[dir]
			z = cur[0] + dz[dir]
			if x < 0 or x>=r or y<0 or y>=c or z<0 or z>=l:
				continue
			if board[z][x][y] == 'E':
				ans.append("Escaped in %d minute(s)." % (visit[cur[0]][cur[1]][cur[2]]))
				flag = 1
				break
			if visit[z][x][y] > 0:
				continue
			if board[z][x][y] == '#':
				continue
			visit[z][x][y] = visit[cur[0]][cur[1]][cur[2]]+1
			q.append((z,x,y))
		if flag ==1:
			break
	if flag != 1:
		ans.append("Trapped!")

for i in ans:
	print(i)
