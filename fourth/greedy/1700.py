# 멀티탭 
from sys import stdin as s

s=open("input.txt","rt")
n,k=map(int,s.readline().split())
muti_list=list(map(int,s.readline().split()))
muti_tap=[0]*n
ans=0
maximum=0
while muti_list:
    print(muti_list,muti_tap)
    product = muti_list[0]
    #멀티탭에 같은 번호가 꽂혀져 있으면 그냥 무시 멀티 리스트에서 제거
    if product in muti_tap: 
        muti_list.remove(product) #이미 멀티탭에 꽂혀 있으니 제품 사용 순서 리스트에서 삭제
        continue
    # 멀티탭에 빈자리가 있을 경우 -> 빈자리에 해당 제품을 꽂는다.
    elif 0 in muti_tap: 
        muti_tap[muti_tap.index(0)]=product
        muti_list.remove(product)
    # 멀티탭에 빈자리가 없을 경우
    else:
        for mt in muti_tap:
            #멀티탭에 꽂혀있는 제품 중 이후에 꽂는 제품이 없을 경우
            #이중 꽂는 제품이 없는 제품을빼주고 탐색중인 제품을 꽂는다.
            if mt not in muti_list:
                change=mt
                break
            
            # 멀티 탭에 꽂혀있는 제품 중 가장 나중에 사용하는 제품을 고름
            # 가장 나중에 사용하는 제품을 뽑고 탐색하고 있는 제품을 꽂는다.
            elif muti_list.index(mt) > maximum:
                maximum = muti_list.index(mt)
                change=mt
                
        muti_tap[muti_tap.index(change)]=product
        muti_list.remove(product)
        maximum=0
        ans+=1
        
        
print(ans)