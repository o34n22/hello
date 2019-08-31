#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 09:45:44 2019

fix:
what if there is a number with two nearest permutations?

@author: mig
"""

import random as rd
import numpy as np

def pose(target=500):
    """
    returns str
    (a random integer with same number of digits as target number)
    """
    while True:
        digits = len(str(target))
        n = 0
        for position in range(digits):
            place_value = 10**position
            n += place_value*rd.randint(0,9)
        if len(str(n)) == digits: 
            return str(n)

# to-do: catch type errors
def permutations(n):
    """
    takes some integer n as a str or int
    produces list of all permutations
    """
    if type(n) == int: n = str(n)
    digits = len(n)
    if digits == 0:
        return []
    elif digits == 1:
        return [n]
    else:
        L = [] 
        for i in range(digits): # gotta start from tail!
            for p in permutations(n[:i]+n[i+1:]):
                L.append(n[i] + p)
    return L

def solve(n,target=500):
    P = permutations(n)
    D = target*np.ones(len(P),dtype=int)
    j = 0
    j_min = 0
    for p in P:
        D[j] = abs(target - int(p))
        if D[j] < D[j_min]: j_min = j
        j+=1
    return P[j_min]


# --------------- testing ----------------


def make_n1():
    b = make_n()
    if b == find_nearest(b): 
        # more efficient: perform one random permutation
        b = rd.choice(permutations(b)[1:])
    return b

def play():
    b = make_n()
    if b == find_nearest(b): 
        b = rd.choice(permutations(b)[1:])
    print('Rearrange the digits of %s to get the nearest number to %d!' % (b,500))
    while True:
        ans = input('->')
        if ans == find_nearest(b):
            print('perfect')
            break
        elif ans not in permutations(b):
            print('Digits aren\'t matching. You must use the digits from \
                  the number above.')
    return None

#play()
#print(type(find_nearest('3876')))
