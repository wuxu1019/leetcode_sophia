# bubble sort
# time complexity is O(n2)
# space complexity is 0

import sys
import multiprocessing

def bubble_sort(nums):
    change = True
    while change:
        change = False
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                change = True
    print nums
    return None

def main():
    nums = [5, 4, 3, 2, 1]
    print nums
    p = multiprocessing.Process(target=bubble_sort, args=(nums,))
    p.start()
    p.join(10)
    if p.is_alive():
        print 'Process is still alive, let us kill it'
    p.terminate()
    p.join()
    
if __name__ == '__main__':
    main()

