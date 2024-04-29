#백준14499

dice = [0 for _ in range(6)]

def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

n,m,x,y,k = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
command = list(map(int,input().split()))

dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
ans = []
for dir in command:
    tx = x+dx[dir]
    ty = y+dy[dir]
    if tx<0 or tx>=n or ty<0 or ty>=n:
        continue
    turn(dir)
    x = tx
    y = ty
    if board[tx][ty] == 0:
        board[tx][ty] = dice[-1]
    else:
        dice[-1] = board[tx][ty]
        board[tx][ty] = 0
    ans.append(dice[0])

for i in ans:
    print(i)
