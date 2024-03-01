#백준 2309
h = []
for i in range(9):
	h.append(int(input()))
h.sort()
for i in range(9):
	for j in range(i+1,9):
		temp = h[:]
		temp.pop(j)
		temp.pop(i)
		if sum(temp) == 100:
			print('\n'.join(map(str, temp)))
			exit()
			

