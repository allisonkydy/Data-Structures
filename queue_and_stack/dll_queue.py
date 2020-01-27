import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # add item to head of storage
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        # if queue is empty
        if self.size == 0:
            return
        # remove item from tail of storage
        item = self.storage.remove_from_tail()
        self.size -= 1
        return item

    def len(self):
        return self.size
        