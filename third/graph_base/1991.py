from sys import stdin as s
from collections import deque

class Node: #이진 탐색 트리를 구현하기 위해선 node 클래스를 장의해야함 이 떄 노드값과 왼쪽 오른 쪽 노드를 설정
    def __init__(self,data,left_node,right_node):
        self.data=data
        self.left_node=left_node
        self.right_node = right_node


#전위 순회(preorder)        
def pre_order(node):
    print(node.data,end='') #루트 노드를 먼저 설정해주고 출력함
    if node.left_node !=None: # 탐색하는 노드의 left node가 있을 경우 다시 탐색
        pre_order(tree[node.left_node])
    if node.right_node !=None: #탐색하는 노드의 right node 가 있을 경우 다시 탐색
        pre_order(tree[node.right_node])
#중위 순회(inorder)
def in_order(node): 
    if node.left_node !=None:
        in_order(tree[node.left_node])
    print(node.data, end='') #제일 왼쪽에 있는 노드를 출력함
    if node.right_node !=None:
        in_order(tree[node.right_node])
# 후위 순회(post-order)
def post_order(node):
    if node.left_node !=None:
        post_order(tree[node.left_node])
    if node.right_node !=None:
        post_order(tree[node.right_node])
    print(node.data, end='') #가장 마지막에 있는 노드를 출력       
            
s=open('input.txt','rt')
n = int(s.readline())
tree ={}

for i in range(n):
    data,left_node, right_node = (s.readline().split())
    if left_node == ".":
        left_node = None
    if right_node ==".":
        right_node = None
    tree[data] = Node(data,left_node,right_node) #tree에 기준이 되는 값과 오른쪽 노드 값, 왼쪽 노드값을 저장
    
        
pre_order(tree['A']) #먼저 시작하는 노드의 값을 지정해줌(항상 A가 루트 노드 조건)
print()
in_order(tree['A'])
print()
post_order(tree['A'])

#클래스 노드를 지정해줌
#전위 중위 후위 순으로 함수를 지정
#기준이 되는 값과 왼쪽 노드, 오른쪽 노드를 입력받아 tree에 저장한다.
#루트 노드는 A로 지정되어 있으므로 tree의 A부터 탐색을 시작한후 출력한다.

class Node:
    def __init__(self,data,left_node, right_node):
        self.data=data
        self.left_node=left_node
        self.right_node =right_node
        
def pre_order(node):
    print(node.data,end='')
    if node.left_node !=None:
        pre_order(tree[node.left_node])
    if node.right_node !=None:
        pre_order(tree[node.right_node])
    
def in_order(node):
    if node.left_node !=None:
        in_order(tree[node.left_node])
    print(node.data,end='')
    if node.right_node != None:
        in_order(tree[node.right_node])
        
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data,end='')
        
s=open('input.txt','rt')
n = int(s.readline())
tree ={}

for i in range(n):
    data,left_node, right_node = s.readline().split()
    if left_node=='.':
        left_node = None
    if right_node=='.':
        right_node=None
    tree[data] = Node(data,left_node,right_node)
    
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
