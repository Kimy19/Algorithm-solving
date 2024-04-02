#백준 2206

from collections import deque

board = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int,input().split())
board = [list(map(int,input().strip())) for _ in range(n)]
visit = [[[0]*2 for _ in range(m)] for _ in range(n)]
visit[0][0][0] = 1

if n == 1 and m == 1 and board[0][0] == 1:
	print(-1)
	exit()

q = deque()
q.append((0,0,0))
flag = 0
while q:
	cur = q.popleft()
	if cur[0] == n-1 and cur[1] == m-1:
			print(visit[cur[0]][cur[1]][cur[2]])
			flag =1
			break
	for dir in range(4):
		x = cur[0] + dx[dir]
		y = cur[1] + dy[dir]
		z = cur[2]
		if x<0 or x>=n or y<0 or y>=m:
			continue
		if board[x][y] == 1 and z == 0:#최초 벽뚫기
			visit[x][y][1] = visit[cur[0]][cur[1]][0] +1
			visit[cur[0]][cur[1]][1] = 1
			q.append((x,y,1))
		elif board[x][y] == 0 and visit[x][y][z] == 0:
			visit[x][y][z] = visit[cur[0]][cur[1]][z] + 1
			q.append((x,y,z))
	if flag:
		break

if flag == 0:
	print(-1)