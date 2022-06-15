class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Doubly LinkedList Node
class DNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
head = tmp = None 
        
def BTtoDLL(root):
    global head,tmp
    head = tmp = None 
    return preOrder(root)



def preOrder(rootNode):
    global head,tmp
    
    # base-case
    if rootNode is None:
        return
    
    preOrder(rootNode.left)
    
    # Logic of creating DLL
    if not head:
        head = tmp = DNode(rootNode.data)
    else:
        new = DNode(rootNode.data)
        tmp.right = new
        new.left = tmp
        tmp = tmp.right
    # End of Logic
        
    preOrder(rootNode.right)
    
    return head
    