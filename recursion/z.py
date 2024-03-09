#백준 1074
n,r,c = map(int,input().split())

def find(n,r,c):
    if n==0:
        return 0
    if r<=pow(2,n-1)-1 and c<=pow(2,n-1)-1:
        return find(n-1,r,c)
    elif r<=pow(2,n-1)-1 and c>pow(2,n-1)-1:
        return pow(2,n-1)*pow(2,n-1)+ find(n-1,r,c-pow(2,n-1))
    elif r>pow(2,n-1)-1 and c<=pow(2,n-1)-1:
        return pow(2,n-1)*pow(2,n-1)*2 + find(n-1,r-pow(2,n-1),c)
    else:
        return pow(2,n-1)*pow(2,n-1)*3 + find(n-1,r-pow(2,n-1),c-pow(2,n-1))

print(find(n,r,c))