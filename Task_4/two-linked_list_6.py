class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:  
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node  
        new_node.prev = last_node  

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node 
        self.head = new_node

    def delete(self, data):
        current = self.head
        while current:  
            if current.data == data:
                if current.prev: 
                    current.prev.next = current.next
                if current.next: 
                    current.next.prev = current.prev
                if current == self.head:  
                    self.head = current.next
                return 
            current = current.next

    def display(self):
        current = self.head
        while current:  
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_reverse(self):
        current = self.head
        if not current:  
            print("None")
            return
        
        while current.next:  
            current = current.next
        
        while current:  
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Пример использования
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.display()  # Ожидаемый вывод: 1 <-> 2 <-> 3 <-> None

dll.prepend(0)
dll.display()  # Ожидаемый вывод: 0 <-> 1 <-> 2 <-> 3 <-> None

dll.delete(2)
dll.display()  # Ожидаемый вывод: 0 <-> 1 <-> 3 <-> None

dll.display_reverse()  # Ожидаемый вывод: 3 <-> 1 <-> 0 <-> None