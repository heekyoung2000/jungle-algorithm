#분배법칙을 이용한 문제로 재귀가 꼭 필요하다
from sys import stdin as s
s=open("input.txt",'rt')
a,b,c=map(int,s.readline().split())


def pow(a,b):
    if b==1:
        return a%c
    else:
        tmp = pow(a,b//2)
        if  b%2==0:
            return (tmp*tmp)%c
        else:
            return (tmp*tmp*a)%c

print(pow(a,b))