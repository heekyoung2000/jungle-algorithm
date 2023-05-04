from sys import stdin as s
from collections import deque
s=open("input.txt","rt")

a=(s.readline().strip())
b=(s.readline().strip())
count=0
table = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1) ]

print(table)
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1] == b[j-1]:
            table[i][j]=table[i-1][j-1]+1
        else:
            table[i][j]=max(table[i-1][j],table[i][j-1])

print(table[len(a)][len(b)])   
