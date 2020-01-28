from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.holding = 0
        self.cache = DoublyLinkedList()
        self.lookup = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # retrieve value from cache using key
        item = self.lookup.get(key)

        # return value if exists, if not return None
        if item.value is not None:
            # move element to front of cache (most recently used)
            self.cache.move_to_front(item)
            return item.value
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # check if key already exists using lookup
        # if not, create a new item and add it to cache and lookup
        if not key in self.lookup:
            # add item to cache and lookup
            self.cache.add_to_head((key, value))
            self.lookup.update({key: self.cache.head})
            # if cache is at max capacity
            if self.cache.length == limit:
                # remove oldest entry from cache (tail) and lookup
                oldest = self.cache.remove_from_tail()
                self.lookup.pop(oldest[0])
        # if it does
        else:
            # rewrite old value with new value
            item = self.lookup.get(key)
            item.value = (key, value)
            # move item to head of list (most recently used)
            self.cache.move_to_front(item)
