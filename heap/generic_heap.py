class Heap:
    def __init__(self, comparator=lambda x, y: x > y):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        max = False
        if len(self.storage) > 1:
            self._switch(0, len(self.storage) - 1)
            max = self.storage.pop()
            self._sift_down(0)
        elif len(self.storage) is 1:
            max = self.storage.pop()
        return max

    def get_priority(self):
        return self.storage[0] if self.storage[0] else None

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent = index // 2 if index not in (1, 2) else 0
        if index is 0:
            return
        elif self.comparator(self.storage[index], self.storage[parent]):
            self._switch(index, parent)
            self._bubble_up(parent)

    def _sift_down(self, index):
        left = index * 2 if index is not 0 else 1
        right = index * 2 + 1 if index is not 0 else 2
        big = index
        if len(self.storage) > left and self.comparator(self.storage[left], self.storage[big]):
            big = left
        if len(self.storage) > right and self.comparator(self.storage[right], self.storage[big]):
            big = right
        if big is not index:
            self._switch(index, big)
            self._sift_down(big)

    def _switch(self, i, j):
        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]
