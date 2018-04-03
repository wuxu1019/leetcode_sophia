
import bisect

def bs_right(l, target):
    lo, hi = 0, len(l)-1

    while lo <= hi:
        mid = lo + (hi - lo) / 2
        if l[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

def bs_left(l, target):
    lo, hi = 0, len(l) -1

    while lo <= hi:
        mid = lo + (hi - lo) / 2
        if l[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo

testcase = [([1, 3, 4, 5, 7, 9], 4),
            ([1, 1, 1, 1, 1], 1),
            ([1, 2, 2, 3], 2),
            ([], 2),
            ([1, 1, 2], 1)]

print "module bisect right"
for nums, k in testcase:
    p1 = bisect.bisect_right(nums, k)
    print p1

print "test my function bisect right"
for nums, k in testcase:
    p2 = bs_right(nums, k)
    print p2

print "module bisect left"
for nums, k in testcase:
    p3 = bisect.bisect_left(nums, k)
    print p3

print "test my function bisect left"
for nums, k in testcase:
    p4 = bs_left(nums, k)
    print p4

