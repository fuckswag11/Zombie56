class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(head, index):
    if head is None or index < 0:
        raise ValueError("Invalid index or empty list")
    
    current = head
    count = 0
    
    while current:
        if count == index:
            return current
        current = current.next
        count += 1
    
    raise ValueError("Index out of range")

# Примеры использования
list1 = Node(1, Node(2, Node(3)))
result1 = get_nth(list1, 0)
print(result1.data)  # Ожидаемый вывод: 1

list2 = Node(1, Node(2, Node(3, None)))
result2 = get_nth(list2, 2)
print(result2.data)  # Ожидаемый вывод: 3

try:
    get_nth(list2, 5)
except ValueError as e:
    print(e)  # Ожидаемый вывод: Index out of range

try:
    get_nth(None, 0)
except ValueError as e:
    print(e)  # Ожидаемый вывод: Invalid index or empty list