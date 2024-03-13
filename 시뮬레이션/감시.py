#백준 감시 15683
dx = [1,0,-1,0]
dy = [0,1,0,-1]

n,m = map(int,input().split())


board1 = []
board2 = []
cctv = []

def view(x,y,dir):
    dir%=4
    while(1):
        x+=dx[dir]
        y+=dy[dir]
        if x<0 or x>=n or y<0 or y>=m or board2[x][y] == 6:
            return
        if board2[x][y]!=0:
            continue
        board2[x][y] = 7

mn = 0
for i in range(n):
    row = list(map(int,input().split()))
    board1.append(row)
    for j in range(m):
        if row[j] != 0 and row[j] != 6:
            cctv.append((i,j))
        if row[j] == 0:
            mn+=1

for tmp in range(1<<(2*len(cctv))):
    board2 = [row[:] for row in board1]
    brute = tmp
    for i in range(len(cctv)):
        dir = brute % 4
        brute//=4
        x, y = cctv[i]
        if board1[x][y] == 1:
            view(x, y, dir)
        elif board1[x][y] == 2:
            view(x, y, dir)
            view(x, y, dir + 2)
        elif board1[x][y] == 3:
            view(x, y, dir)
            view(x, y, dir + 1)
        elif board1[x][y] == 4:
            view(x, y, dir)
            view(x, y, dir + 1)
            view(x, y, dir + 2)
        else:  # board1[x][y] == 5
            view(x, y, dir)
            view(x, y, dir + 1)
            view(x, y, dir + 2)
            view(x, y, dir + 3)
    val = sum(row.count(0) for row in board2)
    mn = min(mn,val)

print(mn)


