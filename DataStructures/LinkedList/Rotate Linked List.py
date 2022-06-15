class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def countLenth(k):
    c = 0
    while k != None:
        c += 1
        k = k.next
    return c

def rotate(head, k):
    if k == 0:
        return head
    
    lenth = countLenth(head)
    # Suppose k = 8 & lenth = 3, then What no. of actual(minimum) k ?
    # 8 % 3 = 2 (means if rotate list 8 time or 2 time, ANS will same!)
    k = k % lenth  if k > lenth else k
    if lenth == k:
        return head


    last, tmp = head, None
    count = 0
    while last.next != None:
        #print(last.data)
        if count == lenth - k-1:
            tmp = last
        count += 1
        last = last.next
        
    last.next = head
    head = tmp.next
    tmp.next = None
    
    return head