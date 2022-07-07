def dig(n):
    s,c=0,0
    while n>0:
        i=n%10
        s=s+i
        c+=1
        n=n//10
    if c==1:
        return s
    else:
        p=s
        return dig(p)
n=int(input())
print(dig(n))
    