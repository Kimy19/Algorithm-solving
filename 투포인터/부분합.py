n,m = map(int,input().split())

num = [0]
num.extend(list(map(int,input().split())))
# num = sorted(num)

sum = [0]
for i in range(1,n+1):
	sum.append(sum[i-1] + num[i])

st = 1
en = 1
ans = n+1
while st <= n and en <= n:
	if sum[en] - sum[st-1] < m:
		en+=1
	else:
		ans = min(ans,en-st+1)
		st+=1


if ans == n+1:
	print(0)
else:
	print(ans)