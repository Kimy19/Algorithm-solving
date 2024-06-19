#baekjoon 11723
import sys

n = int(sys.stdin.readline())
arr = set()
for i in range(n):
	temp = sys.stdin.readline().split()
	if temp[0] == "all":
		arr = set()
		for i in range(1,21):
			arr.add(i)
		continue
	elif temp[0] == "empty":
		arr = set()
		continue
	num = int(temp[1])
	cmd = temp[0]
	if cmd == "add":
		arr.add(num)
	elif cmd == "remove":
		arr.discard(num)
	elif cmd == "check":
		if num in arr:
			print(1)
		else:
			print(0)
	elif cmd == "toggle":
		if num in arr:
			arr.discard(num)
		else:
			arr.add(num)