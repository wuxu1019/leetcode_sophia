"""


Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2

"""
import bisect
import heapq

def get_median_data_insert_sort(array):

    slist = []
    rt = []
    for data in array:
        if not slist:
            slist.append(data)
        else:
            p = bisect.bisect_right(slist, data)
            slist = slist[:p] + [data] + slist[p:]

        if len(slist) % 2 == 1:
            mid = slist[len(slist)/2]
            rt.append(mid)
        else:
            mid = (slist[len(slist)/2-1] + slist[len(slist)/2])/2.0
            if int(mid) == mid:
                rt.append(int(mid))
            else:
                rt.append(mid)
    return rt

def get_median_data_heap(array):

    heap_max = []
    heap_min = []
    rt = []

    for data in array:
        heapq.heappush(heap_max, data)
        mx = heapq.nlargest(1, heap_max)[0]
        index = heap_max.index(mx)
        heap_max.pop(index)

        heapq.heappush(heap_min, mx)

        if len(heap_min) > len(heap_max):
            min = heapq.heappop(heap_min)
            heapq.heappush(heap_max, min)

        if len(heap_max) == len(heap_min):
            mid = (heapq.nlargest(1, heap_max)[0] + heapq.nsmallest(1, heap_min)[0]) / 2.0
        else:
            mid = heapq.nlargest(1, heap_max)[0]
        if mid == int(mid):
            rt.append(int(mid))
        else:
            rt.append(mid)

    return rt


if __name__ == '__main__':
    l = [2, 1, 5, 7, 2, 0, 5]
    rt1 = get_median_data_insert_sort(l)
    print rt1

    rt2 = get_median_data_heap(l)
    print rt2