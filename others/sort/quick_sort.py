# quick sort
# time complexity is O(nlogn), worse case is o(n2)
# space complexity is n

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    less, more, plist, pivot = [], [], [], nums[0]
    for num in nums:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            more.append(num)
        else:
            plist.append(num)
    return quick_sort(less) + plist + quick_sort(more)

    
def main():
    nums = [5, 9, 4, 6, 3, 2, 7, 1]
    print nums
    nums = quick_sort(nums)
    print nums

if __name__ == '__main__':
    main()

