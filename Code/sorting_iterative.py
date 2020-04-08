#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    for i in range(len(items)-1):
        if items[i] > items[i+1]:
            return False

    return True


# def swap(array, index1, index2):
#     """"""
#     temp = array[index1]
#     array[index1] = array[index2]
#     array[index2] = temp

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    n = len(items)
    for i in range(n):
         for j in range(n-i-1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    for i in range(len(items)):
        min = items[i]
        min_index = i

        for j in range(i, len(items)):
            if items[j] < min:
                min = items[j]
                min_index = j

        items[i], items[min_index] = items[min_index], items[i]


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    for i in range(len(items)-1):
        j = i + 1
        while j > 0 and items[j-1] > items[j]:
            items[j-1], items[j] = items[j], items[j-1]
            j -= 1


array = [5, 3, 6, 1, 9, 2]
# selection_sort(array)
# bubble_sort(array)
insertion_sort(array)
print(array)
