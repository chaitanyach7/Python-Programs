a=[6, 10, 14, 15, 21, 22, 26, 33, 34, 35, 38, 39, 46, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95, 106, 111, 115, 118, 119, 122, 123, 129, 133, 134, 141, 142, 143, 145, 146, 155, 158, 159, 161, 166, 177, 178, 183, 185, 187, 194]

def validate(n):
    c=0
    for i in range(2,n):
        n1=i
        n2=n-i+1
        if n1 in a:
           if n2 in a:
               c=2
               break
              
    if(c==2):
        print('YES')
    else:
        print('NO')
t=int(input())
for i in range(t):
    n=int(input())
    validate(n-1)
