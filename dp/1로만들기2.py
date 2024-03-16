#백준 12852
n =  int(input())
ans = []
dp = [0 for _ in range(n+1)]
route = [0 for _ in range(n+1)]

for i in range(2,n+1):
    if i % 3 != 0 and i%2 != 0:
        dp[i] = dp[i-1]+1
        route[i] = i-1
    elif i%3==0:
        if dp[i//3]>= dp[i-1]:
            dp[i] = dp[i-1]+1
            route[i] = i-1
        else:
            dp[i] = dp[i//3]+1
            route[i] = i//3
    elif i%2==0:
        if dp[i//2]>= dp[i-1]:
            dp[i] = dp[i-1]+1
            route[i] = i-1
        else:
            dp[i] = dp[i//2]+1
            route[i] = i//2
i = n
ans.append(n)
while i != 1:
    ans.append(route[i])
    i = route[i]


print(dp[n])
print(*ans)