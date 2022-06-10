# Following is the linked list node structure:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sortTwoLists(first, second):
    # Write your code here.

    if first is None:
        return second
    if second is None:
        return first
    
    headNew = None
    while (first != None) and (second != None):
        if first.data >= second.data:
            if not headNew:
                headNew = new1 = Node(second.data)
            else:
                tmp = Node(second.data)
                new1.next = tmp
                new1 = new1.next
            second = second.next
        else:
            if not headNew:
                headNew = new1 = Node(first.data)
            else:
                tmp = Node(first.data)
                new1.next = tmp
                new1 = new1.next
            first = first.next
            
    if first:
        new1.next = first
    elif second:
        new1.next = second        

    return headNew