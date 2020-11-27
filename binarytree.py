class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        
class binarytree(object):
    def __init__(self,root):
        self.root=Node(root)
        
    def printtree(self,travesal_type):
        if travesal_type=='preorder':
            return self.preorder(tree.root,"")
        elif travesal_type=='inorder':
            return self.inorder(tree.root,"")
        elif travesal_type=='postorder':
            return self.postorder(tree.root,"")
        
        else:
            print('travesal not supported')
            
            
    def preorder(self,start,traversal):
        if start:
            traversal+=(str(start.value)+ '-')
            traversal=self.preorder(start.left,traversal)
            traversal=self.preorder(start.right,traversal)
        return traversal
    
    def inorder(self,start,traversal):
        if start:
            traversal=self.inorder(start.left,traversal)
            traversal+=(str(start.value)+ '-')
            traversal=self.inorder(start.right,traversal)
        return traversal
    
    def postorder(self,start,traversal):
        if start:
            traversal=self.postorder(start.left,traversal)
            traversal=self.postorder(start.right,traversal)
            traversal+=(str(start.value)+ '-')
        return traversal

tree=binarytree(1)
tree.root.left=Node(2)
tree.root.right=Node(3) 
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)

print(tree.printtree('preorder'))
print(tree.printtree('inorder'))
print(tree.printtree('postorder'))

       