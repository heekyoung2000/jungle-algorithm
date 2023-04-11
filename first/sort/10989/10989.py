#메모리 초과 오류남 -> https://www.acmicpc.net/board/view/26132
#모든 입력을 배열에 저장했기 떄문에 메모리 초과남
#sys.stdin.readline()을 사용해야지 메모리 초과가 안남
'''import sys
n=int(sys.stdin.readline())
new_list=[]
for i in range(n):
    number=int(sys.stdin.readline())
    new_list.append(number)
new_list.sort()

for j in new_list:
    print(j)
        '''
'''import sys
       
def sort(list1):
    if len(list1)<2:
        return list1
    mid = len(list1)//2
    left = sort(list1[:mid])
    right = sort(list1[mid:])
    
    return merge_sort(left,right)

def merge_sort(left,right):
    a=0 #left
    b=0 #right
    new_list=[]
    while a<len(left) and b<len(right):
        if left[a]>right[b]:
            new_list.append(right[b])
            b+=1
        elif left[a]<right[b]:
            new_list.append(left[a])
            a+=1
    while a<len(left):
        new_list.append(left[a])
        a+=1
    while b<len(right):
        new_list.append(right[b])
        b+=1
        
    return new_list

n=int(input())
list1=[0]
for i in range(n):
    number=int(sys.stdin.readline())
    list1.append(number) 

for j in sort(list1):
    print(j)'''

import sys

#계수정렬을 사용해야지 메모리 초과가 안남 -> list1 전체를 받아줘서 메모리 초과남

def count_star(n,count):
    for i in range(n):
        count[int(sys.stdin.readline())]+=1
        
    for i in range(len(count)):
        for _ in range(count[i]):
            print(i)

n=int(sys.stdin.readline())
count =[0]*10001
count_star(n,count)






