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
        b.append(y)
    s=b[0]
    if(a[0]==-1):
        m=max(list(s.strip()))
        base=val(str(m))+1
    else:
        base=a[0]
    f=0
    #print(base)
    for i in range(base,37):
        ab=dog(s,i)
        c=0
        for j in range(2,37):
            if fromDeci(j,ab) in b:
                c+=1
        if(c==n):
            f=1
            break
    if(f==1):
        print(ab)
    else:
        print('−1')
