#백준 5427
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,1,-1]

t = int(input())

ans = []
for _ in range(t):
	m, n = map(int,input().split())
	fire_dist = [[0 for _ in range(m)] for _ in range(n)]
	dist = [[0 for _ in range(m)] for _ in range(n)]
	board = []
	fire = []
	start = (0,0)
	for i in range(n):
		row = list(input())
		board.append(row)
		for j in range(len(row)):
			if row[j] == '*':
				fire.append((i,j))
				fire_dist[i][j] = 1
			elif row[j] == '@':
				start = (i,j)
				dist[i][j] =1

	# print(fire)


	q1 = deque()
	q1.extend(fire)
	q2 = deque()
	q2.append(start)
	while q1:
		cur = q1.popleft()
		for dir in range(4):
			x = cur[0] + dx[dir]
			y = cur[1] + dy[dir]
			if x<0 or x>=n or y<0 or y>=m:
				continue
			if fire_dist[x][y] or board[x][y] == '#':
				continue
			fire_dist[x][y] = fire_dist[cur[0]][cur[1]] + 1
			q1.append((x,y))

	# print(fire_dist)
	flag = 0
	while q2:
		if flag ==1:
			break
		cur = q2.popleft()
		for dir in range(4):
			x = cur[0] + dx[dir]
			y = cur[1] + dy[dir]
			if x<0 or x>=n or y<0 or y>=m:
				ans.append(dist[cur[0]][cur[1]])
				flag = 1
				break
			if dist[x][y] or board[x][y] == '#':
				continue
			if fire_dist[x][y]!= 0 and dist[cur[0]][cur[1]] + 1 >= fire_dist[x][y]:
				continue
			dist[x][y] = dist[cur[0]][cur[1]] + 1
			q2.append((x,y))
	# print(dist)
	if flag ==1:
		continue
	ans.append("IMPOSSIBLE")

for i in ans:
	print(i)