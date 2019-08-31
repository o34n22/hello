#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:07:02 2019

@author: mig
"""
import random as rd


def pose():
    """
    produces two numbers to be added together
    """
    top = 10
    increment = 0.1    
    a = rd.randint(0,top)
    b = rd.randint(0,top)
    return increment*a,increment*b

def solve(a,b):
    return a + b