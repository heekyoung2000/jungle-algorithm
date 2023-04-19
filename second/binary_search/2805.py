#이코테 떡볶이 문제와 같은 문제

from sys import stdin as s


def binary_search(list,start,end,m):
    while start<=end:
        result=0
        mid=(start+end)//2
        for i in list:
            if i>mid:
                result+=(i-mid)
            else:
                result+=0
            if result>m:
                break
        if result<m:
            end=mid-1
        elif result>=m:
            start=mid+1
            

    print(end)
    
'''def binary_search(list,start,end,m):
    while start<=end:
        mid=(start+end)//2
        for i in list:
            if i>list[mid]:
                result+=(i-list[mid])
            else:
                result+=0
        if result==m:
           print(list[mid])
           break
        elif result<m:
            end-=1
        else:
            start+=1'''
        

s=open("input.txt","rt")
n,m=map(int,s.readline().split())
height_list=sorted(list(map(int,s.readline().split())))
binary_search(height_list,0,max(height_list),m)