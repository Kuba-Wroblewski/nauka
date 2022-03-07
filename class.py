#!/usr/bin/python3

def yieldPresentation(a):
    yield a
    a += 1
    yield a
    a += a
    yield a
    a *= a
    yield a


for i in yieldPresentation(5):
    print(i, end='\t');
print('\n\n', list(yieldPresentation(5)))
