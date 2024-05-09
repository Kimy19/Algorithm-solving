#baekjoon 2623
from collections import deque
import sys

n, m = map(int,input().split())
indegree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
	row = list(map(int,sys.stdin.readline().split()))
	if len(row) > 2:
		for i in range(1, len(row)-1):
			graph[row[i]].append(row[i+1])
			indegree[row[i+1]] += 1

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

if len(ans) == n:
	for i in ans:
		print(i)
else:
	print(0)