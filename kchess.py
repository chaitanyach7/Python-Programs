def fasa():
    for i in range(8):
        a=c
        b=d
        if(i==0):
            a+=1
            b+=1
        elif(i==1):
            a+=1
            b-=1
        elif(i==2):
            a-=1
            b+=1
        elif(i==3):
            a-=1
            b-=1
        elif(i==4):
            b-=1
        elif(i==5):
            b+=1
        elif(i==6):
            a-=1
        elif(i==7):
            a+=1
        for j in range(n):
            a1=x[j]
            b1=y[j]
            for k in range(8):
                if(k==0):
                    a1+=3
                    b1+=2
                elif(k==1):
                    a1+=3
                    b1-=2
                elif(k==2):
                    a1-=3
                    b1+=2
                elif(k==3):
                    a1-=3
                    b1-=2
                elif(k==4):
                    a1+=2
                    b1-=3
                elif(k==5):
                    a1-=2
                    b1+=3
                elif(k==6):
                    a1-=2
                    b1-=3
                elif(k==7):
                    a1+=2
                    b1+=3
                if(a1==a)and(b1==b):
                    print("YES")
                    return
    print("NO")

for _ in range(int(input())):
    n=int(input())
    x=[None]*n
    y=[None]*n
    for i in range(n):
        x[i],y[i]=input().split()
        x[i]=int(x[i])
        y[i]=int(y[i])
    a,b=[int(z) for z in input().split()]
    c=a
    d=b
    fasa()
    
                    
                    
