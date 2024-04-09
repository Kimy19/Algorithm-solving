#백준 1654
from bisect import bisect_left,bisect_right
import time

k,n = map(int,input().split())
line = []
for _ in range(k):
	line.append(int(input()))

line = sorted(line)
sum = sum(line)

st = 1
en = 2147483647
ans = 0
list =[]
while st<=en:
	mid = (st+en)//2
	num = 0
	for item in line:
		if item>=mid:
			num += item//mid
	if num < n:
		en = mid-1
	else:
		ans = max(ans,mid)
		st = mid+1
print(ans)

