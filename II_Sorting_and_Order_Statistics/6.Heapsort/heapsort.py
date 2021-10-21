import math
import array as arr
from copy import deepcopy
from typing import Any, Union


class HeapUnderflowError(Exception):
    pass

class NewKeyIsSmallerThanCurrentKeyError(Exception):
    pass


class Heap:
    """Binary max heap implementation"""
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

    def heap_maximum(self) -> Union[float, int]:
        return self._array[0]

    def extract_max(self) -> Union[float, int]:
        if self.heap_size < 1:
            raise HeapUnderflowError

        max_key = self.heap_maximum()

        self._array[0] = self.array[self.heap_size]
        self.heap_size -= 1

        self.max_heapify(0)
        return max_key

    def increase_key(self, i: int, key: Union[float, int]) -> None:
        if key < self._array[i]:
            raise NewKeyIsSmallerThanCurrentKeyError

        self._array[i] = key

        while i > 0 and self.array[self.parent_idx(i)] < self._array[i]:
            self.exchange_values(idx1=i, idx2=self.parent_idx(i))
            i = self.parent_idx(i)

    def insert(self, key: Union[float, int]) -> None:
        self.heap_size += 1

        self._array[self.heap_size] = - math.inf
        self.increase_key(i=self.heap_size, key=key)

    def delete(self, i: int) -> None:
        if self.heap_size < 1:
            raise HeapUnderflowError

        if self._array[i] > self._array[self.heap_size]:
            self._array[i] = self._array[self.heap_size]
            self.max_heapify(i=i)
        else:
            self.increase_key(i=i, key=self.heap_size)

        self.heap_size -= 1


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
