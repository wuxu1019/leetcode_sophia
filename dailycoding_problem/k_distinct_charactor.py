"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


"""
import collections

def K_distinct_charactor(s, k):
    ct = collections.Counter()
    ans = 0
    j = 0
    for i in range(len(s)):
        ct[s[i]] += 1
        while len(ct.keys()) > k:
            ct[s[j]] -= 1
            if ct[s[j]] == 0:
                del ct[s[j]]
            j += 1
        ans = max(ans, i-j + 1)
    return ans

if __name__ == '__main__':
    s = 'bcbcbcbcaaaaaaaaaaaaa'
    k = 2
    ans = K_distinct_charactor(s, k)
    print ans
