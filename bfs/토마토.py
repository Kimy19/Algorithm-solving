#백준 7576
from collections import deque

board = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
start = []
flag = 0

m, n = map(int,input().split())

for i in range(n):
	board.append(list(map(int,input().split())))
	if 0 in board[i]:
		flag = 1
	start.extend([(i,j) for j,num in enumerate(board[i]) if num == 1])

# print(board)
# print(start)
# print(start[0][0])

if flag != 1: #모두 익어있을때
	print(0)
	exit()

q = deque()
q.extend(start)
size = len(q)
new_size = 0
count = 0

while q:
	if(size == 0):
		if new_size == 0:
			break
		size = new_size
		new_size = 0
		count+=1
	size -= 1
	cur = q.popleft()
	for dir in range(4):
		x = cur[0] + dx[dir]
		y = cur[1] + dy[dir]
		if x<0 or x>=n or y<0 or y>=m or board[x][y]!= 0:
			continue
		q.append((x,y))
		board[x][y] = 1
		new_size+=1

for i in range(n):
	for j in range(m):
		if board[i][j] == 0: #모두 익히지 못한경우
			print(-1)
			exit()
print(count)