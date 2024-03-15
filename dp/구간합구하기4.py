#백준 11659
n,m = map(int,input().split())
num =[0]
num.extend(list(map(int,input().split())))

section = []
for _ in range(m):
    i, j = map(int,input().split())
    section.append((i,j))
sum = [0]
for i in range(1,n+1):
    sum.append(sum[i-1]+num[i])

for i in range(m):
    x,y =section[i]
    print(sum[y] - sum[x-1])