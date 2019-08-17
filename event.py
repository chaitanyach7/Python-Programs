for _ in range(int(input())):
    a,b=input().split()
    b=str(b)
    a=list(a.strip())
    mn=min(a)
    c=0
    for i in a:
        if(i==mn):
            break
        c+=1
    #print(mn,c)
    for i in range(c):
        a.append(b)
        del(a[0])
    for i in range(len(a)):
        if(a[i]>b):
            a[i]=b
    print("".join(map(str,a)))
    
