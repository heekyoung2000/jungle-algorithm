import heapq  # 우선순위 큐 구현을 위함
from sys import stdin as s

s=open("input.txt","rt")

n,m,h = map(int,s.readline().split()) #m은 상자의 가로칸 수, n은 상자의 세로칸 수, h: 상자의 수
totato_box=[]
for i in range(m):
    list1=list(map(int,s.readline().split()))
    totato_box.append(list1)
print(totato_box)
    



