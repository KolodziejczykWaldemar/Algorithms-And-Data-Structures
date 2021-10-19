import math
import array as arr
from copy import deepcopy


class Heap:
    def __init__(self, array: arr.array, inplace: bool = True) -> None:
        if inplace:
            self._array = array
        else:
            self._array = deepcopy(array)
        self._heap_size = len(self._array)

    def __getitem__(self, item: int):
        return self._array[item]

    def exchange_values(self, idx1: int, idx2: int) -> None:
        temp = self._array[idx1]

        self._array[idx1] = self._array[idx2]
        self._array[idx2] = temp

    @property
    def array(self) -> arr.array:
        return self._array

    @property
    def heap_size(self) -> int:
        return self._heap_size

    @heap_size.setter
    def heap_size(self, size: int) -> None:
        self._heap_size = max(0, size)

    @staticmethod
    def parent_idx(i: int) -> int:
        return math.floor(i/2)

    @staticmethod
    def left_idx(i: int) -> int:
        return 2 * i

    @staticmethod
    def right_idx(i: int) -> int:
        return 2 * i + 1

    def max_heapify(self, i: int) -> None:
        l = self.left_idx(i)
        r = self.right_idx(i)

        if l < self._heap_size and self._array[l] > self._array[i]:
            largest = l
        else:
            largest = i
        if r < self._heap_size and self._array[r] > self._array[largest]:
            largest = r
        if largest != i:
            self.exchange_values(idx1=i, idx2=largest)
            self.max_heapify(i=largest)

    def build_max_heap(self) -> None:
        for i in reversed(range(math.floor(len(self._array) / 2))):
            self.max_heapify(i)


def heapsort(array: arr.array) -> arr.array:
    heap = Heap(array=array, inplace=False)
    heap.build_max_heap()
    for i in reversed(range(1, len(heap.array))):
        heap.exchange_values(idx1=0, idx2=i)
        heap.heap_size -= 1
        heap.max_heapify(0)
    return heap.array


if __name__ == '__main__':
    a = arr.array('i', [40, 5, 3, 2, 6, 7, 1, 3, 2, 4, 99, 1])
    print(heapsort(a))
