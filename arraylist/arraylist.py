import ctypes


class ArrayList:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.arr = self.create_array(self.capacity)

    def length(self):
        return self.size

    def add(self, element):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = element
        self.size += 1

    def get(self, index):
        if 0 < index >= self.size:
            raise IndexError('Index out of bound ')
            # return -1
        return self.arr[index]

    def resize(self):
        new_array = self.create_array(2 * self.capacity)

        for i in range(self.capacity):
            new_array[i] = self.arr[i]

        self.capacity *= 2
        self.arr = new_array

    @staticmethod
    def create_array(size):
        return (size * ctypes.py_object)()
