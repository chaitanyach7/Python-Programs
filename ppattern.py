for _ in range(int(input())):
    n=int(input())
    v=1
    a=[[None]*n]*n
    a[0][0]=v
    v+=1
    for i in range(n):
        for j in range(i,n):
            if(i==0 and j==0):
                break
            a1,a2=i,j
            print(a1,a2,i,j)
            while(True):
                a[a1][a2]=v
                v+=1
                a1+=1
                a2-=1
                print(a1,a2,i,j)
                if(a1==j and a2==i):
                    break
    print(a)
