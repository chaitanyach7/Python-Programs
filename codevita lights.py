n=int(input())
s=[]
ans=[]
ans2=[0]*1000000
ans3=[]
for i in range(n):
    s.append(list(input().strip()))
    c=''
    l=len(s[i])
    if(l%2==0):
        c=s[i][0]+s[i][l//2-1]+s[i][l//2]+s[i][l-1]
        ans.append(list(c.strip()))
    else:
        c=s[i][0]+s[i][l//2]+s[i][l-1]
        ans.append(list(c.strip()))
for i in range(len(ans)):
    c1=0
    #print(ord(ans[i][0]))
    if(len(ans[i])==3):
        c1=(ord(ans[i][0])*(2**0)+ord(ans[i][1])*3) + (ord(ans[i][2])*2)
    else:
        c1=(ord(ans[i][0])+ord(ans[i][1])*2) + (ord(ans[i][2])*3+ord(ans[i][3])*4)
    ans2[c1]+=1
    ans3.append(c1)
for i in range(len(ans)):
    print("".join(map(str,ans[i])),ans2[ans3[i]])
                                              
