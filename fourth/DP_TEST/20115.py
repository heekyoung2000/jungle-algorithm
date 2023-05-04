from sys import stdin as s
from collections import deque
s=open("input.txt","rt")
n=int(s.readline())

drink_list=list(map(int,s.readline().split()))
maximum=max(drink_list)
drink_list.remove(maximum)
sum=0
for i in range(len(drink_list)):
    sum+=drink_list[i]/2
result=maximum + sum
print("{:g}".format(result)) #이거 몰라서 찾아봄