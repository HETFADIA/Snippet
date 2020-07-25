from collections import defaultdict
n=int(input("Enter no of vertices:"))
q=int(input("Enter no of edges:"))
adj=defaultdict(set)
visited=defaultdict(int)
connected=defaultdict(int)
def dfs(v):
    visited[v] = 1
    print(v)
    if v==n:
        connected[1]=n
    for i in adj[v]:
        if visited[i]==0:

            dfs(i)


def addedge(v,w):
    adj[v].add(w)
    adj[w].add(v)

for i in range(q):
    a,b=map(int,input().split())
    addedge(a,b)
dfs(1)
if connected[1]==n:
    print("1 and",n,"are connected")
else:
    print("1 and", n, "are not connected")
