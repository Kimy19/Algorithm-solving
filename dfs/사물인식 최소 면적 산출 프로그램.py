#Softeer [HSAT 2회 정기 코딩 인증평가 기출] 사물인식 최소 면적 산출 프로그램

import sys

n,k = map(int,input().split())
color = [[] for _ in range(k+1)]

for i in range(n):
    x,y,c = map(int,input().split())
    color[c].append((x,y))
# print(color)


min = 5000000
def dfs(cur,points,area):
    global min,color
    if cur == k+1:
        if min > area:
            min = area
            return
    
    for p in color[cur]:
        x1, y1, x2, y2 = points #min min max max
        tx,ty = p
        if tx < x1:
            x1 = tx
        elif tx > x2:
            x2 = tx
        if ty < y1:
            y1 = ty
        elif ty > y2:
            y2 = ty
        
        # 현재 넓이
        size = abs(x1-x2) * abs(y1-y2)
        # min보다 크면 백트래킹
        if size < min:
            dfs(cur+1,(x1,y1,x2,y2),size)
            

for i in color[1]:
    dfs(1,(i[0],i[1],i[0],i[1]),0)
print(min)