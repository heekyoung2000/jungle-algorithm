#하노이 탑
#no: 원반의 갯수, x: 시작 기둥의 번호, y: 목표 기둥의 번호

'''def move(no,x: int,y:int):

    if no > 1:
        move(no-1,x,6-x-y)
        print(f'{x} {y}')
        move(no-1,6-x-y,y)
        오류 코드
        
no= int(input())
print(2**no-1) #이동횟수 출력 
if no<=20:
    move(no,1,3)
'''
#no: 원반의 갯수, x: 처음 시작하는 고리, y: 목표하는 고리
def move(no, x,y):
    if no>1:
        move(no-1,x,6-x-y)
    print(f'{x} {y}')
    if no>1:
        move(no-1,6-x-y,y)
    
no = int(input())
print(2**no-1) #원반의 총 개수
if no<=20:
    move(no,1,3)
   
   

        
    



