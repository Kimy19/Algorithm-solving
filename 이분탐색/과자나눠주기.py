#백준 16401

m,n = map(int,input().split())
num = list(map(int,input().split()))

st = 1
en = max(num)
ans = 0
while st <= en:
	mid = (st+en)//2
	count = 0
	for i in num:
		if i < mid:
			continue
		count += i//mid
	if count>= m:
		ans = max(ans,mid)
		st = mid + 1
	else:
		en = mid - 1
print(ans)