class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseLinkedList(head):
    if head == None:
        return
        
    now = head
    prev = None
    final = None
        
    while now != None:
        nxt = now.next
        if nxt == None:
            final = now
        now.next = prev
            
        prev = now
        now = nxt
    return final