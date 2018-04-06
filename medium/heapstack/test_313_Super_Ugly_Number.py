"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.


"""
import heapq

class Solution(object):
    def nthSuperUglyNumber_kmerge(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1]
        pos = [0] * len(primes)
        while n > 1:
            candi = [ugly[pos[i]] * primes[i] for i in range(len(primes))]
            mini = min(candi)
            ugly.append(mini)
            for c, i in enumerate(pos):
                if candi[c] == mini:
                    pos[c] = i + 1
            n -= 1
        return ugly

    def nthSuperUglyNumber_heap(self, n, primes):
        q = [(primes[i], 0, primes[i]) for i in range(len(primes))]
        heapq.heapify(q)
        ugly = [1]
        while n > 1:
            last, pos, p = heapq.heappop(q)
            ugly.append(last)
            while 1:
                heapq.heappush(q, (ugly[pos + 1] * p, pos + 1, p))
                if q[0][0] == last:
                    last, pos, p = heapq.heappop(q)
                else:
                    break
            n -= 1
        return ugly

if __name__ == '__main__':
    s = Solution()
    n = 12
    primes = [2, 3, 5]
    rt1 = s.nthSuperUglyNumber_heap(n, primes)

    rt2 = s.nthSuperUglyNumber_kmerge(n, primes)

    print rt1
    print rt2
