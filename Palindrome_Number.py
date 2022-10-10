n=int(input())
for i in range(n):
    m = int(input())
    k = int(str(m)[::-1])
    if m==k:
        print(True)
    else:
        print(False)