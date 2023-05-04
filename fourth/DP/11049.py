from sys import stdin as s
from collections import deque
s=open("input.txt","rt")
n=int(s.readline())

list1=[]
dp=[[0]*(n) for _ in range(n)]
for a in range(n):
    r,c=map(int,s.readline().split())
    list1.append([r,c])
result=0
for i in range(1,n):
    for j in range(n):
        if i+j==n:
            break
        dp[j][i+j]=int(1e9)
        for k in range(j,i+j):
            dp[j][i+j]=min(dp[j][i+j],dp[j][k]+dp[k+1][i+j]+list1[j][0]*list1[k][1]*list1[i+j][1])
            
        
print(dp[0][n-1])    