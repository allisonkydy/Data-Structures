class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # insert value at the end of the list
        self.storage.append(value)
        # bubble up the last value of list
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        # # put first element in temp var
        # first = self.storage[0]

        # print(first)
        # # change value of first element to value of last element
        # self.storage[0] = self.storage[-1]

        # print(first)
        # # pop last element from storage
        # self.storage.pop()
        # # while there are children and at least one child is larger than the last item
        # # while self.storage[2*]

        #     # check first element against children using formulas
        #     # if either is larger, swap value of parent with child
        pass

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
        pass

h = Heap()

