from sys import stdin as s
from collections import deque
s=open("input.txt","rt")
n=int(s.readline())
import heapq
list1=[]


list1 = [list(map(int,s.readline().split())) for _ in range(n)]
list1.sort(key=lambda x:(x[1],x[2],x[0]))
lectureroom=[]
lectureroomCheck=[0 for _ in range(n+1)]
newroom=2

heapq.heappush(lectureroom,[list1[0][2],1]) #list1[0][2],1 : list1의 끝나는 시간과 강의실 번호 1을 lectureroom에 넣어줌
lectureroomCheck[list1[0][0]]=1 #list1[0][0] = 
for lecture in list1[1:]: #list에서 강의목록을 하나씩 체크한다.
    if lectureroom[0][0] <= lecture[1]: # 강의의 시작시간보다 끝나는 시간이 작을 경우
        _,curroom = heapq.heappop(lectureroom) #현재 룸과 배열을 pop해준다.
        lectureroomCheck[lecture[0]]=curroom #roomcheck 배열에 현재 룸번호를 넣는다.
        heapq.heappush(lectureroom,[lecture[2],curroom]) #끝나는 시간과 현재 룸번호를 넣어준다.
    else:# 만약 강의의 시작시간보다 끝나는 시간이 더 길면
        lectureroomCheck[lecture[0]]=newroom #새로운 room번호인 2를 넣어준다.
        heapq.heappush(lectureroom,[lecture[2],newroom]) #끝나는 시간과 새로운 room 번호를 저장한다.
        newroom+=1 #newroom에 번호 추가
print(len(lectureroom))
print(*lectureroomCheck[1:])

# while len(L)!=len(list1):
#     for i in range(len(list1)):
#         if list1[i][1]>=list1[k][2]: #다음 시작시간 보다 전 끝나는 시간이 작을때
#             L.append(list1[i])
#             k=i
#     count+=1
#     print(L)

