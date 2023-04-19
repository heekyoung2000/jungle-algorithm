#최소힙

from sys import stdin as s
import heapq
s=open("input.txt",'rt')
n=int(s.readline())

hq=[]

def heap(number):
    if number==0:
        if len(hq)==0:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq,number)

for i in range(n):
    number=int(s.readline())
    heap(number)