#백준 1012
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,1,-1]
q= deque()


t = int(input())
for _ in range(t):
    board = [[0 for _ in range(50)] for _ in range(50)]
    visit = [[0 for _ in range(50)] for _ in range(50)]
    start = []
    m, n, k = map(int, input().split())
    for i in range(k):
        y, x = map(int,input().split())
        board[x][y] = 1
        start.append((x,y))

    count = 0
    for j in range(len(start)):

        first = start[j]
        if visit[first[0]][first[1]] == 1:
            continue
        q.append(start[j])
        visit[first[0]][first[1]] = 1
        count += 1
        while q:
            cur = q.popleft()
            for i in range(4):
                x = cur[0] + dx[i]
                y = cur[1] + dy[i]
                if x<0 or x>=n or y<0 or y>=m:
                    continue
                if board[x][y] == 0 or visit[x][y] ==1:
                    continue
                visit[x][y] = 1
                q.append((x,y))

    print(count)