from sys import stdin as s
from collections import deque
s=open("input.txt","rt")
T=int(s.readline())



#테스트 케이스, 동전 가지 수 n가지 동전의 각 금액, 총 금액
for i in range(T):
    n=int(s.readline())
    coin_list=list(map(int,s.readline().split()))
    total = int(s.readline())
    
    DP = [[0 for _ in range(total+1)] for _ in range(n) ]
    
    for i in range(n):
        for j in range(total+1):
            DP[i][0]=1
            if i==0 and j!=0:
                if j%coin_list[i]==0:
                    DP[i][j]=1
            else:
                if coin_list[i]<=j:
                    coin=coin_list[i]
                    DP[i][j]=DP[i][j-coin]+DP[i-1][j]
                else:
                    DP[i][j]=DP[i-1][j]
    print(DP[n-1][total])

