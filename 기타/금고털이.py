#softeer 금고털이
import sys

w,n = map(int,sys.stdin.readline().split())
gold = []
value = []
for _ in range(n):
	size,cost = map(int,sys.stdin.readline().split())
	gold.append((cost,size))

gold.sort(reverse = True, key = lambda x: x[0])
ans = 0
for i in range(n):
	cost,size = gold[i]
	if w <= size:
		ans += w * cost
		w = 0
		break
	elif w > size:
		ans += size * cost
		w -=size
print(ans)
