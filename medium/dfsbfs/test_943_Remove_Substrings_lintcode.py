

class Solution:
    # @param {string} s a string
    # @param {set} dict a set of n substrings
    # @return {int} the minimum length
    def minLength(self, s, dict):
        # Write your code here
        self.ans = len(s)
        self.record = set()

        def minLengthHelper(s, dict):
            if s in self.record:
                return
            self.record.add(s)
            self.ans = min(self.ans, len(s))

            for sub in dict:
                start = 0

                while start < len(s) and sub in s[start:]:
                    start = s.index(sub, start)
                    minLengthHelper(s[:start] + s[start+len(sub):], dict)
                    start = start + 1

        minLengthHelper(s, dict)
        return self.ans

    def minLength_bfs(self, s, dict):
            # Write your code here
            import Queue
            que = Queue.Queue()
            que.put(s)
            hash = set([s])

            min = len(s)

            while not que.empty():
                s = que.get()
                for sub in dict:
                    found = s.find(sub)
                    while found != -1:
                        new_s = s[:found] + s[found + len(sub):]
                        if new_s not in hash:
                            if len(new_s) < min:
                                min = len(new_s)
                            que.put(new_s)
                            hash.add(new_s)

                        found = s.find(sub, found + 1)
            return min


if __name__ == '__main__':
    s = Solution()
    l = 'aaaaaaaaaabbbbbbabbbbaba'
    dict = ['ab', 'ba']
    rt = s.minLength(l, dict)
    rt2 = s.minLength_dfs(l, dict)
    print rt
    print rt2