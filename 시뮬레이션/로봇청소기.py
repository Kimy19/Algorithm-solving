#baekjoon 14503
import sys

dx = [-1,0,1,0]
dy = [0,1,0,-1]
back_x = [1,0,-1,0]
back_y = [0,-1,0,1]

n,m = map(int,input().split())
r,c,d = map(int,input().split())
board = []
for _ in range(n):
	row = list(map(int,input().split()))
	board.append(row)
count = 0
visit = [[0 for _ in range(m)] for _ in range(n)]
x = r
y = c
while True:
	if board[x][y] == 1:
		print(count)
		exit()
	if visit[x][y] == 0:
		count += 1
		visit[x][y] = 1
	flag = 0
	dir = d
	for _ in range(4):
		dir = (dir + 3) % 4
		tx = x + dx[dir]
		ty = y + dy[dir]
		if board[tx][ty] != 1 and visit[tx][ty] != 1:
			x = tx
			y = ty
			flag = 1
			d = dir
			break
	if flag:
		continue
	x = x + back_x[d]
	y = y + back_y[d]
	# print(x,y,d,count)

# print(count)
