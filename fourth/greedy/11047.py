from sys import stdin as s
from collections import deque
s=open("input.txt","rt")
n,k=map(int,s.readline().split())
coin_list=[]
for i in range(n):
    coin=int(s.readline())
    coin_list.append(coin)
count=0
for i in reversed(coin_list):
    if k>=i:
        count+=k//i
        k=k%i
        
        
print(count)
    
