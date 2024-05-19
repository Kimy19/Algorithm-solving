
t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    hat = list(map(int,input().split()))
    num = sorted(num)
    hat = sorted(hat)
    temp = [[0] for _ in range(n+1)]
    used = [0 for _ in range(2001)]
    for i in range(len(num)):
        for j in hat:
            if num[i]-3 <=j and num[i]+3 >= j:
                temp[i][0] += 1
                temp[i].append(j)
    count = 0
    for i in temp:
        if i[0] == 0:
            continue
        for j in range(1,len(i)):
            if used[i[j]] != 1:
                count+= 1
                used[i[j]] = 1
                break
    ans.append(count)

for i in range(len(ans)):
    print(f"#{i+1} {ans[i]}")