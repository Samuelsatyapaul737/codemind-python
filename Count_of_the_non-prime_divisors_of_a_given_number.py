def prime(n):
    if n==1:
        return 1
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
c=0
l=[]
c1=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
        if prime(i):
            c1+=1
print((c-c1)+1)