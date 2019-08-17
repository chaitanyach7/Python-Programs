import sys
for _ in range(int(input())):
    n=int(input())
    a=[]
    for i in range(1,n+1):
        a.append(i)
    l=len(a)
    xi=0
    while(l>6):
        print('?',a[xi],a[xi+1],a[xi+2],a[xi+3],a[xi+4])
        sys.stdout.flush()
        x,y=map(int,input().split())
        a.remove(x)
        a.remove(y)
        l=len(a)
        if(l<6):
            a.append(y)
            break
        if(l==6):
            break
    #ans=[]
    #fas=[0]
    #pntr=[a[0],a[1],a[2],a[3],a[4]]
    x=[None]*6
    y=[None]*6
    c=[0]*6
    print('?',a[0],a[1],a[2],a[3],a[4])
    sys.stdout.flush()
    x[0],y[0]=map(int,input().split())
    print('?',a[0],a[1],a[2],a[3],a[5])
    sys.stdout.flush()
    x[1],y[1]=map(int,input().split())
    print('?',a[0],a[1],a[2],a[5],a[4])
    sys.stdout.flush()
    x[2],y[2]=map(int,input().split())
    print('?',a[0],a[1],a[5],a[3],a[4])
    sys.stdout.flush()
    x[3],y[3]=map(int,input().split())
    print('?',a[0],a[5],a[2],a[3],a[4])
    sys.stdout.flush()
    x[4],y[4]=map(int,input().split())
    print('?',a[5],a[1],a[2],a[3],a[4])
    sys.stdout.flush()
    x[5],y[5]=map(int,input().split())
    #print(x,y)
    for i in range(6):
        c1=0
        for j in range(0,6):
            #print(x[i],x[j],y[i],y[j])
            if(x[i]==x[j] and y[i]==y[j]):
                c1+=1
        c[i]=c1
    #print(c,a)
    fasak=5
    #ans=0
    for i in range(6):
        if(c[i]==2):
            if(a[fasak] in x or a[fasak] in y):
                fasak-=1
                continue
            else:
                ans=a[fasak]
        #print(i,fasak)
        fasak-=1
        #print(fasak)
    print("!",ans)
