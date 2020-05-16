class node():
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 
    
    def insert(self,val):
        if self.val:
            if val < self.val:
                if self.left == None:
                    self.left = node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right == None:
                    self.right = node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

def inorder(root, res):
    # Recursive travesal 
    if root:
        inorder(root.left,res)
        res.append(root.val)
        inorder(root.right,res)

def treesort(arr):
    # Build BST
    if len(arr) == 0:
        return arr
    root = node(arr[0])
    for i in range(1,len(arr)):
        root.insert(arr[i])
    # Traverse BST in order. 
    res = []
    inorder(root,res)
    return res

print(treesort([3,1,9,0,2,11]))


Tracing:

inorder(3,[])
inorder(1,[])
inorder(0,[])
inorder(None,[])
inorder(None,[0])
inorder(2,[0,1])
inorder(None,[0,1])
inorder(None,[0,1,2])
inorder(9,[0,1,2,3])
inorder(None,[0,1,2,3])
inorder(11,[0,1,2,3,9])
inorder(None,[0,1,2,3,9])
inorder(None,[0,1,2,3,11])
