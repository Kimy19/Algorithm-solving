#백준1920
#이진 탐색 직접구현시 st,en은 항상 찾고자하는 것이 될수있는 범위로 설정
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))

m = int(input())
find = list(map(int,input().split()))

def find_num(arr, n):
	st = 0
	en = len(arr)-1
	while st<=en:
		mid = (st + en) // 2
		if arr[mid] == n:
			print(1)
			return
		elif arr[mid] > n:
			en = mid-1
		elif arr[mid] < n:
			st = mid+1
	print(0)
	return

num = sorted(num)
for i in find:
	find_num(num, i)


