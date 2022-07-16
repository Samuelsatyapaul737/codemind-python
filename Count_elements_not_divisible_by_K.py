a,b=map(int,input().split())
c=list(map(int,input().split()))
c1=0
for i in range(a):
    if c[i]%b!=0:
        c1+=1
print(c1)