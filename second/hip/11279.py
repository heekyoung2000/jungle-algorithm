# x가 자연수 : 배열에 x 값 추가 
# x가 0이라면 배열에서 가장 큰 값 출력하고 그 값을 배열에서 제거
from sys import stdin as s
import heapq


s=open("input.txt",'rt')
n=int(s.readline())

hq = []

def heap(a):
    if a==0:
        if len(hq)==0:
            print(0)
        else:
            print(heapq.heappop(hq)[1])#마이너스를 붙임으로써 작은 숫자부터 출력
    elif a!=0:
        heapq.heappush(hq,(-a,a)) #마이너스 값과 일반 값을 둘다 저장
        print(hq)
        
    return

for i in range(n):
    number = int(s.readline())
    heap(number)