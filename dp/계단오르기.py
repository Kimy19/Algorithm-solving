n = int(input())
num=[0]
for i in range(n):
    num.append(int(input()))

dp1 = [0 for _ in range(n+1)]
dp2 = [0 for _ in range(n+1)]
dp1[1] = num[1]
dp2[1] = num[1]


for i in range(2,n+1):
    dp1[i] = dp2[i-1] + num[i]
    dp2[i] = max(dp1[i-2],dp2[i-2]) + num[i]
print(max(dp1[n],dp2[n]))