"""
Given a string collection tag_list, an array of strings all_tags, find the smallest all_tags sub-array contains all the string in the tag_list, output the length of this sub-array. If there is no return -1.

1 <= |tag_list|,|all_tags| <=10000
All string length <= 50
Example
Given tag_list = ["made","in","china"], all_tags = ["made", "a","b","c","in", "china","made","b","c","d"], return 3.

Explanation:
["in", "china","made"] contains all the strings in tag_list,6 - 4 + 1 = 3.
Given tag_list = ["a"], all_tags = ["b"], return -1.

Explanation:
Does not exist.
"""


class Solution:
    """
    @param tagList: The tag list.
    @param allTags: All the tags.
    @return: Return the answer
    """

    def getMinimumStringArray(self, tagList, allTags):
        # Write your code here
        ["made", "a", "b", "c", "in", "china", "made", "b", "c", "d"]
        target = collections.Counter(tagList)
        ans = float('INF')
        i = 0
        ct = len(target)
        for j in range(len(allTags)):
            if allTags[j] in target:
                if target[allTags[j]] == 1:
                    ct -= 1
                target[allTags[j]] -= 1
            while ct == 0:
                ans = min(ans, j - i + 1)
                if allTags[i] in target:
                    if target[allTags[i]] == 0:
                        ct += 1
                    target[allTags[i]] += 1
                i += 1
        return ans if ans != float('INF') else -1


