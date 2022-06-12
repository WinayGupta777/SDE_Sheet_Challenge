
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __del__(self):
        if(self.next):
            del self.next


def addTwoNumbers(h1, h2):
    # Write your code here.
    carry = 0
    p1,p2 = h1,h2
    headNew = None
    while (p1 != None) and (p2 != None):
        sumOf2 = p1.data + p2.data + carry
        val = sumOf2 % 10
        carry = sumOf2 // 10
        if not headNew:
            headNew =k1 = Node(val)
        else:
            tmp = Node(val)
            k1.next = tmp
            k1 = k1.next
        p1 = p1.next
        p2 = p2.next
    
    if p1:
        while p1 != None:
            sumOf1 = carry + p1.data
            carry = sumOf1 // 10
            val = sumOf1 % 10
            tmp = Node(val)
            k1.next = tmp
            k1 = k1.next
            p1 = p1.next
    elif p2:
        while p2!=None:
            sumOf1 = carry + p2.data
            carry = sumOf1 // 10
            val = sumOf1 % 10
            tmp = Node(val)
            k1.next = tmp
            k1 = k1.next
            p2 = p2.next

    if carry:
        tmp = Node(carry)
        k1.next = tmp
        k1 = k1.next
        
    return headNew