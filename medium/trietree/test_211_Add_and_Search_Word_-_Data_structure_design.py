"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""


class TireNode(object):
    def __init__(self, val):
        self.end = val
        self.next = {}


class WordDictionary_trie_way(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = TireNode(False)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.addOneWord(word)

        return

    def addOneWord(self, word):
        root = self.tree

        for c in word:
            if c not in root.next:
                root.next[c] = TireNode(False)
            root = root.next[c]
        root.end = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchHelper(word, 0, self.tree)

    def searchHelper(self, word, p, root):
        if p == len(word):
            if root.end == True:
                return True
            else:
                return False
        if word[p] != '.':
            return word[p] in root.next and self.searchHelper(word, p + 1, root.next[word[p]])
        for c in string.ascii_lowercase:
            if c in root.next and self.searchHelper(word, p + 1, root.next[c]):
                return True
        return False


class WordDictionary_2_way(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = collections.defaultdict(set)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.dict[len(word)].add(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return True

        if len(word) not in self.dict:
            return False

        for candi in self.dict[len(word)]:
            for i, c in enumerate(word):
                if c != '.' and c != candi[i]:
                    break
            else:
                return True
        return False



