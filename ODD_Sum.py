n=int(input())
a=list(map(int,input().split()))
even=0
odd=0
for i in range(n):
    if a[i]%2!=0:
        odd+=a[i]
print(odd)