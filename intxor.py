import sys
def fasak():
    a=[]
    v=[]
    x=[]
    answer=[]
    n=int(input())
    tseries=int(n//4)
    count=int(n%4)
    if(count==0):
        for i in range(n):
            a.append(i+1)
        valpie=4
        for i in range(n):
            if(valpie<=n):
                x.append(valpie)
                valpie+=4
            else:
                break
        x.insert(0,0)
        st=0
        for lm in range(tseries):
            c=x[st]
            print(1,a[c],a[c+1],a[c+2])
            sys.stdout.flush()
            r=int(input())
            ar=r
            print(1,a[c+1],a[c+2],a[c+3])
            sys.stdout.flush()
            r=int(input())
            br=r
            print(1,a[c+2],a[c+3],a[c])
            sys.stdout.flush()
            r=int(input())
            cr=r
            print(1,a[c+3],a[c],a[c+1])
            sys.stdout.flush()
            r=int(input())
            dr=r
            st+=1
            answer.append(ar^cr^dr)
            answer.append(br^dr^ar)
            answer.append(cr^ar^br)
            answer.append(dr^br^cr)
    elif(count==1):
        for i in range(n):
            a.append(i+1)
        valpie=5
        for i in range(n):
            if(valpie<=n):
                x.append(valpie)
                valpie+=4
            else:
                break
        x.insert(0,0)
        st=0
        print('1 1 2 3')
        sys.stdout.flush()
        r=int(input())
        ar=r
        print('1 2 3 4')
        sys.stdout.flush()
        r=int(input())
        br=r
        print('1 3 4 5')
        sys.stdout.flush()
        r=int(input())
        cr=r
        print('1 4 5 1')
        sys.stdout.flush()
        r=int(input())
        dr=r
        print('1 5 1 2')
        sys.stdout.flush()
        r=int(input())
        er=r
        answer.append(br^cr^er)
        answer.append(cr^dr^ar)
        answer.append(dr^er^br)
        answer.append(er^ar^cr)
        answer.append(ar^br^dr)
        st+=1
        lm=0
        while(lm<tseries-1):
            c=x[st]
            print(1,a[c],a[c+1],a[c+2])
            sys.stdout.flush()
            r=int(input())
            ar=r
            print(1,a[c+1],a[c+2],a[c+3])
            sys.stdout.flush()
            r=int(input())
            br=r
            print(1,a[c+2],a[c+3],a[c])
            sys.stdout.flush()
            r=int(input())
            cr=r
            print(1,a[c+3],a[c],a[c+1])
            sys.stdout.flush()
            r=int(input())
            dr=r
            st+=1
            answer.append(ar^cr^dr)
            answer.append(br^dr^ar)
            answer.append(cr^ar^br)
            answer.append(dr^br^cr)
            lm+=1
    elif(count==2):
        for i in range(n):
            a.append(i+1)
        valpie=6
        for i in range(n):
            if(valpie<=n):
                x.append(valpie)
                valpie+=4
            else:
                break
        x.insert(0,0)
        st=0
        c=x[st]
        print('1 1 2 5')
        sys.stdout.flush()
        r=int(input())
        ar=r
        print('1 2 3 6')
        sys.stdout.flush()
        r=int(input())
        br=r
        print('1 3 4 1')
        sys.stdout.flush()
        r=int(input())
        cr=r
        print('1 4 5 2')
        sys.stdout.flush()
        r=int(input())
        dr=r
        print('1 5 6 3')
        sys.stdout.flush()
        r=int(input())
        er=r
        print('1 6 1 4')
        sys.stdout.flush()
        r=int(input())
        fr=r
        answer.append(ar^br^er)
        answer.append(br^cr^fr)
        answer.append(cr^dr^ar)
        answer.append(dr^er^br)
        answer.append(er^fr^cr)
        answer.append(fr^ar^dr)
        st+=1
        for lm in range(tseries-1):
            c=x[st]
            print(1,a[c],a[c+1],a[c+2])
            sys.stdout.flush()
            r=int(input())
            ar=r
            print(1,a[c+1],a[c+2],a[c+3])
            sys.stdout.flush()
            r=int(input())
            br=r
            print(1,a[c+2],a[c+3],a[c])
            sys.stdout.flush()
            r=int(input())
            cr=r
            print(1,a[c+3],a[c],a[c+1])
            sys.stdout.flush()
            r=int(input())
            dr=r
            st+=1
            answer.append(ar^cr^dr)
            answer.append(br^dr^ar)
            answer.append(cr^ar^br)
            answer.append(dr^br^cr)
    elif(count==3):
        for i in range(n):
            a.append(i+1)
        valpie=7
        for i in range(n):
            if(valpie<=n):
                x.append(valpie)
                valpie+=4
            else:
                break
        x.insert(0,0)
        st=0
        print('1 1 2 3')
        sys.stdout.flush()
        r=int(input())
        ar=r
        print('1 2 3 4')
        sys.stdout.flush()
        r=int(input())
        br=r
        print('1 3 4 5')
        sys.stdout.flush()
        r=int(input())
        cr=r
        print('1 4 5 6')
        sys.stdout.flush()
        r=int(input())
        dr=r
        print('1 5 6 7')
        sys.stdout.flush()
        r=int(input())
        er=r
        print('1 6 7 1')
        sys.stdout.flush()
        r=int(input())
        fr=r
        print('1 7 1 2')
        sys.stdout.flush()
        r=int(input())
        gr=r
        answer.append(ar^cr^dr^fr^gr)
        answer.append(br^dr^er^gr^ar)
        answer.append(cr^er^fr^ar^br)
        answer.append(dr^fr^gr^br^cr)
        answer.append(er^gr^ar^cr^dr)
        answer.append(fr^ar^br^dr^er)
        answer.append(gr^br^cr^er^fr)
        st+=1
        lm=0
        while(lm<tseries-1):
            c=x[st]
            print(1,a[c],a[c+1],a[c+2])
            sys.stdout.flush()
            r=int(input())
            ar=r
            print(1,a[c+1],a[c+2],a[c+3])
            sys.stdout.flush()
            r=int(input())
            br=r
            print(1,a[c+2],a[c+3],a[c])
            sys.stdout.flush()
            r=int(input())
            cr=r
            print(1,a[c+3],a[c],a[c+1])
            sys.stdout.flush()
            r=int(input())
            dr=r
            st+=1
            answer.append(ar^cr^dr)
            answer.append(br^dr^ar)
            answer.append(cr^ar^br)
            answer.append(dr^br^cr)
            lm+=1
    answer.insert(0,2)
    print(" ".join(map(str,answer)))
    sys.stdout.flush()
    #print("\n")
    omg=int(input())
    sys.stdout.flush()
    if(omg==-1):
        return 1
for _ in range(int(input())):
    pubg=fasak()
    if(pubg==1):
        break
