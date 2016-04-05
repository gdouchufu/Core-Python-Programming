#!/usr/bin/env python
from __future__ import division

def tran_F_to_C(F):
    C = (F - 32) * (5 / 9)
    return round(C, 2)

print tran_F_to_C(42)