class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self, data):
        self.root = Node(data)
        
    def insert(self, data):
        self.curr_node = self.root
        while True:
            if self.curr_node.data > data:
                if self.curr_node.left != None:
                    self.curr_node = self.curr_node.left
                else:
                    self.curr_node.left = Node(data)
                    break
            else:
                if self.curr_node.right != None:
                    self.curr_node = self.curr_node.right
                else:
                    self.curr_node.right = Node(data)
                    break
    
    def search(self, data):
        self.curr_node = self.root
        while self.curr_node != None:
            if self.curr_node.data == data:
                return True
            elif self.curr_node.data > data:
                self.curr_node = self.curr_node.left
            else:
                self.curr_node = self.curr_node.right
        return False
    
    def delete(self, data):
        is_search = False
        self.curr_node = self.root
        self.parent = self.root
        
        while self.curr_node:
            if self.curr_node.data == data:
                is_search = True
                break
            elif data < self.curr_node.data:
                self.parent = self.curr_node
                self.curr_node = self.curr_node.left
            else:
                self.parent = self.curr_node
                self.curr_node = self.curr_node.right
        
        if is_search == False:
            return False
        
        if self.curr_node.left == None and self.curr_node.right == None:
            if data < self.parent.data:
                self.parent.left = None
            else:
                self.parent.right = None
        
        if self.curr_node.left != None and self.curr_node.right == None:
            if data < self.parent.data:
                self.parent.left = self.curr_node.left
            else:
                self.parent.right = self.curr_node.left
        
        if self.curr_node.left == None and self.curr_node.right != None:
            if data < self.parent.data:
                self.parent.left = self.curr_node.right
            else:
                self.parent.right = self.curr_node.right
        
        if self.curr_node.left != None and self.curr_node.right != None:
            self.change_node = self.curr_node.right
            self.change_node_parent = self.curr_node.right
            while self.change_node.left != None:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
            if self.change_node.right != None:
                self.change_node_parent.left = self.change_node.right
            else:
                self.change_node_parent.left = None
                
            if data < self.parent.data:
                self.parent.left = self.change_node
                self.change_node.right = self.curr_node.right
                self.change_node.left = self.curr_node.left
            else:
                self.parent.right = self.change_node
                self.change_node.right = self.curr_node.right
                self.change_node.left = self.curr_node.left

            return True 