for _ in range(int(input())):
    l,d,h=map(int,input().split())
    if(l*h>=d):
        print("Yes")
    else:
        print("No")
