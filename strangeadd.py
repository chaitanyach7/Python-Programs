import math
cp=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
for i in range(int(input())):
    n=int(input())
    c=0
    a=list(map(int,input().split()))
    b=[0]*n
    for j in range(1,n):
        if(a[j-1] in cp):
            b[j-1]=a[j-1]
            if(a[j] in cp):
                b[j]=a[j]
            else:
                for k in range(0,len(cp)):
                    if(cp[k]<a[j]):
                        b[j]=cp[k]
                    else:
                        break
        else:
            for k in range(0,len(cp)):
                if(cp[k]<a[j-1]):
                    b[j-1]=cp[k]
                else:
                    break
            if(a[j] in cp):
                b[j]=a[j]
            else:
                for k in range(0,len(cp)):
                    if(cp[k]<a[j]):
                        b[j]=cp[k]
                    else:
                        break
    for j in range(n):
        if(a[j]==b[j]):
            c+=1
    print(math.ceil((n-c)/2))
    print(' '.join(map(str,b)))
