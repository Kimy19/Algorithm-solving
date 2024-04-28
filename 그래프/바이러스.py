#백준2606
from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
	i,j = map(int,input().split())
	graph[i].append(j)
	graph[j].append(i)

q = deque()
q.append(1)
ans = 0
visit = [0 for _ in range(n+1)]
visit[1] = 1
while q:
	cur = q.popleft()
	for i in graph[cur]:
		if visit[i]:
			continue
		q.append(i)
		visit[i] = 1
		ans += 1
		
print(ans)