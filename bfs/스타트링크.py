#baekjoon 5014
from collections import deque

f,s,g,u,d = map(int,input().split())

visit = [0 for _ in range(f+1)]
dir = [u,-d]

if s == g:
	print(0)
	exit(0)
q = deque()
q.append(s)
visit[s] = 1
while q:
	cur = q.popleft()
	for i in dir:
		temp = cur + i
		if temp == g:
			print(visit[cur])
			exit(0)
		if temp < 1 or temp > f:
			continue
		if visit[temp]:
			continue
		visit[temp] = visit[cur] + 1
		q.append(temp)

print("use the stairs")
