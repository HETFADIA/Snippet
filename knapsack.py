def knapsack(arr,n,w):
    dp=[]
    for i in range(n+1):
        dp.append([])
        for j in range(w+1):
            dp[i].append(0)
    for i in range(n+1):
        for j in range(w+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif arr[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],arr[i-1]+dp[i-1][j-arr[i-1]])
    res = dp[n][w] 
    theta=[]
    if dp[n][w]!=w:
        return None
    for i in range(n, 0, -1): 
        if res <= 0: 
            break
        if res == dp[i - 1][w]: 
            continue
        else:
            theta.append(arr[i-1])
            res = res - arr[i - 1] 
            w = w - arr[i - 1] 
    return theta
def knapsack2(arr,n,w):
    dp=[]
    for i in range(n+1):
        dp.append([])
        for j in range(w+1):
            dp[i].append(0)
    for i in range(n+1):
        for j in range(w+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif arr[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],arr[i-1]+dp[i-1][j-arr[i-1]])
    return dp[n][w] 
n=int(input())
arr=list(map(int,input().split()))
w=sum(arr)//3
if 3*w==sum(arr):
    theta=knapsack(arr,n,w)
    if theta==None:
        print(0)
    else:
        theta1=[]
        for i in arr:
            if i in theta:
                theta.remove(i)
            else:
                theta1.append(i)
        if knapsack2(theta1,len(theta1),w)==w:
            print(1)
        else:
            print(0)
        
        
else:
    print(0)
