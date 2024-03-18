#softeer 우물안 개구리
# import sys

# n,m = map(int,input().split())
# w =[0]
# temp = list(map(int,input().split()))
# w.extend(temp)

# best = [0 for i in range(n+1)]

# rel =[]
# for i in range(m):
#     a,b = map(int,input().split())
#     rel.append((a,b))
            
#     if w[a] > w[b]:
#         if best[a]!= -1:
#             best[a] = 1
#         best[b] = -1
#     elif w[b] > w[a]:
#         if best[b]!= -1:
#             best[b] = 1
#         best[a] = -1
#     else:
#         best[b] = -1
#         best[a] = -1

# print(best.count(1)+best.count(0)-1)
    

#두번째 풀이
n,m = map(int,input().split())
w = [0] + list(map(int,input().split()))
rel = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    rel[a].append(b)
    rel[b].append(a)

count = 0

for i in range(1,n+1):
    flag = 1
    for j in rel[i]:
        if w[i] <= w[j]:
            flag = 0
            break
    if flag == 1:
        count+=1
  
print(count)