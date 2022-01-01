
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root,new_val)


    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)


    def search(self, find_val):
        if self.root:
            current = self.root
            while current:
                if find_val < current.value:
                    current = current.left
                elif find_val > current.value:
                    current = current.right
                elif find_val == current.value:
                    return True

        return False

    # def search(self, find_val):
    #     return self.search_helper(self.root, find_val)
    #
    # def search_helper(self, current, find_val):
    #     if current:
    #         if current.value == find_val:
    #             return True
    #         elif current.value < find_val:
    #             return self.search_helper(current.right, find_val)
    #         else:
    #             return self.search_helper(current.left, find_val)
    #     return False

    def inorder_print(self, start, traversal):
        """recursive print solution."""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str((start.value)) + " "
            traversal = self.inorder_print(start.right, traversal)
        return traversal


# Set up tree
tree = BST(9)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.insert(5)
tree.insert(13)
tree.insert(11)

print(tree.inorder_print(tree.root," "))


# Check search
# Should be True

print(tree.search(4))
# Should be False
print(tree.search(6))