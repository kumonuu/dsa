class Node:
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None
    
    def display(self):
        if self.left_child:
            self.left_child.display()
        print(self.data)
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

    #def delete(self):

root = Node(50)
root.add_child(30)
root.add_child(70)
root.add_child(80)
root.add_child(60)
root.add_child(40)
root.add_child(10)
root.add_child(75)

root.display()