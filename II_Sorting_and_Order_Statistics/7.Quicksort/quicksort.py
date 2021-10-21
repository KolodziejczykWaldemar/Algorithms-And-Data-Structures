import array as arr


def quicksort(array: arr.array, p: int, r: int) -> None:
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q-1)
        quicksort(array, q+1, r)


def partition(array: arr.array, p: int, r: int) -> int:
    x = array[r]
    i = p - 1

    for j in range(p, r):
        if array[j] <= x:
            i += 1

            # exchange array[i] with array[j]
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

    # exchange array[i + 1] with array[r]
    temp = array[i + 1]
    array[i + 1] = array[r]
    array[r] = temp
    return i + 1


if __name__ == '__main__':
    a = arr.array('i', [40, 5, 3, 2, 6, 7, 1, 3, 2, 4, 99, 1])
    print(a)
    quicksort(a, 0, len(a)-1)
    print(a)
