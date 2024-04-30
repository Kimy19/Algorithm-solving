#[softeer] 함께하는 효도
import sys
import copy
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n, m = map(int,input().split())
q = deque()
board = []
for _ in range(n):
	board.append(list(map(int,input().split())))

start = []
visit = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
	i,j = map(int,input().split())
	start.append((i-1,j-1))
	visit[i-1][j-1] = 1
ans = 0
def get_harvest(cur,visit,point):
	global start,ans,n,m

	if cur == m:
		# print(point)
		ans = max(ans,point)
		return
	
	# print(cur, board[x][y])
	for i in range(64):
		x,y = start[cur]
		temp = point
		temp += board[x][y]
		temp_visit = [row[:] for row in visit]
		count = 3
		flag = 0
		while (count>0):
			dir = i%4
			i//=4
			count -= 1
			tx = x + dx[dir]
			ty = y + dy[dir]
			if tx<0 or tx>=n or ty<0 or ty>=n:
				flag = 1
				break
			if temp_visit[tx][ty] == 0:
				temp_visit[tx][ty] = 1
				temp += board[tx][ty]
			x = tx
			y = ty
		if flag:
			continue
		get_harvest(cur+1,temp_visit,temp)
		

get_harvest(0,visit,0)
print(ans)
