from bisect import bisect_left, bisect_right


arr =[-1,1,2,3,4,5]
l_index = bisect_left(arr,0)#삽입가능한 가장 왼쪽 인덱스
r_index = bisect_right(arr,0)# ,, 오른쪽 인덱스

if l_index == r_index:
	print("not exist")
else:
	print("exist")