class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pos = []

    def __del__(self):
        if (self.next):
            del self.next


def firstNode(head):

    # visited node's address will be stored !
    visited = []
    while head != None:
        #print(head.data)
        if head in visited:
            return head
        visited.append(head)
        head = head.next






