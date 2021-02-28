from collections import defaultdict,OrderedDict,Counter
from sys import stdin,stdout
from bisect import bisect_left,bisect_right
# import numpy as np
from queue import Queue,PriorityQueue
from heapq import heapify,heappop,heappush
from statistics import median,mean
from math import gcd,sqrt,floor,factorial,ceil,log2,log10,log
import fractions
import copy
from copy import deepcopy
import sys
import io
sys.setrecursionlimit(10**8)
import math
import os
import bisect
import collections
mod=pow(10,9)+7
import random
from random import random,randint,randrange
from time import  time;
def ncr(n, r, p=mod):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den,
            p - 2, p)) % p
def normalncr(n,r):
    r=min(r,n-r)
    count=1;
    for i in range(n-r,n+1):
        count*=i;

    for i in range(1,r+1):
        count//=i;
    return count

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
# SieveOfEratosthenes(a9)
# prime_number=[]
# for i in range(2,a9):
#     if prime[i]:
#         prime_number.append(i)
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
def input_int():
    return int(input())
def matrix(a,b):
    return [[0 for i in range(b)] for j in range(a)]
def swap(a,b):
    return b,a
def find_gcd(l):
    a=l[0]
    for i in range(len(l)):
        a=gcd(a,l[i])
    return a;
def is_prime(n):
    sqrta=int(sqrt(n))
    for i in range(2,sqrta+1):
        if n%i==0:
            return 0;
    return 1;
def prime_factors(n):
    sqrta = int(sqrt(n))
    for i in range(2,sqrta+1):
        if n%i==0:
            return [i]+prime_factors(n//i)
    return [n]
def p(a):
    if type(a)==str:
        print(a+"\n")
    else:
        print(str(a)+"\n")
def ps(a):
    if type(a)==str:
        print(a)
    else:
        print(str(a))
def kth_no_not_div_by_n(n,k):
    return k+(k-1)//(n-1)
def forward_array(l):
    stack = []
    forward=[0]*n
    for i in range(len(l) - 1, -1, -1):
        while len(stack) and l[stack[-1]] < l[i]:
            stack.pop()
        if len(stack) == 0:
            forward[i] = len(l);
        else:
            forward[i] = stack[-1]
        stack.append(i)
    return forward;
def backward_array(l):
    stack = []
    backward=[0]*n
    for i in range(len(l)):
        while len(stack) and l[stack[-1]] < l[i]:
            stack.pop()
        if len(stack) == 0:
            backward[i] = -1;
        else:
            backward[i] = stack[-1]
        stack.append(i)
    return backward
nc="NO"
yc="YES"
ns="No"
ys="Yes"

# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# input=stdin.readline
# print=stdout.write


t=int(input())
for i in range(t):
    n=int(input())
    l=get_list();
    dict=defaultdict(int)
    forward=forward_array(l)
    backward=backward_array(l)
    for i in range(n):
        j=forward[i]
        if j!=n:
            dict[l[j]-l[i]]=1
    for i in range(n):
        j=backward[i]
        if j!=-1:
            dict[l[j]-l[i]]=1
    print(len(dict))



