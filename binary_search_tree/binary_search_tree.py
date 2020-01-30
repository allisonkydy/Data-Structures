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
        # iterative solution
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

        # recursive solution from lecture
        # compare root node
        # if value < self.value:
        #     if not self.left:
        #         # if node does not exist, insert new node
        #         self.left = BinarySearchTree(value)
        #     else:
        #         # if node exists, recurse
        #         self.left.insert(value)
        # else: # value is >= node
        #     if not self.right:
        #         self.right = BinarySearchTree(value)
        #     else:
        #         self.right.insert(value)
         

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # recursive solution
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        else:
            if self.right is None:
                return False
            return self.right.contains(target)

        # iterative solution
        # node = self
        # while True:
        #     # if values match, return true
        #     if target == node.value:
        #         return True
        #     # if target is less, move left
        #     elif target < node.value:
        #         # if no left child, tree does not contain target
        #         if node.left is None:
        #             return False
        #         node = node.left
        #     # if target is greater or equal, move right
        #     else:
        #         # if no right child, tree does not contain target
        #         if node.right is None:
        #             return False
        #         node = node.right

        # recursive lecture solution
        # if self.value == target:
        #     return True
        # if target < self.value:
        #     if not self.left:
        #         return False
        #     else:
        #         return self.left.contains(target)
        # else:
        #     if not self.right:
        #         return False
        #     else:
        #         return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # move right until reach the rightmost (max) node
        while self.right is not None:
            self = self.right
        return self.value

        # recursive solution from lecture
        # if not self.right:
        #     return self.value
        # else:
        #     return self.right.get_max()

        # return recursive call when you want to find an answer
        # if it's a process or search, no need to return

        # iterative solution from lecture
        # max_value = self.value
        # # create a reference to the current node and update it 
        # # as we traverse the tree
        # current = self
        # while current:
        #     if current.value > max_value:
        #         max_value = current.value
        #     current = current.right
        # return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # second pass recursive solution
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

        # first pass recursive solution
        # def traverse_tree(node, cb):
        #     if node is None:
        #         return
        #     else:
        #         cb(node.value)
        #         traverse_tree(node.left, cb)
        #         traverse_tree(node.right, cb)
        # traverse_tree(self, cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)
        if self.right:
            self.right.in_order_print(self.right)
        print(self.value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # make a queue and temp var
        q = Queue()
        tmp = node
        q.enqueue(tmp)
        # while the queue is not empty
        while q.len() > 0:
            # save root in temp var, dequeue
            tmp = q.dequeue()
            # print value
            print(tmp.value)
            # check left and right
            # if item exists, add to queue
            if tmp.left:
                q.enqueue(tmp.left)
            if tmp.right:
                q.enqueue(tmp.right)
                
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # use a stack and a temp var
        # while the stack is not empty
            # save root in temp var, then pop off stack
            # do the thing (call cb)
            # check left and right
                # if left/right add to stack
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
