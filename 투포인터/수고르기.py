n,m = map(int,input().split())

num = []
for i in range(n):
	num.append(int(input()))

num = sorted(num)
ans = max(num) - min(num)
st = 0
en = 0
while st<n and en<n:
	if num[en]-num[st] < m:
		en+= 1
	else:
		ans = min(ans,num[en]-num[st])
		st+= 1

print(ans)