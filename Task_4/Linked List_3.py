class Node:
    def __init__(self, data=None):
        self.data = data  
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 

    def is_empty(self):
        return self.head is None  

    def append(self, data):
        new_node = Node(data) 
        if self.is_empty(): 
            self.head = new_node 
            return
        last_node = self.head 
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node  

    def prepend(self, data):
        new_node = Node(data) 
        new_node.next = self.head  
        self.head = new_node 

    def delete(self, data):
        if self.is_empty(): 
            return
        if self.head.data == data:
            self.head = self.head.next 
            return
        cur_node = self.head  
        while cur_node.next: 
            if cur_node.next.data == data:
                cur_node.next = cur_node.next.next 
                return
            cur_node = cur_node.next  

    def display(self):
        if self.is_empty(): 
            print("Список пуст")
            return
        cur_node = self.head 
        while cur_node:  
            print(cur_node.data, end = " .. ") 
            cur_node = cur_node.next  
        print("None")  

# Example usage:
my_linked_list = LinkedList()

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.prepend(0)

my_linked_list.display()

my_linked_list.delete(2)

my_linked_list.display()
