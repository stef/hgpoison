#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from random import choice

import homoglyphs as hg

verbose = False
classes = 'LATIN', 'CYRILLIC','GREEK', 'COPTIC'

if '-v' in sys.argv:
    verbose=True
    del sys.argv[sys.argv.index('-v')]

if '-c' in sys.argv:
    idx = sys.argv.index('-c')
    del sys.argv[idx]
    classes = sys.argv[idx]
    del sys.argv[idx]
    classes = classes.upper().split(',')

if len(sys.argv)<2:
    print("usage: %s [-c <latin,cyrillic,coptic,greek,...>] string" % sys.argv[0])
    sys.exit(0)

homoglyphs = hg.Homoglyphs(categories=(classes))

total = 1
res = []
for a in ' '.join(sys.argv[1:]):
    c = homoglyphs.get_combinations(a) or [a]
    total*=len(c)
    res.append(choice(c))
print(''.join(res))
if verbose: print("total combinations:", total)
