import sys
k,l = map(int,sys.stdin.readline().split())

dict = {}
dict2 = {}
for i in range(l):
    num = str(sys.stdin.readline().strip())
    dict[num] = i+1
    dict2[i+1] = num
i = 1
cnt = 1
while cnt<=k and i <= l:
    if dict[dict2[i]] == i:
        print(dict2[i])
        i+= 1
        cnt+=1
    else:
        i+=1
        continue
