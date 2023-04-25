from sys import stdin as s
from collections import deque
import sys

#전위 순회는 첫번쨰 자리가 루트 노드 이고 왼쪽 노드, 오른쪽 노드 결과로 입력됨
# 따라서 후위순회는 왼쪽, 오른쪽 루트로 돌아가므로 재귀로 돌려줌

#recursion error
sys.setrecursionlimit(10000)
s=open('input.txt','rt')
postOrder=[]


    
def postorder(nums):
    if len(nums)==0: #배열이 비어 있다면 종료
        return
    if len(nums) ==1: #배열에 값이 하나만 있다면 출력한 후 종료
        print(nums[0])
        return
    idx = len(nums) #부모 노드를 기준으로 값이 커지는 순간의 인덱스
    for i in range(1,len(nums)):
        if nums[i]>nums[0]:
            idx=i
            break
    
    #왼쪽 자식 노드에 대하여 재귀 호출
    if idx >1:
        postorder(nums[1:idx])
    #오른쪽 자식 노드에 대하여 재귀 호출
    if idx< len(nums):
        postorder(nums[idx:])
    #부모 노드의 값 호출
    print(nums[0])
   
#입력에 대한 길이가 없어서 EOF로 입력 받는다.
        
if __name__ == '__main__':
    preOrder=[]
    while True:
        try: 
            num = int(s.readline())
            preOrder.append(num)
        except: break
    postorder(preOrder)


sys.setrecursionlimit(10**5)

s=open('input.txt','rt') ## 시간초과
class Tree:
    def __init__(self,value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def insert(self,value):#받아온 값을 value에 저장하고 기존의 루트노드 값과 비교
        if value < self.value: #만약 받아온 값이 루트 노드 보다 작다면 왼쪽에 위치해야 함
            if self.left_node == None:
                self.left_node= Tree(value) #트리에 left_node가 없으면 트리에 받아온 값을 저장
            else: # 만약 left_node에 값이 있으면 다시 탐색
                self.left_node.insert(value) 
        else: #받아온 값이 루트노드 보다 크다면 오른쪽에 위치해야 함
            if self.right_node == None: # right_node에 없다면 value 저장
                self.right_node = Tree(value)
            else: # 만약 값이 있다면 다시 탐색
                self.right_node.insert(value)
                
    #후위 순회 탐색
    def postOrder(self): # 왼쪽 -> 오른쪽 -> 뿌리
        if self.left_node !=None: # 왼쪽 노드가 값이 없을 때까지 탐색
            self.left_node.postOrder()
        if self.right_node !=None: #오른쪽 노드가 값이 없을 때 까지 탐색
            self.right_node.postOrder()
            
        print(self.value)
    
if __name__ == '__main__':
    preOrder=[]
    while True: #preOrder에 입력된 n이 끝날떄 까지 append 해주기 위해 while 문 사용
        try:
            n=int(s.readline())
            preOrder.append(n)
        except:
            break

    binaryTree = Tree(preOrder[0]) #tree에 value 값을 루트노드 값으로 설정

    for i in range(1,len(preOrder)):
        num=preOrder[i]
        binaryTree.insert(num)
    
    binaryTree.postOrder()