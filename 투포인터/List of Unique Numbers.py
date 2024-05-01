#백준 13144
n = int(input())
num = list(map(int,input().split()))
st = 0
en = 0
count = 0
visited = [0 for _ in range(100001)]

while st<= en and en<n:
    if not visited[num[en]]:
        visited[num[en]] = 1
        count += en-st +1
        en+= 1
    else:
        while visited[num[en]]:
            visited[num[st]] = 0
            st+= 1

print(count)

#set을 활용하는법
def count_unique_subsequences(arr):
    n = len(arr)
    count = 0
    unique_nums = set()

    left = 0
    for right in range(n):
        while arr[right] in unique_nums:
            unique_nums.remove(arr[left])
            left += 1
        unique_nums.add(arr[right])
        count += right - left + 1

    return count
