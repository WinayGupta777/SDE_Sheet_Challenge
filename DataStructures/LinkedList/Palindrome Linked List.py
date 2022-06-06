from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

#Following is the class structure of the LinkedListNode class:
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
            
            
def isPalindrome(head):
    # Write your code here.
    l1 = makeListOfValues(head)
    l2 = l1.copy()
    l1.reverse()
    if l1 == l2:
        return 1
    else:
        return 0
    
def makeListOfValues(k):
    dataValues=[]
    while k != None:
        #print(k.data)
        dataValues.append(k.data)
        k = k.next
    return dataValues
  

def takeinput():
    
    inputlist=[int(ele) for ele in input().split()]
    
    head=None
    tail=None
    
    for currentData in inputlist:
        
        if currentData == -1:
            break
        
        Newnode=Node(currentData)
        
        if head is None:
            head=Newnode
            tail=Newnode
        else:
            tail.next=Newnode
            tail=Newnode
            
    return head

#Main
t = int(stdin.readline().rstrip())

while t > 0:
    
    head = takeinput()
    
    if isPalindrome(head):
        print('true')
    else:
        print('false')
        
    t -= 1
