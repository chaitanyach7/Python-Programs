from sys import maxsize 
q,k=map(int,input().split())
arr=[]
brr=[]
ans=0
for _ in range(q):
    qs=list(map(int,input().split()))
    if(qs[0]==1):
        arr.insert(0,qs[2])
        brr.insert(0,qs[1]^ans)
    elif(qs[0]==2):
        arr.append(qs[2])
        brr.append(qs[1]^ans)
    else:
        l=len(arr)
        #sum1=0
        fas=ans^qs[1]
        #print(fas)
        a1=fas-k
        a2=fas+k
        #print(a1,a2,fas)
        max_so_far = -maxsize - 1
        max_ending_here = 0
        abr=[]
        for i in range(l):
            if(brr[i]>=a1)and(brr[i]<=a2):
                #abr.append(arr[i])
        #l1=len(abr)
        #print(abr)
        #for i in range(l1):
                max_ending_here = max_ending_here + arr[i] 
                if (max_so_far < max_ending_here): 
                    max_so_far = max_ending_here 
                if max_ending_here < 0: 
                    max_ending_here = 0
            if(max_so_far<0):
                max_so_far=0
        print(max_so_far)
        ans=max_so_far
