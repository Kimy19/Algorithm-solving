from bisect import bisect_left,bisect_right

def count(arr,n):
	left_index = bisect_left(arr,n)
	right_index = bisect_right(arr,n)
	return right_index-left_index

n = int(input())
num = list(map(int,input().split()))
m = int(input())
find_num = list(map(int,input().split()))

num = sorted(num)
ans = []
for i in find_num:
	ans.append(count(num,i))
print(*ans)