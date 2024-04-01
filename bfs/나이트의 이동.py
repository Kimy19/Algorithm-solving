from collections import deque

board = []
dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]


t = int(input())

for _ in range(t):
	n = int(input())
	board = [[0 for _ in range(n)] for _ in range(n)]
	start = tuple(map(int,input().split()))
	end = tuple(map(int,input().split()))
	q = deque()
	q.append(start)
	while q:
		flag = 0
		cur = q.popleft()
		for dir in range(8):
			x = cur[0]+dx[dir]
			y = cur[1]+dy[dir]
			if x == end[0] and y == end[1]:
				print(board[cur[0]][cur[1]] + 1)
				flag = 1
				break
			if x<0 or x>=n or y<0 or y>=n:
				continue
			if board[x][y] != 0:
				continue
			board[x][y] = board[cur[0]][cur[1]] + 1
		if flag:
			break
	