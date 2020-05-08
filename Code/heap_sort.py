def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]

def heap_sort(items):
    count = len(items) - 1
    heapify(items)
    while count >= 0:
        swap(items, 0, count)
        sift_down(items, 0, count-1)
        count -= 1

def heapify(items):
    """Turn items to a heap in linear time"""
    end = len(items) - 1
    start = (end - 1) // 2

    while start >= 0:
        sift_down(items, start, end)
        start -= 1

def sift_down(items, parent_index, end):
    while parent_index * 2 + 1 <= end:
        child = parent_index * 2 + 1
        if child + 1 <= end and items[child] < items[child + 1]:
            child += 1

        if items[parent_index] < items[child]:
            swap(items, parent_index, child)
            parent_index = child
        else:
            return

if __name__ == "__main__":
    arr = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
    heap_sort(arr)
    print(arr)

    arr2 = [21, 17, 2, 28, 515, 30, 1000, 1020, 1002, 2, 0, -10]
    heap_sort(arr2)
    print(arr2)
