# insertion sort
# time complexity is O(n2)
# space complexity is 0

import sys
import multiprocessing

def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i-1
        key = nums[i]
        while nums[j] > key and j >= 0:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key 
    print nums
    return None

def main():
    nums = [5, 4, 3, 2, 1]
    print nums
    p = multiprocessing.Process(target=insertion_sort, args=(nums,))
    p.start()
    p.join(10)
    if p.is_alive():
        print 'Process is still alive, let us kill it'
    p.terminate()
    p.join()
    
if __name__ == '__main__':
    main()

