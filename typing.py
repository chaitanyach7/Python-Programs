aws=['a','e','i','o','u']
nans=[['e','i','o'],['e','i','u'],['e','o','u'],['i','o','u'],['e','i','o','u'],['a'],['e'],['i'],['o'],['u'],['a','e'],['a','i'],['a','o'],['a','u'],['e','i'],['e','o'],['e','u'],['i','o'],['i','u'],['o','u'],['a','e','i'],['a','e','o'],['a','e','u'],['a','i','o'],['a','i','u'],['a','o','u'],['a','e','i','o'],['a','e','o','u'],['a','e','i','u'],['a','i','o','u'],['a','e','i','o','u']]
mans=[0]*31
#print(len(nans))
for _ in range(int(input())):
    n=int(input())
    a=[None]*n
    c=0
    for i in range(n):
        a[i]=input().strip()
        a[i]=sorted(list(set(a[i])))
        #print(nans.index(a[i]))
        mans[nans.index(a[i])]+=1
    for i in range(n):
        ans=sorted([x for x in aws if x not in a[i]])
        #print(ans)
        for i in range(len(nans)):
            #print(ans,nans[i])
            #issubset()
            if(all(x in nans[i] for x in ans)):
                c+=mans[i]
    #print(mans)
    mans=[0]*31
    print(c//2)
