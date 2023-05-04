import sys
import heapq

sys.stdin = open("input.txt", "rt")

N = int(sys.stdin.readline())
lectures = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lectures.sort(key=lambda x:(x[1],x[2], x[0]))
lectureRoom = []
lectureRoomCheck =[0 for _ in range(N+1)]
print(lectures)
newroom = 2
heapq.heappush(lectureRoom,[lectures[0][2],1])
lectureRoomCheck[lectures[0][0]] = 1
for lecture in lectures[1:]:
    if lectureRoom[0][0] <= lecture[1]:
        _ ,curroom=heapq.heappop(lectureRoom)
        lectureRoomCheck[lecture[0]] = curroom
        heapq.heappush(lectureRoom, [lecture[2], curroom])
    else:
        lectureRoomCheck[lecture[0]] = newroom
        heapq.heappush(lectureRoom, [lecture[2], newroom])
        newroom+=1
print(lectureRoomCheck)
print(len(lectureRoom))
print(*lectureRoomCheck[1:])