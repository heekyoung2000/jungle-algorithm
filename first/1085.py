import sys

x,y,w,h=map(int, sys.stdin.readline().split())

if w-x<x:
    if h-y<y:
        if h-y<w-x:
            print(h-y)
        else:
            print(w-x)
    else:
        if y<w-x:
            print(y)
        else:
            print(w-x)
else:
    if h-y<y:
        if h-y<x:
            print(h-y)
        else:
            print(x)
    else:
        if y<x:
            print(y)
        else:
            print(x)

