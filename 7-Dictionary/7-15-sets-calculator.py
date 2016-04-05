#!/usr/bin/env python

def issubset(set1, set2):
    return set1.issubset(set2)
def issuperset(set1, set2):
    return set1.issuperset(set2)
def union(set1, set2):
    return set1 | set2
def intersection(set1, set2):
    return set1 & set2
def difference(set1, set2):
    return set1 - set2
def symmetric_difference(set1, set2):
    return set1 ^ set2

set1 = set(['aa',123,'bb'])
set2 = set(['aa',456])

# ^, <, <=, >, >=, ==, !=
ops = {'sub':issubset, 'super':issuperset, '|':union, '&':intersection, '-':difference, '^':symmetric_difference}

for op in ops:
    print op, ops[op](set1, set2)
