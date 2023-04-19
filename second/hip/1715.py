from sys import stdin as s
import heapq

hq=[]

def heap(hq):
    sum=0
    if len(hq)==1:
        print(0)
    else:
        while len(hq)>1:
            min1=heapq.heappop(hq)
            min2=heapq.heappop(hq)
            sum+=min1+min2
            heapq.heappush(hq,min1+min2)
        print(sum)

s=open("input.txt",'rt')
n=int(s.readline())

for i in range(n):
    num=int(s.readline())
    heapq.heappush(hq,num)
heap(hq)