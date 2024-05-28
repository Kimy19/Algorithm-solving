#softeer 부트캠프 코테
from itertools import permutations


num = list(map(str,input().split()))
perms = permutations(num)
max_num = None
min_num = None

for perm in perms:
    num_str = ''.join(map(str,perm))
    if max_num is None or num_str>max_num:
        max_num = num_str
    if min_num is None or num_str<min_num:
        min_num = num_str

print(int(min_num) + int(max_num))



