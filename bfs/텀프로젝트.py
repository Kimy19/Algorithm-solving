#baekjoon 9466
from collections import deque
import sys

t = int(sys.stdin.readline())
for _ in range(t):
	n = int(sys.stdin.readline())
	graph = [0]
	graph.extend(list(map(int,sys.stdin.readline().split())))
	q = deque()
	visit = [0 for _ in range(n+1)]
	count = 0
	for i in range(1,n+1):
		q.append(i)
		path = []
		while q:
			cur = q.popleft()
			if (visit[cur] == 1):
				break
			path.append(cur)
			visit[cur] = 1
			if visit[graph[cur]] == 1:
				if graph[cur] in path:
					index = path.index(graph[cur])
					count += len(path[index:])
				break
			q.append(graph[cur])
	print(n-count)
