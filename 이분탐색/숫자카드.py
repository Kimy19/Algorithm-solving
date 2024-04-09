#백준 10815
import sys
from bisect import bisect_left, bisect_right

n = int(input())
num = list(map(int,sys.stdin.readline().split()))
m = int(input())
num2 = list(map(int,sys.stdin.readline().split()))
num = sorted(num)

ans = []
for i in num2:
	if bisect_right(num,i) - bisect_left(num,i) > 0:
		ans.append(1)
	else:
		ans.append(0)
print(*ans)



