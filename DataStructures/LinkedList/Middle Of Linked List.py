from os import *
from sys import *
from collections import *
from math import *

'''

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

'''
def findMiddle(head):
    # Write your code here
    c=0
    k = head
    middleNodePos = giveMeCount(head) // 2
    while  c < middleNodePos:
        k = k.next
        c += 1
    return k

def giveMeCount(head):
    k1 = head
    cnt = 0
    while k1 != None:
        cnt += 1
        k1 = k1.next
    return cnt