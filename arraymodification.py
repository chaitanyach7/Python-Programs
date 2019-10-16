for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    w=k//n
    b=a
    if(w==0):
        for i in range(k):
            a[i]=a[i]^a[n-i-1]
        print(" ".join(map(str,a)))
    else:
        seq1=[]
        seq2=[]
        seq3=[]
        for i in range(n):
            a[i%n]=a[i%n]^a[n-(i%n)-1]
            seq1.append(a[i%n])
        for i in range(n):
            a[i%n]=a[i%n]^a[n-(i%n)-1]
            seq2.append(a[i%n])
        for i in range(n):
            a[i%n]=a[i%n]^a[n-(i%n)-1]
            seq3.append(a[i%n])
        
        if(w%3==1):
            #print(seq1,1)
            for i in range(k%n):
                seq1[i%n]=seq1[i%n]^seq1[n-(i%n)-1]
            print(" ".join(map(str,seq1)))
        elif(w%3==2):
            #print(seq2,2)
            for i in range(k%n):
                seq2[i%n]=seq2[i%n]^seq2[n-(i%n)-1]
            print(" ".join(map(str,seq2)))
        else:
            #print(seq3,3)
            for i in range(k%n):
                seq3[i%n]=seq3[i%n]^seq3[n-(i%n)-1]
            print(" ".join(map(str,seq3)))
