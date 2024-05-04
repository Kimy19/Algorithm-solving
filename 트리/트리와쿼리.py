#baekjoon 15681
import sys
from collections import deque
sys.setrecursionlimit(10**6)

n,r,q = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    s,e = map(int,sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

visit = [0 for _ in range(n+1)]

def dfs(cur):
    visit[cur] = 1
    for i in graph[cur]:
        if visit[i] == 0:
            visit[cur] += dfs(i)
    return visit[cur]
dfs(r)

for _ in range(q):
    node = int(sys.stdin.readline())
    print(visit[node])
    

