MAX=256 
 
def compare(arr1, arr2): 
    for i in range(MAX): 
        if arr1[i] != arr2[i]: 
            return False
    return True
  
def search(pat, txt): 
  
    M = len(pat) 
    N = len(txt) 

    countP = [0]*MAX
  
    countTW = [0]*MAX
  
    for i in range(M): 
        (countP[ord(pat[i]) ]) += 1
        (countTW[ord(txt[i]) ]) += 1

    for i in range(M,N): 

        if compare(countP, countTW): 
            return 1 

        (countTW[ ord(txt[i]) ]) += 1

        (countTW[ ord(txt[i-M]) ]) -= 1
  
    if compare(countP, countTW): 
        return 1


def lrotate(inp,d):  
    lf = inp[:d]
    ls = inp[d:]
    s=ls+lf
    return s[0]
def rrotate(inp,d):
    rf = inp[0 : len(inp)-d] 
    rs = inp[len(inp)-d : ]
    s=rs+rf
    return s[0]
s=input()
n=int(input())
#s=a[0]
fina=s
#n=int(a[1])
b=[]
c=[]
for i in range(n):
    j,k=input().split()
    b.append(j)
    c.append(int(k))
    
#print(s,n,b,c)
ans=""
for i in range(n):
    if(b[i]=='L'):
        ans+=lrotate(s,c[i])
    else:
        ans+=rrotate(s,c[i])
#print(ans,fina)
if(search(ans,fina)):
    print("YES",end="")
else:
    print("NO",end="")
    
    
