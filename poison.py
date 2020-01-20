#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from random import choice

import homoglyphs as hg

res = []
classes = 'LATIN', 'CYRILLIC','GREEK', 'COPTIC'

if '-c' in sys.argv:
    idx = sys.argv.index('-c')
    del sys.argv[idx]
    classes = sys.argv[idx]
    del sys.argv[idx]
    classes = classes.upper().split(',')

homoglyphs = hg.Homoglyphs(categories=(classes))

total = 1
for a in ' '.join(sys.argv[1:]):
    c = homoglyphs.get_combinations(a) or [a]
    total*=len(c)
    res.append(choice(c))
print(''.join(res))
print("total combinations:", total)
