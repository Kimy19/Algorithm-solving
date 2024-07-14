#baekjoon 22862

n,k = map(int,input().split())
num = list(map(int,input().split()))

s = 0
e = 0
count = 0
ans = 0

while e < n:
    if count > k:
        if num[s] % 2 == 1:
            count -= 1
        s += 1
        continue
    else:
        if num[e] % 2 == 1:
            count += 1
        e += 1
        ans = max(ans,(e-s-count))
print(ans)