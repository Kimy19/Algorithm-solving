#baekjoon 23971
import math

r,c,n,m = map(int,input().split())
print(math.ceil(r/(n+1)) * math.ceil(c/(m+1)))