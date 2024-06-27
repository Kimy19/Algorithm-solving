#softeer

n = int(input())
w = list(map(int,input().split()))

ans = 0
for i in range(2,101):
	count = 0
	for j in range(n):
		if w[j] % i == 0:
			count += 1
	ans = max(ans,count)
print(ans)