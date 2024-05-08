#baekjoon 2252
import sys
from collections import deque

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
for _ in range(m):
	i,j = map(int,sys.stdin.readline().split())
	graph[i].append(j)
	indegree[j] += 1
q = deque()
for i in range(1,n+1):
	if indegree[i] == 0:
		q.append(i)

ans = []
while q:
	cur = q.popleft()
	ans.append(cur)
	for i in graph[cur]:
		indegree[i] -= 1
		if indegree[i] == 0:
			q.append(i)
print(*ans)