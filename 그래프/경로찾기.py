#백준 11403
from collections import deque

n = int(input())
graph = []
for i in range(n):
	graph.append(list(map(int,input().split())))

def find(st,en):
	global graph
	
	visit = [0 for _ in range(n+1)]
	q = deque()
	q.append(st)
	while q:
		cur = q.popleft()
		for i in range(n):
			if graph[cur][i] == 0:
				continue
			if visit[i]:
				continue
			if i == en:
				return 1
			q.append(i)
			visit[i] = 1
	return 0

ans = [[] for _ in range(n)]
for i in range(n):
	for j in range(n):
		ans[i].append(find(i,j))

for row in ans:
	print(*row)