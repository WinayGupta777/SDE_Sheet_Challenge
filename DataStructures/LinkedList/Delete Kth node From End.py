class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
        

def countLenth(head):
    lenth = 0
    while head != None:
        lenth += 1
        head = head.next
    return lenth

def removeKthNode(h1, n):
    
    if h1 == None:
        return
    
    lenthOfList = countLenth(h1)
    indexToRemoved = lenthOfList - n
    k = h1

    if n == lenthOfList:
        # remove first node
        h1 = h1.next if h1.next else None
        return h1
    
    elif n == 0:
        # nothing to do
        return h1

    else:
        for _ in range(0,indexToRemoved - 1):
            k = k.next
        # skip that node
        k.next = k.next.next
        
        return h1