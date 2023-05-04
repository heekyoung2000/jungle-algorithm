from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)
s=open("input.txt","rt")

class Node:
    def __init__(self,data,left_node,right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

n=int(s.readline())
tree={}
for i in range(n):
    node, left_node, right_node = map(str,s.readline().split())
    if left_node==".":
        left_node =  None
    if right_node ==".":
        right_node = None
    tree[node] = Node(node,left_node,right_node)
    
