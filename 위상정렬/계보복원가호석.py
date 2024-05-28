#baekjoon 21276
from collections import deque
import sys

n = int(sys.stdin.readline())
p = list(map(str,sys.stdin.readline().split()))
p = sorted(p)

index = {p[i]:i for i in range(n)}
for i in range(n):
	index[p[i]] = i

m = int(input())
graph = [[] for _ in range(n)]
inbound = [0 for _ in range(n)]
for _ in range(m):
	i,j = map(str,sys.stdin.readline().split())
	graph[index[j]].append(index[i])
	inbound[index[i]] += 1

ans = []
q = deque()
for i in range(n):
	if inbound[i] == 0:
		ans.append(p[i])
		q.append(i)
print(len(ans))
print(*ans)

child = {key: [] for key in p}
while q:
	cur = q.popleft()
	for i in graph[cur]:
		inbound[i] -= 1
		if inbound[i] == 0:
			child[p[cur]].append(p[i])
			q.append(i)

for i in p:
	if child[i]:
		child[i] = sorted(child[i])
		print(f"{i} {len(child[i])} {' '.join(child[i])}")
	else:
		print(f"{i} {len(child[i])}")
