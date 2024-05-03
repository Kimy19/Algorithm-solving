#백준 1822
import sys
from bisect import bisect_left,bisect_right

n, m = map(int,input().split())

a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

a = sorted(a)
b = sorted(b)
ans = []
for i in a:
	temp = bisect_right(b,i) - bisect_left(b,i)
	if temp == 0:
		ans.append(i)
print(len(ans))
print(*ans)


	