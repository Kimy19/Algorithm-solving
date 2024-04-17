#백준 2003
n,m = map(int,input().split())

num = list(map(int,input().split()))
st = 0
en = 0
sum = [0]
for i in range(len(num)):
	sum.append(num[i]+ sum[-1])
ans = 0
while en < len(num) and st < len(num):
	if st == en:
		temp = num[st]
	else:
		temp = sum[en+1] - sum[st]
	if temp < m:
		en += 1
	else:
		if temp == m:
			ans += 1
		st += 1
print(ans)