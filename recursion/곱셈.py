#백준 1629
a,b,c = map(int,input().split())

def mod(a,b,c):
	if b == 1:
		return(a % c)
	
	val = mod(a,b//2,c)
	val = val * val % c
	if b%2 == 0:
		return(val)
	return (val * a % c)

print(mod(a,b,c))

#print(pow(a,b,c))	