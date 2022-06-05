from os import *
from sys import *
from collections import *
from math import *

# Following is the List Node Class
class LinkedListNode:
    def __init__(self, data):

        self.data = data
        self.next = None

    def __del__(self):
        if(self.next):
            del self.next

def deleteNode(node):
    # Write your code here.
    node.data = node.next.data
    node.next = node.next.next

    # Copying the next node's data in current node
    # then linking current node to next's next node