#baekjoon 1240
from collections import deque
import sys

n,m = map(int,sys.stdin.readline().split())
cost = [[0 for _ in range(n+1)]for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    i,j,k = map(int,sys.stdin.readline().split())
    cost[i][j] = k
    cost[j][i] = k
    graph[i].append(j)
    graph[j].append(i)

ans = []
for _ in range(m):
    s,e = map(int,sys.stdin.readline().split())
    q = deque()
    q.append(s)
    dist = [0 for _ in range(n+1)]
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if dist[i]:
                continue
            dist[i] = dist[cur] + cost[cur][i]
            q.append(i)
    ans.append(dist[e])

for i in ans:
    print(i)