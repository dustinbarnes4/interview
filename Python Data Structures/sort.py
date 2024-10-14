"""Name: Dustin Barnes
Course: 2400-001
Project 2: Sort
All of the following code was written by me. This project implements
several sort functions that use different methods to sort an unsorted
list. Implements quicksort, mergesort, selection_sort, and insertion_sort."""

from time import perf_counter
from random import seed, sample
from recursioncounter import RecursionCounter

def quicksort(lyst):
    """Acts as the user interface function to start the quicksort.
    passes the lyst along with the first and last indexes to the
    quicksort_helper function which performs the sort function recursively."""
    if not isinstance(lyst, list):
        raise ValueError("input to be sorted must be a list")
    quicksort_helper(lyst, 0, len(lyst)-1)
    return lyst

def quicksort_helper(lyst, low_index, high_index):
    """Takes input from the quicksort function and works with the function
    named partition along with recursive calls of itself to perform a quicksort."""
    RecursionCounter()
    if low_index < high_index:
        pivot_index = partition(lyst, low_index, high_index)
        quicksort_helper(lyst, low_index, pivot_index-1)
        quicksort_helper(lyst, pivot_index+1, high_index)

def partition(lyst, low_index, high_index):
    """Takes input from quicksort_helper and selects a pivot in the list, then
    compares items from the list with the pivot to place smaller items in front of
    it and larger items after it. At the end of this function the pivot will be in
    its proper place in the function."""
    middle_index = (low_index + high_index)//2
    pivot = lyst[middle_index]
    lyst[middle_index], lyst[high_index] = lyst[high_index], lyst[middle_index]
    boundary = low_index
    for index in range(low_index, high_index):
        if lyst[index] < pivot:
            lyst[index], lyst[boundary] = lyst[boundary], lyst[index]
            boundary += 1
    lyst[boundary], lyst[high_index] = lyst[high_index], lyst[boundary]
    return boundary

def mergesort(lyst):
    """Acts as the user interface function that initiates a mergesort
    function. Initiates a copy_buffer list the length of the input
    list and passes the copy_buffer, list to be sorted, and low and high
    indexes to mergesort_helper to initiate the mergesort."""
    if not isinstance(lyst, list):
        raise ValueError("input to be sorted must be a list")
    copy_buffer = [n*0 for n in range(len(lyst))]
    mergesort_helper(lyst, copy_buffer, 0, len(lyst)-1)
    return lyst

def mergesort_helper(lyst, copy_buffer, low_index, high_index):
    """Recursive function that continually splits the lyst into smaller pieces
    and works with merge to mergesort a list."""
    RecursionCounter()
    if low_index < high_index:
        middle_index = (low_index + high_index)//2
        mergesort_helper(lyst, copy_buffer, low_index, middle_index)
        mergesort_helper(lyst, copy_buffer, middle_index + 1, high_index)
        merge(lyst, copy_buffer, low_index, middle_index, high_index)

def merge(lyst, copy_buffer, low_index, middle_index, high_index):
    """Takes two sublists and merges them in the proper sorted order.
    index_1 represents the first index of the first sublist, and
    index_2 represents the first index of the second sublist. It then
    compares these with each other and sorts the sublists into one list
    located in the copy_buffer. Once the two sublists have been sorted,
    the copy_buffer is copied into the original lyst."""
    index_1 = low_index
    index_2 = middle_index + 1
    for i in range(low_index, high_index + 1):
        if index_1 > middle_index:
            copy_buffer[i] = lyst[index_2]
            index_2 += 1
        elif index_2 > high_index:
            copy_buffer[i] = lyst[index_1]
            index_1 += 1
        elif lyst[index_1] < lyst[index_2]:
            copy_buffer[i] = lyst[index_1]
            index_1 += 1
        else:
            copy_buffer[i] = lyst[index_2]
            index_2 += 1
    for i in range(low_index, high_index + 1):
        lyst[i] = copy_buffer[i]

def selection_sort(lyst):
    """Continually looks for the smallest item in the list and places
    that item at the front of the list. Repeats this process until the list
    is sorted."""
    if not isinstance(lyst, list):
        raise ValueError("input to be sorted must be a list")
    for index in range(len(lyst)): #pylint: disable=C0200
        for compare_index in range(index + 1, len(lyst)):
            if lyst[compare_index] < lyst[index]:
                lyst[compare_index], lyst[index] = lyst[index], lyst[compare_index]
    return lyst

def insertion_sort(lyst):
    """Takes a list as input and uses insertion to sort the list.
    This is done by taking each index and inserting it into a sublist
    at its proper sorted location."""
    if not isinstance(lyst, list):
        raise ValueError("input to be sorted must be a list")
    search_index = 1
    while search_index < len(lyst):
        insert_item = lyst[search_index]
        compare_index = search_index - 1
        while compare_index >= 0:
            if insert_item < lyst[compare_index]:
                lyst[compare_index + 1] = lyst[compare_index]
                compare_index -= 1
            else:
                break
        lyst[compare_index + 1] = insert_item
        search_index += 1
    return lyst

def is_sorted(lyst):
    """Takes a list as input, checks to make sure the items are integers, and
    then asserts whether or not the list is sorted. Returns true if it is sorted
    and false if it is not."""
    for i in lyst:
        if not isinstance(i, int):
            raise ValueError("items in the list must be integers")
    test_index = 0
    while test_index + 1 < len(lyst) and lyst[test_index] < lyst[test_index + 1]:
        status = True
        test_index += 1
    if lyst[test_index] == lyst[-1]:
        return status
    if lyst[test_index] > lyst[test_index + 1]:
        status = False
        return status

def main():
    """Main function. Performs 5 sorts including the 4 defined sort functions and
    the build in timsort .sort() function. It times each of these sorts and outputs the
    duration of each sort."""
    try:
        seed(0)
        sort_function_list = [selection_sort, insertion_sort, mergesort, quicksort]
        function_names_list = ["selection_sort", "insertion_sort", "mergesort", "quicksort"]
        for function in range(len(sort_function_list)): #pylint: disable=C0200
            data_set = sample(range(100000), 10000)
            function_name = function_names_list[function]
            print("Starting " + function_name)
            start_time = perf_counter()
            sort_function_list[function](data_set)
            finish_time = perf_counter()
            total_time = finish_time - start_time
            print(function_name + " duration: " + str(f'{total_time:.4f}') + " seconds\n")
        data_set = sample(range(100000), 10000)
        print("Starting timsort")
        start_time = perf_counter()
        data_set.sort()
        finish_time = perf_counter()
        total_time = finish_time - start_time
        print("timsort duration: " + str(f'{total_time:.4f}') + " seconds\n")
    except ValueError as err:
        print("Error ", err)

if __name__ == "__main__":
    main()
