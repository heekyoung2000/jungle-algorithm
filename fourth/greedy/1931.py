from sys import stdin as s
from collections import deque

s=open("input.txt","rt")

n=int(s.readline()) # 회의 수
time_list=[]
L=[0]
k=0
for i in range(n):
    start,end=map(int,s.readline().split())
    time_list.append([end,start])

time_list.sort()

for i in range(1,n):
    if time_list[i][1]>=time_list[k][0]:
        L.append(i)
        k=i

print(len(L))    
