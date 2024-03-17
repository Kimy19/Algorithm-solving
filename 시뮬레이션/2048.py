#백준 12100
import copy

N = int(input())
board = []
for i in range(N):
    row = list(map(int,input().split()))
    board.append(row)

def move(dir):
    global board2,N
    if dir<=1:
        
        for index,arr in enumerate(board2):#한줄씩
            temp = []
            if dir==1:
                arr = arr[::-1]
            for i in range(len(arr)):# 0 아닌수 추출
                if arr[i] != 0:
                    temp.append(arr[i])
            # print(temp)
            new_row = []
            for i in range(len(temp)):# 합칠 수들 합치기
                if temp[i] == -1:
                    continue
                if i == len(temp)-1:
                    new_row.append(temp[i])
                    continue
                if temp[i] == temp[i+1]:
                    new_row.append(temp[i] *2)
                    temp[i+1] = -1
                else:
                    new_row.append(temp[i])
            for _ in range(len(arr)-len(new_row)): # 0 추가로 넣어주기
                new_row.append(0)
            # print(new_row)
            if dir ==1:
                new_row = new_row[::-1]
            board2[index] = copy.deepcopy(new_row) # 원래 보드에 복사
            # print(board2)
        
    else:
        temp_board=[]
        for i in range(N):
            arr = [r[i] for r in board2[::-1]]
            temp = []
            if dir==3:
                arr = arr[::-1]
            for i in range(len(arr)):# 0 아닌수 추출
                if arr[i] != 0:
                    temp.append(arr[i])
            # print(temp)
            new_row = []
            for i in range(len(temp)):# 합칠 수들 합치기
                if temp[i] == -1:
                    continue
                if i == len(temp)-1:
                    new_row.append(temp[i])
                    continue
                if temp[i] == temp[i+1]:
                    new_row.append(temp[i] *2)
                    temp[i+1] = -1
                else:
                    new_row.append(temp[i])
            for _ in range(len(arr)-len(new_row)): # 0 추가로 넣어주기
                new_row.append(0)
            # print(new_row)
            if dir ==3:
                new_row = new_row[::-1]
            temp_board.append(new_row)
            # print(temp_board)
        for i in range(N):
            for j in range(N):
                board2[N-j-1][i] = temp_board[i][j]
        # print(board2)
            
                    

# board2 = copy.deepcopy(board)
# move(3)
    
ans = 0
#1024가지
for n in range(1024):
    board2 = copy.deepcopy(board)
    # num =[]
    for _ in range(5):
        dir=n%4
        # num.append(dir)
        n//=4
        move(dir)
    # print(num)
    for row in board2:
        ans = max(ans,max(row))
print(ans)