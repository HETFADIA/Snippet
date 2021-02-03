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
import random
from random import random,randint,randrange
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
def reverse_bisect_right(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x > a[mid]:
            hi = mid
        else:
            lo = mid+1
    return lo
def reverse_bisect_left(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x >= a[mid]:
            hi = mid
        else:
            lo = mid+1
    return lo
def get_list():
    return list(map(int,input().split()))
def get_str_list_in_int():
    return [int(i) for i in list(input())]
def get_str_list():
    return list(input())
def get_map():
    return map(int,input().split())
def get_int():
    return int(input())
def matrix(a,b):
    return [[0 for i in range(b)] for j in range(a)]
def swap(a,b):
    return b,a
def get_gcd(l):
    a=l[0]
    for i in range(len(l)):
        a=gcd(a,l[i])
    return a;
nc="NO"
yc="YES"
ns="No"
ys="Yes"
# t=get_int()
t=1;
for i in range(t):
    r,c=get_map();
    if r==1 and c==1:
        print("0")
    elif r<c:
        l=matrix(r,c)
        for i in range(r):
            for j in range(c):
                a=i+1;
                b=r+c-j;
                l[i][j]=a*b;
        for i in l:
            print(*i)
    else:
        l=matrix(r,c)
        for i in range(r):
            for j in range(c):
                a=j+1;
                b=r+c-i;
                l[i][j]=a*b;
        for i in l:
            print(*i)

