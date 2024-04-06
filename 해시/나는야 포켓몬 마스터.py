n,m = map(int,input().split())

dict1 = {}
dict2 = {}
for i in range(n):
    name = input()
    dict1[i+1] = name
    dict2[name] = i+1
    

ans =[]
for i in range(m):
    temp = input()
    if temp.isdigit():
        ans.append(dict1[int(temp)])
    else:
        ans.append(dict2[temp])
for i in ans:
    print(i)