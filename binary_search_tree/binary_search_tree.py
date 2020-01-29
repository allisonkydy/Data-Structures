import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = self
        new_node = BinarySearchTree(value)
        while True:
            # compare value to root node
            # if value is lesser, move left
            if value < node.value:
                # if there's no child in that direction, insert the value
                if node.left is None:
                    node.left = new_node
                    break
                node = node.left
            # if value is greater or equal, move right
            else:
                if node.right is None:
                    node.right = new_node
                    break
                node = node.right
         

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        node = self
        while True:
            # if values match, return true
            if target == node.value:
                return True
            # if target is less, move left
            elif target < node.value:
                # if no left child, tree does not contain target
                if node.left is None:
                    return False
                node = node.left
            # if target is greater or equal, move right
            else:
                # if no right child, tree does not contain target
                if node.right is None:
                    return False
                node = node.right

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# bst = BinarySearchTree(1)

# bst.insert(2)
# bst.insert(3)
# # bst.insert(4)

# while bst is not None:
#     print(bst.value)
#     bst = bst.right