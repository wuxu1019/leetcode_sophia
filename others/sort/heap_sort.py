# heap sort
# average and worst time complexity is O(nlogn)

import sys
import multiprocessing

def heaplize(nums, p):
    r, l = p*2+1, (p+1)*2
    max = p
    if r < len(nums) and nums[max] < nums[r]:
        max = r
    if l < len(nums) and nums[max] < nums[l]:
        max = l
    if max != p:
        nums[max], nums[p] = nums[p], nums[max]
        heaplize(nums, max)
    return nums

def heap_sort(nums):
    for i in range(len(nums)/2-1, -1, -1):
        nums = heaplize(nums, i)
    for i in range(len(nums)-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        nums = heaplize(nums[0:i], 0)+nums[i:len(nums)]

def main():
    nums = [1, 6, 8, 9, 7, 3, 4, 5]
    print nums
    p = multiprocessing.Process(target=heap_sort, args=(nums,))
    p.start()
    p.join(10)
    if p.is_alive():
        print 'Process is still alive, let us kill it'
    p.terminate()
    p.join()
    
if __name__ == '__main__':
    main()

