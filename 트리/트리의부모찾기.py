#백준 11725
from collections import deque
import sys

n = int(input())
graph =[[] for _ in range(n+1)]
for _ in range(n-1):
	i,j = map(int,sys.stdin.readline().split())
	graph[i].append(j)
	graph[j].append(i)

p = [0 for _ in range(n+1)]
q = deque()
q.append(1)
while q:
	cur = q.popleft()
	for i in graph[cur]:
		if i == p[cur]:
			continue
		q.append(i)
		p[i] = cur

for i in range(2,n+1):
	print(p[i])