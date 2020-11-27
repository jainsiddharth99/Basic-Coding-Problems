class binarysearchtree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
            
    def add_node(self,value):
        if value ==self.value:
            return
        
        if value<self.value:
            if self.left:
                self.left.add_node(value)
            else:
                self.left=binarysearchtree(value)
        else:
            if self.right:
                self.right.add_node(value)
            else:
                self.right=binarysearchtree(value)
     
    def inorder(self):
        traversal=[]
        if self.left:
            traversal+=self.left.inorder()
            
        traversal.append(self.value)
        
        if self.right:
            traversal+=self.right.inorder()
        return traversal      
    
    def search(self,data):
        if self.value==data:
            return True
        if data<self.value:
            #value in left subtree
            if self.left:
                return self.left.search(data)
            else:
                return False    
        if data>self.value:
            #data in right subtree
            if self.right:
                return self.right.search(data)
            else:
                return False
            
    def find_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.find_max()
    
    def find_min(self):
        if self.left is None:
            return self.value
        else:
            return self.left.find_min()
        
    def delete(self,data):
        if data<self.value:
            if self.left:
                self.left=self.left.delete(data) 
                   
        elif data>self.value:
            if self.right:
                self.right=self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            
            if self.left is None:
                return self.right
            
            if self.right is None:
                return self.left   
            
            min_data=self.right.find_min()
            self.value=min_data
            self.right=self.right.delete(min_data)
            
        return self         
        
                     
def build_tree(traversal):
    root=binarysearchtree(traversal[0])
    for i in range(1,len(traversal)):
        root.add_node(traversal[i])       
    return root

num=[12,56,76,13,15,8,6]
number_tree=build_tree(num)
print(number_tree.inorder())

print(number_tree.search(13))

number_tree.add_node(17)
print(number_tree.inorder())

number_tree.delete(15)

print(number_tree.inorder())