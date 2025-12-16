class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def linked_list(*values):
    ll = LinkedList()
    for value in values:
        new_node = Node(value)
        if ll.head is None:
            ll.head = new_node
        else:
            current = ll.head
            while current.next:
                current = current.next
            current.next = new_node
    return ll

def print_linked_list(linked_list):
    current = linked_list.head
    result = []
    while current:
        result.append(str(current.value))
        current = current.next
    print(" -> ".join(result) + " -> None")

def get_node_and_prev(linked_list, index):
    current = linked_list.head
    prev = None
    count = 0
    
    while current and count < index:
        prev = current
        current = current.next
        count += 1
    
    if current is None:  
        return None, None
    
    return current, prev

def swap_nodes(list_pointer1, index1, list_pointer2, index2):
    list1 = list_pointer1[0]
    list2 = list_pointer2[0]

    node1, prev1 = get_node_and_prev(list1, index1)
    node2, prev2 = get_node_and_prev(list2, index2)

    if node1 is None or node2 is None:
        return False  

    
    if list1 == list2 and index1 == index2:
        return False

    
    if prev1 is not None:
        prev1.next = node2
    else:
        list1.head = node2  

    if node2 is not None:
        temp_next = node2.next
        node2.next = node1.next
        node1.next = temp_next

   
    if prev2 is not None:
        prev2.next = node1
    else:
        list2.head = node1 

    if node1 is not None:
        temp_next = node1.next
        node1.next = temp_next

    return True

# Пример использования
list1 = linked_list(1, 2, 3, 4)
list2 = linked_list(5, 6, 7, 8)

result = swap_nodes([list1], 2, [list2], 0)
print(result)  # Вывод: True

print_linked_list(list1)
# Вывод: 1 -> 2 -> 5 -> 4 -> None

print_linked_list(list2)
# Вывод: 3 -> 6 -> 7 -> 8 -> None

list1 = linked_list(1, 2, 3)
list2 = linked_list(4, 5, 6)

result = swap_nodes([list1], 1, [list2], 3)
print(result)  # Вывод: False

print_linked_list(list1)
# Вывод: 1 -> 2 -> 3 -> None

print_linked_list(list2)
# Вывод: 4 -> 5 -> 6 -> None