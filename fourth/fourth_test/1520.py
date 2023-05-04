from sys import stdin as s
from collections import deque
s=open("input.txt","rt")
m,n=map(int,s.readline().split())

result=[]
for i in range(m):
    list1=list(map(int,s.readline().split()))
    result.append(list1)
dp=[[-1 for _ in range(n)] for _ in range(m)] #dp를 -1값으로 채워줌
dx=[0,0,1,-1]
dy=[1,-1,0,0]
dp[m-1][n-1]= 1 #마지막 목표 값을 1로 설정해줌

def dfs(row,col):
    for i in range(4):
        newx=row+dx[i]
        newy=col+dy[i]
        if 0<=newx<m and 0<=newy<n and result[newx][newy]<result[row][col]:#다음 방문할 좌표가 현재 좌표보다 높이(값)이 작을경우
            if dp[newx][newy] == -1: #만약 방문한 좌표가 방문한 적이 없다면
                dp[newx][newy] =0 # 방문표시로 0으로 만들어 주고
                dfs(newx,newy) #dfs를 돌아줌 이때 상하좌우로 돌아주고 다시 값 찾기
                dp[row][col] += dp[newx][newy] #방문한 dp 값 누적합으로 저장하기
            else:
                dp[row][col] += dp[newx][newy] #방문한 dp 값 누적합으로 저장하기

dp[0][0]=0
dfs(0,0)
print(dp[0][0])
    


            
            


