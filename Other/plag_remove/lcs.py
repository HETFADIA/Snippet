def lcs(a,b,n,m):
    
    l=[]
    for i in range(n+1):
        l.append([])
        for j in range(m+1):
            l[i].append(0)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1]==b[j-1]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    index = l[n][m] 
    lcs = [""] * (index+1) 
    lcs[index] = "" 
    i = n
    j = m 
    while i > 0 and j > 0: 
        if a[i-1] == b[j-1]: 
            lcs[index-1] = a[i-1] 
            i-=1
            j-=1
            index-=1
        elif l[i-1][j] > l[i][j-1]: 
            i-=1
        else: 
            j-=1
    return "".join(lcs)
n=int(input())
a=input()
m=int(input())
b=input()

print(lcs(a,b,n,m))


