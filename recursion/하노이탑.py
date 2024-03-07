#백준 11729
n = int(input())
count = 0
route = []
def func(a,b,n):
	global count
	if n == 1:
		count+=1
		route.append((a,b))
		return
	func(a,6-a-b,n-1)
	route.append((a,b))
	count+=1
	func(6-a-b,b,n-1)

func(1,3,n)
print(count)
for i in range(len(route)):
	print(route[i][0],route[i][1])