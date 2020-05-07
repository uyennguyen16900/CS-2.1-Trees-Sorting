from binaryheap import BinaryMinHeap

def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]


def heapify(arr, index, ending_index):
    """"""
    left_index = index * 2 + 1
    right_index = index * 2 + 2

    if left_index >= ending_index:
        return

    child_index = 0
    if right_index <= ending_index:
        if arr[left_index] > arr[right_index]:
            child_index = left_index
        else:
            child_index = right_index
    else:
        child_index = left_index

    print(arr[child_index], arr[index])

    if arr[child_index] > arr[index]:
        swap(arr, index, child_index)
        heapify(arr, child_index, ending_index)


def heap_sort(heap):
    """"""
    heap = BinaryMinHeap(arr)
    print(heap[0])
    last_index = heap.size() - 1
    while last_index > 0:
        swap(arr, 0, last_index)
        heapify(heap, 0, last_index)
        last_index -= 1

    return arr


arr = [2, 4, 5, 7, 4, 6, 9]

heapify(arr, 0, 6)
# print(heap)
print(heap_sort(arr))
