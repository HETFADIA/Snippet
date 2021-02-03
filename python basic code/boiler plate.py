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
def swap(a,b):
    return b,a
def get_gcd():
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
    n=get_int();
    l=get_list();
    dict=Counter(l)
    friend=1;
    arr=[]
    repeted_arr=[]
    for i in range(n):
        if not l[i]:
            arr.append(i)
            while friend in dict:
                friend+=1
            if friend==i+1:
                repeted_arr.append(i)
            dict[friend]=1
            l[i]=friend
    if len(repeted_arr)==1:
        index1=repeted_arr[-1]
        the_index=0
        index2=arr[the_index]
        while index2==index1:
            the_index+=1
            index2=arr[the_index]
        l[index1],l[index2]=swap(l[index1],l[index2])
    else:
        for index in range(len(repeted_arr)-1):
            l[repeted_arr[index]],l[repeted_arr[index+1]]=l[repeted_arr[index+1]],l[repeted_arr[index]]
    print(*l)
