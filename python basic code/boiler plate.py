from collections import defaultdict,OrderedDict,Counter
from sys import stdin,stdout
from bisect import bisect_left,bisect_right
import numpy as np
from queue import Queue
from statistics import median
from math import gcd,sqrt,floor,factorial,ceil
import copy
from copy import deepcopy
import sys
sys.setrecursionlimit(10**7)
import math
import os
import bisect
import collections
input=stdin.readline
print=stdout.write
inf=float("inf")
adj=defaultdict(set)
visited=defaultdict(int)
def addedge(a,b):
    adj[a].add(b)
    adj[b].add(a)
def bfs(v):
    q=Queue()
    q.put(v)
    visited[v]=1
    while q.qsize()>0:
        s=q.get_nowait()
        print(s)
        for i in adj[s]:
            if visited[i]==0:
                q.put(i)
                visited[i]=1
def dfs(v,visited):
    if visited[v]==1:
        return;
    visited[v]=1

    print(v)
    for i in adj[v]:
        dfs(i,visited)


