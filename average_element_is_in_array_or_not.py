n=int(input())
a=list(map(int,input().split()))
c=0
s=0
for i in range(n):
    s=s+a[i]
avg=s//n
for i in a:
    if avg in a:
        c=1
if c==1:
    print('True')
else:
    print('False')