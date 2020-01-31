class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # insert value at the end of the list
        self.storage.append(value)
        # bubble up the last value of list
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        # put first element in temp var
        first = self.storage[0]
        # change value of first element to value of last element
        self.storage[0] = self.storage[-1]
        # pop last element from storage
        self.storage.pop()
        # sift down first element
        self._sift_down(0)
        
        return first

    def get_max(self):
        if len(self.storage) > 0:
            return self.storage[0]
        else:
            return None

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # find index of parent
        parent = (index - 1) // 2
        # if parent index is -1 or parent value is greater than or equal to value at index, stop bubbling
        if parent < 0 or self.storage[parent] >= self.storage[index]:
            return
        # if parent value is less than value at index
        else:
            # swap parent value with value at index
            self.storage[parent], self.storage[index] = self.storage[index], self.storage[parent]
            # recurse with parent index
            self._bubble_up(parent)

    def _sift_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2

        # if there are no children, end sift
        if left >= self.get_size() and right >= self.get_size():
            return
        
        # if there is only a left child and it's larger than the 
        # value at the given index, swap and end sift
        if right >= self.get_size() and self.storage[left] > self.storage[index]:
            self.storage[left], self.storage[index] = self.storage[index], self.storage[left]
            return        
        
        max_child = None
        # find the index of the largest child
        if self.storage[left] >= self.storage[right]:
            max_child = left
        else:
            max_child = right
        # if the value of the largest child is greater than the value
        # at the given index, swap and continue sifting
        if self.storage[max_child] > self.storage[index]:
            self.storage[max_child], self.storage[index] = self.storage[index], self.storage[max_child]
            self._sift_down(max_child)

