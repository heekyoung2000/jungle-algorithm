#2차원 배열 생성 후 가로에는 최대 kg을, 세로에는 물건의 개수를 넣어준다.
#물건이 1개일 때 부터 4개 담을 때까지의 가치 합을 저장한다.
#이때 물건의 합이 7이하 이면 누적 가치합을 저장한다.

#0. 가치합을 저장할 테이블을 생성한다.
#0-1. 물건의 무게와 가치를 저장할 리스트를 생성해서 저장한다. 이때 가치합 테이블을 탐색할때 1부터 탐색을 할 것이므로 0,0을 넣은 리스트를 생성한다.
#1. weight에 stuff에 저장해놓은 무게를 저장, value에 stuff에 저장해놓은 가치를 저장 
#2. 만약 탐색하고 있는 테이블의 가로가 무게보다 작다면 그전 누적 기대값의 최대 값을 저장한다.
#3. 아니라면 물건을 넣은 뒤의 남은 무게를 채울 수 있는 최대값과 현재 가치값을 더한 값과 그전 누적 기대값의 최대값을 비교하여 큰 값을 저장한다.

from sys import stdin as s
from collections import deque
s=open("input.txt","rt")
n,k=map(int,s.readline().split())

table=[[0] *(k+1) for _ in range(n+1)]  

stuff = [[0,0]]
for i in range(n):
    w,v = map(int,s.readline().split())
    stuff.append([w,v])

for i in range(1,n+1):
    for j in range(1,k+1):
        weight=stuff[i][0]
        value = stuff[i][1]
        if j<weight:
            table[i][j]=table[i-1][j]
        else:
            table[i][j]=max(table[i-1][j],table[i-1][j-weight]+value)
print(table)            
print(table[n][k])
    