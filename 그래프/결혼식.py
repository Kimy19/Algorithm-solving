#백준 5567
from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
	i,j = map(int,input().split())
	graph[i].append(j)
	graph[j].append(i)

visit = [0 for _ in range(n+1)]
q = deque()
q.append(1)
visit[1] = 1
ans = 0
while q:
	cur = q.popleft()
	for i in graph[cur]:
		if visit[i]:
			continue
		if visit[cur] >=3:
			continue
		visit[i] = visit[cur] + 1
		q.append(i)
		ans += 1
print(visit)
print(ans)

	