from collections import deque
import sys

n,m = map(int,input().split())

board = [[0 for _ in range(n+1)]for _ in range(n+1)]
for _ in range(m):
	i,j = map(int,sys.stdin.readline().split())
	board[i][j] = 1
	board[j][i] = 1

ans = 0
q = deque()
visit = [0 for _ in range(n+1)]
for i in range(1,n+1):
	if visit[i]:
		continue
	q.append(i)
	visit[i] = 1
	ans += 1
	while q:
		cur = q.popleft()
		for j in range(1,n+1):
			if board[cur][j] == 0 or visit[j]:
				continue
			q.append(j)
			visit[j] = 1

print(ans)

	

