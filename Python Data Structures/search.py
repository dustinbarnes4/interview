"""Name: Dustin Barnes
Course: 2420-001
Project 1, Search
All of the following code was written solely by me. This project
creates functions for three different search algorithms,
linear, recursive binary, and jump searching."""

import math
from random import seed, sample
import time
from recursioncounter import RecursionCounter

def linear_search(lyst, target):
    """Takes in a target and a list and searches the list
    sequentially for the target. Target and all items in the list
    must be integers. Returns True if the target is in the list
    and False if it is not."""
    if not isinstance(target, int):
        raise ValueError("target must be an integer")
    for item in lyst:
        if not isinstance(item, int):
            raise ValueError("items in the list must be integers")
        if item is target:
            return True
    return False

def recursive_binary_search(lyst, target):
    """Takes a list and a target and uses recursion via the
    recursive_binary_search_helper to conduct a binary search for the
    target. If the target is in the list, it will return True, if it
    is not it will return False. Target and items in the list must be integers"""
    def recursive_binary_search_helper(low_index, high_index, lyst, target): #pylint: disable=R1710
        """This function helps the main recursive_binary_search by taking in low
        and high indexes and then performs binary searches through the list."""
        RecursionCounter()
        if not isinstance(lyst[low_index], int):
            raise ValueError("items in the list must be integers")
        if not isinstance(lyst[high_index], int):
            raise ValueError("items in the list must be integers")
        #base case
        if low_index == high_index:
            if target is lyst[low_index]:
                return True
            return False
        mid_index = (low_index + high_index)//2
        if not isinstance(lyst[mid_index], int):
            raise ValueError("items in the list must be integers")
        if target is lyst[mid_index]:
            return True
        if target > lyst[mid_index]:
            low_index = mid_index + 1
            return recursive_binary_search_helper(low_index, high_index, lyst, target)
        if target < lyst[mid_index]:
            high_index = mid_index
            return recursive_binary_search_helper(low_index, high_index, lyst, target)

    if not isinstance(target, int):
        raise ValueError("target must be an integer")
    low_index = 0
    high_index = len(lyst)-1
    return recursive_binary_search_helper(low_index, high_index, lyst, target)

def jump_search(lyst, target):
    """Takes in a target and a list and conducts a jump search
    to see if the target is in the list. Target and all items in the list
    must be integers. Uses the square root of the length of the list to determine
    the length of the jump segements. If the item is in the list then it will return
    True, if it is not then it will return False."""
    if not isinstance(target, int):
        raise ValueError("target must be an integer")
    jump_size = int(math.sqrt(len(lyst)))
    search_index = jump_size
    while lyst[search_index] < target:
        search_index = search_index + jump_size
        if search_index >= len(lyst)-1:
            break
    search_index = search_index - jump_size
    while search_index <= min(target, len(lyst)-1):
        if not isinstance(lyst[search_index], int):
            raise ValueError("items in the list must be integers")
        if lyst[search_index] == target:
            return True
        search_index += 1
    return False

def main():
    """The main function. Creates a data set in a list of 5000000 integers from a range of
    50000000. It then sorts them, and then times the algorithms in searches for items in
    the beginning, middle, and end of the array while printing out these times."""
    seed(0)
    data_set = sample(range(50000000), 5000000)
    data_set.sort()
    test_elements = [data_set[0], data_set[2500000], data_set[-1], -1]
    search_function_list = [linear_search, recursive_binary_search, jump_search]
    search_times = []
    search_truth = []
    try:
        for element in test_elements:
            for function in search_function_list:
                start_time = time.perf_counter()
                search_truth.append(function(data_set, element))
                end_time = time.perf_counter()
                total_time = end_time - start_time
                search_times.append(total_time)
    except ValueError as err:
        print("Error,", err)
    print("Searching for a number in the beginning of the array...")
    print("\tlinear_search() returned "+str(search_truth[0])+" in "+str(f'{search_times[0]:.7f}')+" seconds") #pylint: disable=C0301
    print("\trecursive_binary_search() returned "+str(search_truth[1])+" in "+str(f'{search_times[1]:.7f}')+" seconds")  #pylint: disable=C0301
    print("\tjump_search() returned "+str(search_truth[2])+" in "+str(f'{search_times[2]:.7f}')+" seconds")  #pylint: disable=C0301
    print("Searching for a number in the middle of the array...")
    print("\tlinear_search() returned "+str(search_truth[3])+" in "+str(f'{search_times[3]:.7f}')+" seconds")  #pylint: disable=C0301
    print("\trecursive_binary_search() returned "+str(search_truth[4])+" in "+str(f'{search_times[4]:.7f}')+" seconds")  #pylint: disable=C0301
    print("\tjump_search() returned "+str(search_truth[5])+" in "+str(f'{search_times[5]:.7f}')+" seconds")  #pylint: disable=C0301
    print("Searching for a number at the end of the array...")
    print("\tlinear_search() returned "+str(search_truth[6])+" in "+str(f'{search_times[6]:.7f}')+" seconds")  #pylint: disable=C0301
    print("\trecursive_binary_search() returned "+str(search_truth[7])+" in "+str(f'{search_times[7]:.7f}')+" seconds")  #pylint: disable=C0301
    print("\tjump_search() returned "+str(search_truth[8])+" in "+str(f'{search_times[8]:.7f}')+" seconds")  #pylint: disable=C0301
    print("Searching for a number NOT in the array...")
    print("\tlinear_search() returned "+str(search_truth[9])+" in "+str(f'{search_times[9]:.7f}')+" seconds")  #pylint: disable=C0301
    print("\trecursive_binary_search() returned "+str(search_truth[10])+" in "+str(f'{search_times[10]:.7f}')+" seconds")  #pylint: disable=C0301
    print("\tjump_search() returned "+str(search_truth[11])+" in "+str(f'{search_times[11]:.7f}')+" seconds")  #pylint: disable=C0301

if __name__ == "__main__":
    main()
