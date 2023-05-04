from sys import stdin as s
from collections import deque
s=open("input.txt","rt")
n=int(s.readline())
dp=[[0 for _ in range(n)] for _ in range(n)]

jump_list=[]
for _ in range(n):
    list1 = list(map(int,s.readline().split()))
    jump_list.append(list1)

dp[0][0]=1
for i in range(n):
    for j in range(n):
        if jump_list[i][j]:
            cost = jump_list[i][j] #jump할 수 있는 거리를 cost에 저장한다.
            if j+cost<n: #만약 가로줄 + cost를 했을 때 게임판을 넘어가지 않는다면
                dp[i][j+cost]+=dp[i][j] # 점프한 좌표에 원래 서있던 좌표의 값을 더해준다.
            if i+cost<n: #만약 세로줄 +cost를 했을 때 게임판을 넘어가지 않는다면
                dp[i+cost][j]+=dp[i][j] # 점프한 좌표에 원래 서있던 좌표의 값을 더해준다.

print(dp[n-1][n-1]) # 가장 오른쪽 아래 칸 좌표 값을 출력한다.
