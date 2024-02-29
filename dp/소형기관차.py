with open('../input.txt','r') as f:
    n = int(f.readline())
    num = list(map(int,f.readline().split()))
    size = int(f.readline())

# n = int(input())
# num = list(map(int,input().split()))
# size = int(input())



for i in range(1,n):
    num[i] += num[i-1]

print(num)

dp = [[0 for _ in range(n)] for _ in range(3)]
print(dp)

for i in range(3):
    for j in range((i+1)*size-1, n):
        if i == 0:
            if j-size <0:
                dp[i][j] = max(dp[i][j-1],num[j])
            else:
                dp[i][j] = max(dp[i][j-1],num[j]-num[j-size])
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j-size]+num[j]-num[j-size])
print(dp)
print(dp[2][n-1])