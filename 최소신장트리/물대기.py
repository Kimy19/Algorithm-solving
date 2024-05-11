#baekjoon 1368
import sys
from collections import deque
import heapq

n = int(input())
w = [0]
for _ in range(n):
    w.append(int(sys.stdin.readline()))


graph = [[] for _ in range(n+1)]
for i in range(1,n+1):
    row = list(map(int,sys.stdin.readline().split()))
    for j in range(len(row)):
        if j+1 == i:
            continue
        graph[i].append((row[j],j+1))
    for k in range(1,n+1):
        if i == k:
            continue
        graph[i].append((w[k],k))
       


included = [0 for _ in range(n+1)]
cnt = 0
ans = 0
min_n = 100001
start = 0
for i in range(1,n+1):
        if w[i] < min_n:
            min_n = w[i]
            start = i
arr = []
for edge in graph[start]:
    heapq.heappush(arr, edge)
included[start] = 1
cnt += 1
ans += w[start]
while cnt < n:
    cost, dest = heapq.heappop(arr)
    if included[dest]:
        continue
    included[dest] = 1
    ans += cost
    cnt += 1
    for i in graph[dest]:
        if included[i[1]]:
            continue
        heapq.heappush(arr,i)
print(ans)