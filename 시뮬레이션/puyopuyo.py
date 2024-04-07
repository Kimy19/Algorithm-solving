#백준 11559
from collections import deque
import copy

dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = 0
board = []
#input
for i in range(12):
    row = list(map(str,input().strip()))
    board.append(row)

#bfs
def pop():
    global board,dx,dy,ans

    while 1:
        visit = [[0 for _ in range(6)] for _ in range(12)]
        pop_list =[]
        for i in range(12):
            for j in range(6):
                if board[i][j] == '.' or visit[i][j]:
                    continue
                q= deque()
                q.append((i,j))
                visit[i][j] = 1
                temp = []
                temp.append((i,j))
                count = 1
                while q:
                    cur = q.popleft()
                    for dir in range(4):
                        x = cur[0] + dx[dir]
                        y = cur[1] + dy[dir]
                        if x<0 or x>=12 or y<0 or y>=6:
                            continue
                        if board[x][y]=='.' or visit[x][y]:
                            continue
                        if board[x][y] != board[cur[0]][cur[1]]:
                            continue
                        visit[x][y] = count + 1
                        count+=1
                        q.append((x,y))
                        temp.append((x,y))
                if count >= 4:
                    pop_list.extend(temp)
        # print(pop_list)
        # print(visit)
        if pop_list:
            for x,y in pop_list:
                board[x][y] = 'x'
            reorder()
            # for r in board:
            #     print(r)
            ans += 1
        else:
            return


def reorder():
    global board
    
    for i in range(6):
        row = []
        x_list =[]
        for j in range(12):
            if board[j][i] == 'x':
                x_list.append(j)
            row.append(board[j][i])

        new_row = []
        for _ in range(len(x_list)):
            new_row.append('.')
        for j in range(12):
            if j in x_list:
                continue
            new_row.append(row[j])
        # print(new_row)
        for j in range(12):
            board[j][i] = new_row[j]
        # board[i] = copy.deepcopy(new_row)
        # print(board)


pop()
print(ans)
