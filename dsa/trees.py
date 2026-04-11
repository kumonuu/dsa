class Node:
    def __init__(self,data):
        self.data = data
        self.children = []
    def display(self,level):
        print(level*"   "+self.data)

        if self.children:
            for child in self.children:
                child.display(level+1)
    def add_child(self,child): 
        self.children.append(child)

electronics = Node("Electronics")

tv = Node("TV")
electronics.add_child(tv)

toshiba = Node("Toshiba")
tv.add_child(toshiba)

phone = Node("Phone")
electronics.add_child(phone)

ios = Node("iOS")
phone.add_child(ios)

android = Node("Android")
phone.add_child(android)

laptop = Node("Laptop")
electronics.add_child(laptop)

macos = Node("MacOS")
laptop.add_child(macos)

electronics.display(0)