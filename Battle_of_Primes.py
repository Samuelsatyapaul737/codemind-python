def prime(n):
    if n==1:
        return 0
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    return 1
x = int(input())
y = int(input())
i=1
v = x+y
while i!=0:
    n = v+i
    if prime(n):
        m=n
        break
    i += 1
print(abs((x+y)-m))