#2개를 제외하고 나머지를 더했을때 100이 되는 숫자 찾기
#9개에서 2개를 뽑아야 함
import sys
import random

def choose(list1):
    while True:
        out = random.sample(list1,7)
        if sum(out)==100:
            break
    return out
        
    
list1=[]
for i in range(9):
    list1.append(int(sys.stdin.readline()))
    
#2개를 뽑기
result=choose(list1)
result.sort()
for i in result:
    print(i)    
    
    
#내장함수 말고도 쓸수 있는 방법을 찾아볼 것