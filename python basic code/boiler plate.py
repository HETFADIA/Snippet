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


class MaxHeap:

    def __init__(self, maxsize):

        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):

        return pos // 2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):

        return 2 * pos

        # Function to return the position of

    # the right child for the node currently
    # at pos
    def rightChild(self, pos):

        return (2 * pos) + 1

    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):

        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):

        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],
                                            self.Heap[fpos])

        # Function to heapify the node at pos

    def maxHeapify(self, pos):

        # If the node is a non-leaf node and smaller
        # than any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
                    self.Heap[pos] < self.Heap[self.rightChild(pos)]):

                # Swap with the left child and heapify
                # the left child
                if (self.Heap[self.leftChild(pos)] >
                        self.Heap[self.rightChild(pos)]):
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))

                    # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

                    # Function to insert a node into the heap

    def insert(self, element):

        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while (self.Heap[current] >
               self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

            # Function to print the contents of the heap

    def Print(self):

        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) +
                  " LEFT CHILD : " + str(self.Heap[2 * i]) +
                  " RIGHT CHILD : " + str(self.Heap[2 * i + 1]))

            # Function to remove and return the maximum

    # element from the heap
    def extractMax(self):

        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)

        return popped
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
nc="NO"
yc="YES"
ns="No"
ys="Yes"
t=1;
# t=input_int()
for i in range(t):
    n=input_int()
    if is_prime(n):
        print(n)
        continue
    fac=prime_factors(n)
    dict=Counter(fac)
    lena=len(dict)
    if len(dict)>1:
        print(1)
    else:
        print(list(dict)[0])


