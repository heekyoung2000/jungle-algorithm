'''import sys



def sort(new_list):
    mid = len(new_list)//2
    left = new_list[:mid]
    right = new_list[mid:]
    merge_sort(left,right)
    
def merge_sort(left,right):
    a=0
    b=0
    list1=[]
    while a<len(left) and b<len(right):
        if len(left[a])> len(right[b]):
             list1.append(left[a])
             a+=1
        else:
            list1.append(right[b])
            b+=1
    while a<len(left):
        list1.append(left[a])
        a+=1
    while b<len(right):
        list1.append(right[b])
    
    return list1


n=int(sys.stdin.readline())
new_list=[]    
for i in range(n):
    word = str(sys.stdin.readline().strip())
    new_list.append(word)

for j in sort(new_list):
    print(j)'''

#1. key=lambda 함수를 사용할 생각을 못해서 못품->개념 익혀서 적용
#2. 중복 set 함수를 쓸때 list형식으로 다시 변환해주지 못해서 틀림
#3. 반복문을 잘못 돌려서 시간 초과남
import sys
    
n=int(sys.stdin.readline())
list1=[]
new_list=[]    
for i in range(n):
    word = str(sys.stdin.readline().rstrip())
    new_list.append(word)
list1 = list(set(new_list))
list1.sort(key=lambda x:len(x))
for i in list(list1):
    print(i)
    
import sys
    
n=int(sys.stdin.readline())
list1=[]
new_list=[]    
for i in range(n):
    word = str(sys.stdin.readline().strip())
    length= len(word)
    new_list.append([word,length])
list1 = set(list(map(tuple,new_list)))
new_list=list(list1)
new_list.sort(key=lambda new_list:(new_list[1],new_list))
for i in list(new_list):
    print(i[0])
    