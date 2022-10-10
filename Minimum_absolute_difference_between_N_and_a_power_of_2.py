from math import floor, log2
def minAbs(n) :
	l=pow(2,floor(log2(n)))
	r=l*2
	return min((n-l),(r-n))

n=int(input())
print(minAbs(n))