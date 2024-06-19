import sys

n,m = map(int,sys.stdin.readline().split())
dict1 = {}
for _ in range(n):
	name = str(sys.stdin.readline())
	dict1[name] = 1
count = 0
ans = []
for _ in range(m):
	name = str(sys.stdin.readline())
	if dict1.get(name):
		count += 1
		ans.append(name)
print(count)
ans = sorted(ans)
for i in ans:
	print(i,end = '')