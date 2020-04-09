#!python
from sorting_iterative import insertion_sort
from random import *

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list

    combined_list = list()
    j, i = 0, 0

    while len(items1) > i and len(items2) > j:
        if items1[i] <= items2[j]:
            combined_list.append(items1[i])
            i += 1
        else:
            combined_list.append(items2[j])
            j += 1

    if i < len(items1):
        combined_list.extend(items1[i:])
    elif j < len(items2):
        combined_list.extend(items2[j:])

    return combined_list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order
    middle = len(items) // 2
    left_l = items[:middle]
    right_l = items[middle:]

    insertion_sort(left_l)
    insertion_sort(right_l)

    merged = merge(left_l, right_l)
    items[:] = merged

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Check if list is so small it's already sorted (base case)
    # Split items list into approximately equal halves
    # Sort each half by recursively calling merge sort
    # Merge sorted halves into one list in sorted order
    if len(items) <= 1:
        return items
    else:
        merged = merge(merge_sort(items[:len(items)//2]), merge_sort(items[len(items)//2:]))
        items[:] = merged



def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Choose a pivot any way and document your method in docstring above
    pivot = items[high]
    p_index = low
    # Loop through all items in range [low...high]
    for i in range(low, high):
    # Move items less than pivot into front of range [low...p-1]
        if items[i] <= pivot:
            items[i], items[p_index] = items[p_index], items[i]
            p_index += 1
    # Move items greater than pivot into back of range [p+1...high]
    items[p_index], items[high] = items[high], items[p_index]
    # Move pivot item into final position [p] and return index p
    return p_index


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Check if high and low range bounds have default values (not given)
    if low is None:
        low = 0
    if high is None:
        high = len(items) - 1
    # Check if list or range is so small it's already sorted (base case)
    if low < high:
        # Partition items in-place around a pivot and get index of pivot
        p_index = partition(items, low, high)
        # Sort each sublist range by recursively calling quick sort
        quick_sort(items, low, p_index-1)
        quick_sort(items, p_index+1, high)



a = [-2, 1, 10, 4, 2, 6]
b = ['B', 'A']
print(quick_sort(a))
print(merge_sort(b))
print(a)
