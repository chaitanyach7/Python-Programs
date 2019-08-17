
def balla(N, K): 

    if (N == 0): return 0
    if (K == 0): return 1

    if (memo[N][K] != 0): 
        return memo[N][K] 

    sum = 0
    for i in range(K + 1): 

        if (i <= N - 1): 
            sum += balla(N - 1, K - i) 

    memo[N][K] = sum
  
    return sum
M=500
memo = [[0 for i in range(M)] for j in range(M)]
for _ in range(int(input())):
    a=list(map(int,input().split()))
    for n in a:
        m=(n*(n-1))/2
        for i in m:
            print(balla(n,i),end=" ")
        print()
