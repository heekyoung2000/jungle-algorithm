from sys import stdin as s

#선형 탐색
'''def distance(n):
    result=[]
    end=1
    current_num=100
    for start in range(n):
        while end<n:
            interval_sum=0
            interval_sum+=list1[start]+list1[end]
            if abs(interval_sum)<current_num:
                current_num=abs(interval_sum)
                result.append((current_num, list1[start],list1[end]))
            end+=1
            #print(end,interval_sum)
        if end==n:
            end=start+2
    print(result)
    mini=min(result)
    print(f'{mini[1]} {mini[2]}')'''

'''result=[]
def distance(list1):
    start=0
    end=n-1
    target=abs(list1[start]+list1[end])
    target_left=start
    target_right = end
    while start<end:
        if abs(list1[start]+list1[end])<target:
            target_left=start
            target_right=end
            target = abs(list1[start]+list1[end])
        if list1[start]+list1[end]<0:
            end-=1
        else:
            start+=1
    print(f'{list1[target_left]} {list1[target_right]}')'''
    

def distance(list1):
    print(list1)
    start=0
    end=n-1
    target = abs(list1[start]+list1[end])
    final = [list1[start],list1[end]]
    #target_left=start
    #target_right=end
    
    while start<end:
        left_val =list1[start]
        right_val = list1[end]
        sum=left_val+right_val
        if abs(sum)<target:
            target=abs(list1[start]+list1[end])
            final=[left_val, right_val]
            if target==0:
                break
        if sum<0:
            start+=1
        else:
            end-=1
    print(f'{final[0]} {final[1]}')
            
            
            
s=open("input.txt","rt")
n=int(s.readline())
list1=sorted(list(map(int,s.readline().split())))
distance(list1)