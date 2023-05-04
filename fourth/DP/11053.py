from sys import stdin as s
from collections import deque
s=open("input.txt","rt")


n=int(s.readline())
list1=list(map(int,s.readline().split()))

count=1
now=list1[0]
DP=[1]*(n+1)
for i in range(0,n):
    for j in range(0,i):
        if list1[i]>list1[j]: #끝점을 기준으로 끝점보다 작은 값이 있으면 dp에 추가
            DP[i]=max(DP[i],DP[j]+1)
        
print(max(DP))