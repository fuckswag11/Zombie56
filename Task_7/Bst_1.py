class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key, value=None):
        new_node = BSTNode(key, value)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    return
                current = current.right

    def search(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None 

    def delete(self, key):
        node_to_delete = self._find_node(self.root, key)
        if node_to_delete is None:
            return False
        
        if node_to_delete.left is None and node_to_delete.right is None:
            if node_to_delete == self.root:
                self.root = None
            else:
                if node_to_delete == node_to_delete.parent.left:
                    node_to_delete.parent.left = None
                else:
                    node_to_delete.parent.right = None

        elif node_to_delete.left is None or node_to_delete.right is None:
            child = node_to_delete.left if node_to_delete.left else node_to_delete.right
            if node_to_delete == self.root:
                self.root = child
            else:
                if node_to_delete == node_to_delete.parent.left:
                    node_to_delete.parent.left = child
                else:
                    node_to_delete.parent.right = child
            child.parent = node_to_delete.parent

        else:
            successor = self._find_min(node_to_delete.right)
            node_to_delete.key = successor.key
            node_to_delete.value = successor.value
            self.delete(successor.key)

        return True

    def _find_node(self, root, key):
        while root is not None:
            if key == root.key:
                return root
            elif key < root.key:
                root = root.left
            else:
                root = root.right
        return None

    def inorder_traversal(self):
        return list(self._inorder_helper(self.root))

    def _inorder_helper(self, node):
        if node is not None:
            yield from self._inorder_helper(node.left)
            yield (node.key, node.value)
            yield from self._inorder_helper(node.right)

    def find_min(self):
        if self.root is None:
            return None
        return self._find_min(self.root).key

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def find_max(self):
        if self.root is None:
            return None
        return self._find_max(self.root).key

    def _find_max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def height(self):
        return self._height_helper(self.root)

    def _height_helper(self, node):
            if node is None:
                return -1  # Высота пустого дерева -1
            left_height = self._height_helper(node.left)
            right_height = self._height_helper(node.right)
            return max(left_height, right_height) + 1


        