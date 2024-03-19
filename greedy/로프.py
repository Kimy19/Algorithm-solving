#백준 2217
n = int(input())
w = []
for i in range(n):
	w.append(int(input()))

w = sorted(w, reverse= True)

max = 0
for i in range(n):
	if max< w[i] * (i+1):
		max = w[i] *(i+1)
print(max)
	