from collections import defaultdict,OrderedDict,Counter
from sys import stdin,stdout
from bisect import bisect_left,bisect_right
# import numpy as np
from queue import Queue,PriorityQueue
from heapq import heapify,heappop,heappush
from statistics import median
from math import gcd,sqrt,floor,factorial,ceil,log2,log10
import copy
from copy import deepcopy
import sys
sys.setrecursionlimit(10**7)
import math
import os
import bisect
import collections
mod=pow(10,9)+7

def ncr(n, r, p=mod):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den,
            p - 2, p)) % p
# input=stdin.readline
# print=stdout.write
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
# a9=pow(10,6)+10
# prime = [True for i in range(a9 + 1)]
# def SieveOfEratosthenes(n):
#     p = 2
#     while (p * p <= n):
#         if (prime[p] == True):
#             for i in range(p * p, n + 1, p):
#                 prime[i] = False
#         p += 1
def get_list():
    return list(map(int,input().split()))
def get_str_list():
    return list(input())
def get_map():
    return map(int,input().split())
def get_int():
    return int(input())
t=int(input())
for i in range(t):
    n=int(input())
    l=get_list();
    q=PriorityQueue()
    for i in range(1,n):
        index=i+1
        tuple=(l[i],index)
        q.put(tuple)
    flag=True;
    ans=[[] for i in range(2*n)]
    count=0
    while q.empty()==0:
        begin1=q.get_nowait();
        value1=begin1[0]
        index1=begin1[1]
        if q.qsize():
            begin2=q.get_nowait();
            value2=begin2[0]
            index2=begin2[1]
        else:
            begin2=None;
            value2=None;
            index2=None;
        if value1>l[0]:
            if begin2==None:
                flag=False
                break;
            diff=value1-l[0];
            ans[count].append(index1)
            ans[count].append(index2)
            ans[count].append(diff)
            count+=1
            value1 -= diff;
            value2+=diff;
            begin1=(value1,index1)
            begin2=(value2,index2)
            q.put(begin1)
            q.put(begin2)
        else:
            ans[count].append(index1)
            ans[count].append(1)
            ans[count].append(value1)
            count+=1
            l[0]+=value1
            if begin2:
                q.put(begin2)
    if flag:
        print(count)
        for j in range(count):
            print(*ans[j])
    else:
        print(-1)

