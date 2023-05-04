from sys import stdin as s
from collections import deque
s=open("input.txt","rt")
n=int(s.readline())

# 첫번 쨰 방법 실패
# dp= list(map(int,s.readline().split()))
# i=0
# count=0
# while i<n:
#     cost=dp[i]
#     #옆으로 이동할 수 없으므로 break 해줌
#     if cost==0:
#         break
#     if i+cost<=n:
#         count=1
#         for j in range(i,cost+1):
#             cost=max(dp[i],dp[j])
#             i=dp.index(cost)
#         i+=cost
#         count+=1
#     # i+cost <=n:
#     #     i = i+cost
#     #     if dp[i-1]>dp[i]:
#     #         i=i-1
#     #     count+=1
#     elif i+cost> n:
#         cost= n-i
#         i=cost+i
#         count+=1
    
# if i==n:
#     print(count)
# else:
#     print(-1)
#         #오른쪽 끝으로 갈 수 없는 경우 -1
        
# 2번째 방법 dp 설정
dp=[n+1]*n
dp[0]=0
print(dp)
cost_list = list(map(int,s.readline().split()))
for i in range(n):
    for j in range(1,cost_list[i]+1):
        if i+j >=n:
            break
        dp[i+j]=min(dp[i+j],dp[i]+1)
print(dp)
print(dp[n-1] if dp[n-1] != n+1 else -1)
        
        

