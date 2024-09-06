class ndarray:
    def __init__(self, array=None):
        if array:
            self.array = array
        else:
            self.array = []

    def __add__(self, nd):
        if isinstance(nd, int):
            new_nd = ndarray()
            for i in range(len(self.array)):
                new_nd.array.append(self.array[i] + nd)
            return new_nd

        if len(self.array) != len(nd.array):
            raise ValueError('arrays are not the same size')

        new_nd = ndarray()
        for i in range(len(self.array)):
            new_nd.array.append(self.array[i] + nd.array[i])

        return new_nd

    def __mul__(self, nd):
        if len(self.array) != len(nd.array):
            raise ValueError('arrays are not the same size')

        new_nd = ndarray()
        for i in range(len(self.array)):
            new_nd.array.append(self.array[i] * nd.array[i])

        return new_nd

    def __repr__(self):
        return str(self.array)


x = ndarray([1, 2, 3, 4, 5])
y = ndarray([10, 20, 30, 40, 50])
z = ndarray([5, 2, 3, 1, 6])

k = (x + y) * z
# print(k)
import numpy as np

a = np.random.randint(10, 20, (3, 3), dtype='int8')
print(a)