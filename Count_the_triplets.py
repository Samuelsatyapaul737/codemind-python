a=int(input())
for i in range(a):
    c=0
    n=int(input())
    l=list(map(int,input().split()))
    for j in range(len(l)):
        for k in range(len(l)):
            if l[j]!=l[k]:
                if l[j]+l[k] in l:
                    c+=1
    if c==0:
        print('-1')
    elif c!=0:
        print(c//2)
                 