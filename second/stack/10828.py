from sys import stdin as s
from collections import deque


new_list=[]
def stack(a):
    if a[0]=="push":
        new_list.append(a[1])
    elif a[0]=="top":
        if len(new_list)==0:
            print(-1)
        else:
            print(new_list[-1])
    elif a[0]=="size":
        print(len(new_list))
    elif a[0]=="empty":
        if len(new_list)==0:
            print(1)
        else:
            print(0)
    elif a[0]=="pop":
        if len(new_list)==0:
            print(-1)
        else:
            print(new_list.pop())       
        

s=open('input.txt','rt')
n = int(s.readline())

list1=[]
for i in range(n):
    no = list(map(str,s.readline().split()))
    stack(no)
