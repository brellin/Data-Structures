class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        max = None
        if len(self.storage) > 1:
            self._switch(0, len(self.storage) - 1)
            max = self.storage.pop()
            self._sift_down(0)
        elif len(self.storage) is 1:
            max = self.storage.pop()
        return max

    def get_max(self):
        return self.storage[0] if len(self.storage) else False

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent = index // 2 if index not in (1, 2) else 0
        if index is 0:
            return
        elif self.storage[index] > self.storage[parent]:
            self._switch(index, parent)
            self._bubble_up(parent)

    def _sift_down(self, index):
        left = index * 2 if index is not 0 else 1
        right = index * 2 if index is not 0 else 2
        big = index
        if len(self.storage) > left and self.storage[left] > self.storage[index]:
            big = left
        if len(self.storage) > right and self.storage[right] > self.storage[index]:
            big = right
        if big is not index:
            self._switch(big, index)

    def _switch(self, i, j):
        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]
