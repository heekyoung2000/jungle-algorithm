#python 함수 sort로 풀기
n=int(input())
list1=[]
for i in range(n):
    number=int(input())
    list1.append(number)

list1.sort()
for j in list1:
    print(j)
    
#퀵정렬로 사용하기->9개 미만이면 단순 삽입 정렬이 더 빠름
'''def insertion_sort(list1):
    for i in range(1,n):
        j=i
        tmp=list1[i]
        while j>0 and list1[j-1]>tmp:
            list1[j]=list1[j-1] # 큰값을 뒤에 저장
            j-=1
        list1[j]=tmp #작은 값을 앞에 저장

n=int(input())
list1=[]
for i in range(n):
    number=int(input())
    list1.append(number)

insertion_sort(list1)
for j in list1:
    print(j)'''

#퀵정렬로 풀어보기
def quick_sort(list1,left,right):
    pl=left #왼쪽 커서
    pr=right #오른쪽 커서
    x=(left+right)//2
    
    while pl<=pr:
        while list1[pl] < list1[x]:
            pl+=1 # pivot보다 작은 수 일경우 오른쪽으로 한칸 이동
        while list1[pr] > list1[x]:
            pr-=1 #pivot보다 큰 수 일경우 왼쪽으로 한칸 이동
        if pl<=pr:
            list1[pl],list1[pr]=list1[pr],list1[pl]
            pl+=1
            pr-=1
    if left < pr:
        quick_sort(list1,left,pr)
    if pl < right:
        quick_sort(list1,pl,right)            
            
    
n= int(input())
list1=[]
for i in range(n):
    number=int(input())
    list1.append(number)
quick_sort(list1,0,len(list1)-1)
for j in list1:
    print(j)

#틀렸다는데 뭐가 틀렸지...?
    


    
    
