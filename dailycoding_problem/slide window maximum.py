"""
ood morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

Upgrade to premium an
"""
import collections

def find_slide_window_maximum(l, k):

    q = collections.deque()

    for i in range(k):
        while q and l[i] >= l[q[-1]]:
            q.pop()
        q.append(i)

    rt = []
    for i in range(k, len(l)):
        rt.append(l[q[0]])

        while q and q[0] <= i-k:
            q.popleft()

        while q and l[i] >= l[q[-1]]:
            q.pop()

        q.append(i)

    rt.append(l[q[0]])
    return rt

if __name__ == '__main__':
    l = [12, 1, 78, 90, 57, 89, 56]
    k = 3
    s = find_slide_window_maximum(l, k)
    print s