#백준 7785 해시

n = int(input())

dict = {}
for i in range(n):
	# row = list(map(str,input().split()))
	name, state = input().strip().split()
	# print(name,state)
	if state == 'leave':
		del dict[name]
	else:
		dict[name] = True

ans = sorted(dict.keys(), reverse= True)
for i in ans:
	print(i)
