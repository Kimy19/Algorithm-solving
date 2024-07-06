#baekjoon 1446
n, d = map(int,input().split())

route = []
for i in range(n):
    s,e,l = map(int,input().split())
    if s<d and e<=d and e-s > l:
        route.append((s,e,l))
dis = [i for i in range(d+1)]

for i in range(d+1):
    if i > 0:
        dis[i] = min(dis[i],dis[i-1]+1)
    for s,e,l in route:
        if i == s and (dis[i]+l) < dis[e]:
            dis[e] = dis[i]+l
print(dis[d])

