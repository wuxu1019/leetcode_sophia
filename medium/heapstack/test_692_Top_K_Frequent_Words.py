"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:
You may assume k is always valid, 1  k  number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.

"""
import collections
import heapq

class Solution(object):

    def topKFrequent_bf(self, words, k):
        ct = collections.Counter(words)
        sort_word = sorted(ct.items(), key=lambda m: (-m[1], m[0]))
        return [data[0] for data in sort_word][:k]


    def topKFrequent_heap(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        ct = collections.Counter(words)
        heap = [(-val, key) for key, val in ct.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for i in range(0, k)]


if __name__ == '__main__':
    s = Solution()
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 2
    rt1 = s.topKFrequent_heap(words, k)
    print rt1

    rt2 = s.topKFrequent_bf(words, k)
    print rt2