from sys import stdin as s
from collections import deque
s=open("input.txt","rt")
n,m=map(int,s.readline().split())
small_list=set()

for _ in range(m):# 크기가 작은 돌들의 번호
    a=int(s.readline().strip())
    small_list.add(a)


dp = [[10001]*(int((2*n)**0.5)+2) for _ in range(n+1)]

dp[1][0] =0 
for i in range(2,n+1):
    if i in small_list:
        continue
    for v in range(1,int((2*i)**0.5)+1):
        dp[i][v] = min(dp[i-v][v-1], dp[i-v][v],dp[i-v][v+1])+1
        
ans = min(dp[n])
if ans == 10001:
    print(-1)
else:
    print(ans)
        

