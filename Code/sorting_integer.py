#!python
from sorting_iterative import insertion_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Find range of given numbers (minimum and maximum integer values)
    minimum, maximum = min(numbers), max(numbers)
    # Create list of counts with a slot for each number in input range
    count_ls = [0] * (maximum - minimum + 1)
    # Loop over given numbers and increment each number's count
    for num in numbers:
        count_ls[num - minimum] += 1
    # Loop over counts and append that many numbers into output list
    k = 0
    for index, num in enumerate(count_ls):
        for i in range(num):
            # nums.append(index+minimum)
            numbers[k] = index+minimum
            k += 1


    return numbers


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Find range of given numbers (minimum and maximum values)
    maximum = max(numbers)
    minimum = min(numbers)

    # calculate each bucket's size
    bucket_size = (maximum - minimum + 1) / num_buckets

    # Create list of buckets to store numbers in subranges of input range
    buckets = [[] for i in range(num_buckets)]

    # Loop over given numbers and place each item in appropriate bucket
    for num in numbers:
        bucket_index = 0
        while bucket_index <  num_buckets:
            if (num - minimum) >= (bucket_size * bucket_index) and (num - minimum) < (bucket_size * (bucket_index+1)):
                buckets[bucket_index].append(num)
                break
            bucket_index += 1

    # Sort each bucket using insertion sort
    for i in range(num_buckets):
        insertion_sort(buckets[i])

    # Loop over buckets and append each bucket's numbers into output list
    index = 0
    for i in range(num_buckets):
        for j in range(len(buckets[i])):
            # mutate input instead of creating new output list
            numbers[index] = buckets[i][j]
            index += 1

    return numbers


if __name__ == "__main__":
    nums = [7, 8, 20, 32, 7, 8, 7, -2, -10]
    print(bucket_sort(nums))
