#백준 4179
from collections import deque
import copy

board = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q_person = deque()
q_fire = deque()

n, m = map(int,input().split())
dist = [[0 for _ in range(m)]for _ in range(n)]
dist_fire = [[0 for _ in range(m)]for _ in range(n)]


for i in range(n):
	board.append(input())

for i in range(n):
	for j in range(m):
		if board[i][j] == 'J':
			q_person.append((i,j))
		elif board[i][j] == 'F':
			dist[i][j] = -1
			q_fire.append((i,j))
		elif board[i][j] == '#':
			dist[i][j] = -1
			dist_fire[i][j] = -1

# print(dist)
# print(dist_fire)
while q_fire:
	cur = q_fire.popleft()
	for dir in range(4):
		x = cur[0] + dx[dir]
		y = cur[1] + dy[dir]
		if x<0 or x>=n or y<0 or y>=m or board[x][y]== '#':
			continue
		if dist_fire[x][y] > 0 or board[x][y] =='F':
			continue
		dist_fire[x][y] = dist_fire[cur[0]][cur[1]] + 1
		q_fire.append((x,y))
# print(dist_fire)
while q_person:
	cur = q_person.popleft()
	for dir in range(4):
		x = cur[0] + dx[dir]
		y = cur[1] + dy[dir]
		if x<0 or x>=n or y<0 or y>=m:
			print(dist[cur[0]][cur[1]] + 1)
			exit()
		if dist[x][y]!=0:
			continue
		if dist_fire[x][y] > 0 and dist_fire[x][y] <= dist[cur[0]][cur[1]] + 1:
			continue
		dist[x][y] = dist[cur[0]][cur[1]] + 1
		q_person.append((x,y))

print("IMPOSSIBLE")