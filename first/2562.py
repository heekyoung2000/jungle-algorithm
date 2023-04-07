#list1 = list(map(int,input().split('\n')))
#왜안되는 지 모르겠음

list1=[]
for i in range(9):
    a= int(input())
    list1.append(a)
    
print(max(list1))
print(list1.index(max(list1))+1)