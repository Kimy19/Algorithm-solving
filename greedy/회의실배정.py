# 백준 1931
n = int(input())
time =[]
for _ in range(n):
	t1,t2 = map(int,input().split())
	time.append((t1,t2))

time = sorted(time, key=lambda x: (x[1], x[0]))

print(time)
	
count = 1
end = time[0][1]
for i in range(1,n):
	if time[i][0] < end:
		continue
	count+=1
	end = time[i][1]
print(count)
	
