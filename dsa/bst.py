class Node:
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None
    
    def display(self):
        if self.left_child:
            self.left_child.display()
        print(self.data, end=" ")
        if self.right_child:
            self.right_child.display()

    def add_child(self,key):
        if key > self.data:
            if self.right_child:
                self.right_child.add_child(key)
            else:
                self.right_child = Node(key)
        elif key < self.data:
            if self.left_child:
                self.left_child.add_child(key)
            else:
                self.left_child = Node(key)

    def find_min(self):
        current = self
        while current.left_child:
            current = current.left_child
        return current.data

    def delete(self, key):
        if key < self.data:
            if self.left_child:
                self.left_child = self.left_child.delete(key)
            return self
        elif key > self.data:
            if self.right_child:
                self.right_child = self.right_child.delete(key)
            return self

        # leaf node
        if self.left_child is None and self.right_child is None:
            return None
        # one left child
        elif self.left_child is None:
            return self.right_child
        # one right child
        elif self.right_child is None:
            return self.left_child  
        # two children
        else:
            min_val = self.right_child.find_min()
            self.data = min_val
            self.right_child = self.right_child.delete(min_val)
            return self
    
    def minimum(self):
        if self.left_child:
            self.left_child.minimum()
            return self.left_child.data
        else:
            return self.data

    def maximum(self):
        if self.right_child:
            self.right_child.maximum()
            return self.right_child.data
        else:
            return self.data




root = Node(50)
root.add_child(30)
root.add_child(75)
root.add_child(40)

print(root.minimum())
print(root.maximum())