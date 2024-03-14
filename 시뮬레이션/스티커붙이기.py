#백준 18808
import copy
n,m,k = map(int,input().split())

s_size = []
sticker = []

for i in range(k):
    size = list(map(int,input().split()))
    s_size.append(size)
    temp = []
    for j in range(size[0]):
        row = list(map(int,input().split()))
        temp.append(row)
    sticker.append(copy.deepcopy(temp))

# #90도 돌리는 함수
def spin(arr,size):
    result = []
    # print(arr)
    for i in range(size[1]):
        row = [r[i] for r in arr[::-1]]
        result.append(row)
    # print(result)
    return result


def OOB(x,y):
    if x<0 or x>n or y<0 or y>m:
        return True
    else: return False

def check_fit(sticker,size,r,c):
    global board
    x,y= size
    for i in range(x):
        for j in range(y):
            if board[r+i][c+j] and sticker[i][j] :
                # print("스티커",sticker)
                # print(f'시작점{r,c},i,j{i,j}')
                return False
            if sticker[i][j]==0 :
                continue
    for i in range(x):
        for j in range(y):
            if sticker[i][j]==1:
                board[r+i][c+j] = 1
    return True

board = [[0 for _ in range(m)] for _ in range(n)] # 보드

for i in range(k):#스티커
    # print(f'스티커 {i+1}')
    for dir in range(4):#90도 회전
        if dir>0:
            # print(f'스티커 {i+1} 회전{dir}')
            sticker[i] = spin(sticker[i],s_size[i])
            s_size[i] = list(reversed(s_size[i]))
            # print(f'size {s_size[i]}')
        temp = sticker[i]

        for r in range(n-s_size[i][0]+1):
            for c in range(m-s_size[i][1]+1):#시작점
                if not check_fit(temp,s_size[i],r,c):
                    continue
                # print(f'{r} {c}에서 성공')
                break
            else:
                continue
            break
        else:
            continue
        break
    

# print(board)
ans = sum(row.count(1) for row in board) 
print(ans)
                            




