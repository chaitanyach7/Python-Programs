'''
2
3
-1 10000
8 20
-1 16
3
-1 10100
-1 5A
-1 1011010
'''
def val(c): 
    if c >= '0' and c <= '9': 
        return ord(c) - ord('0') 
    else: 
        return ord(c) - ord('A') + 10
def reVal(num): 
    if (num >= 0 and num <= 9): 
        return chr(num + ord('0'))
    else: 
        return chr(num - 10 + ord('A'));
def dog(str,base): 
    llen = len(str) 
    power = 1
    num = 0 
    for i in range(llen - 1, -1, -1): 
        num += val(str[i]) * power 
        power = power * base 
    return num
def fromDeci(base, inputNum):
    res=""
    index = 0
    while (inputNum > 0): 
        res+= reVal(inputNum % base)
        inputNum = int(inputNum / base)
    res = res[::-1]
    return res
for _ in range(int(input())):
    n=int(input())
    a,b=[],[]
    ans=None
    c=0
    for i in range(n):
        x,y=input().split()
        a.append(int(x))
        if(a[i]==-1):
            c+=1
        b.append(y)
    if(c==n):
        s=b[0]
        f1=[]
        m=max(list(s.strip()))
        base=val(str(m))+1
        for i in range(base,37):
            ab=dog(s,i)
            #print(ab)
            c1=0
            wwe=[]
            for j in range(2,37):
                wwe.append(fromDeci(j,ab))
            for i in range(n):
                if b[i] in wwe:
                    c1+=1
            if(c1==n):
                f1.append(ab)
        if(len(f1)!=0):
            print(min(f1))
        else:
            print(-1)
    else:
        for i in range(n):
            if(a[i]!=-1):
                k=i
                break
        ab=dog(b[k],a[k])
        wwe=0
        f=0
        #print(ab)
        wwf=[]
        for j in range(2,37):
            wwf.append(fromDeci(j,ab))
        for i in range(n):
            for j in range(len(wwf)):
                if b[i]==wwf[j] and (a[i]==-1 or a[i]==j+2):
                    wwe+=1
        if(wwe==n) and f==0:
            print(ab)
        else:
            print(-1)
