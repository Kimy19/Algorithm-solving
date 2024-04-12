#백준 11724
from collections import deque
import sys

n,m = map(int,input().split())

graph = [[]for _ in range(n+1)]
for _ in range(m):
	i,j = map(int,sys.stdin.readline().split())
	graph[i].append(j)
	graph[j].append(i)

q = deque()
ans = 0
visit = [0 for _ in range(n+1)]

for i in range(1,n+1):
	if visit[i]:
		continue
	q.append(i)
	visit[i] = 1
	ans += 1
	while q:
		cur = q.popleft()
		for j in graph[cur]:
			if visit[j]:
				continue
			q.append(j)
			visit[j] = 1

print(ans)

