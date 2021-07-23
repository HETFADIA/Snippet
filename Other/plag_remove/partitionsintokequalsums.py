def isKPartitionPossibleRec(arr, subsetSum, taken,  
                            subset, K, N, curIdx, limitIdx): 
    if subsetSum[curIdx] == subset: 
        if (curIdx == K - 2): 
            return True
        return isKPartitionPossibleRec(arr, subsetSum, taken,  
                                       subset, K, N, curIdx + 1 , N - 1) 
    for i in range(limitIdx, -1, -1): 
        if (taken[i]): 
            continue
        tmp = subsetSum[curIdx] + arr[i]  
        if (tmp <= subset): 
            taken[i] = True
            subsetSum[curIdx] += arr[i]  
            nxt = isKPartitionPossibleRec(arr, subsetSum, taken,  
                                          subset, K, N, curIdx, i - 1) 
            taken[i] = False
            subsetSum[curIdx] -= arr[i]  
            if (nxt): 
                return True
    return False
def isKPartitionPossible(arr, N, K): 
    if (K == 1): 
        return True
    if (N < K): 
        return False
    sum = 0
    for i in range(N): 
        sum += arr[i]  
    if (sum % K != 0): 
        return False
    subset = sum // K  
    subsetSum = [0] * K  
    taken = [0] * N 
    for i in range(K): 
        subsetSum[i] = 0
    for i in range(N): 
        taken[i] = False
    subsetSum[0] = arr[N - 1]  
    taken[N - 1] = True
    return isKPartitionPossibleRec(arr, subsetSum, taken,  
                                   subset, K, N, 0, N - 1)
N=int(input())
arr = list(map(int,input().split()))
if (isKPartitionPossible(arr, N, 3)): 
    print(1) 
else: 
    print(0) 

