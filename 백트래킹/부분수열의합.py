#백준 1182
n, s = map(int, input().split())
num = list(map(int,input().split()))
count = 0

def func(sum,cur):
	global count
	global n
	
	if cur == n:
		if sum == s:
			count+=1
		return
	func(sum+num[cur],cur+1)
	func(sum,cur+1)

func(0,0)
if s == 0:
	count-= 1
print(count)

