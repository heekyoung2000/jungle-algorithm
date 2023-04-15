# ( 를 넣고 )가 나오면 가장 최근에 넣은 (  뺌
# 근데 )) 같은 경우는 cnt-=1 했을 때 음수가 나오므로 no
# ())(() 같은 경우에는 괄호가 닫혀지지 않으므로 안됨 
#따라서 CNT가 음수가 나오면 바로 NO 출력


from sys import stdin as s
from collections import deque
s=open('input.txt','rt')
n = int(s.readline())
dq=deque()


def a(no):
    cnt=0
    for i in range(len(no)):
        if no[i]=="(":
            cnt+=1
        else:
            cnt-=1
            if cnt<0:
                break
                
    if cnt==0:
        print("YES")
    else:
        print("NO")
        

for i in range(n):
    no = list(map(str,s.readline().strip()))
    a(no)
