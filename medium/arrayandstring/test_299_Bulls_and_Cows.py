"""
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

For example:

Secret number:  "1807"
Friend's guess: "7810"
Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. In the above example, your function should return "1A3B".

Please note that both secret number and friend's guess may contain duplicate digits, for example:

Secret number:  "1123"
Friend's guess: "0111"
In this case, the 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow, and your function should return "1A1B".
You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

Credits:
Special thanks to @jeantimex for adding this problem and creating all test cases.
"""

class Solution(object):
    def getHint_twopass(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secl = [0] * 10
        gusl = [0] * 10
        bull, cow = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                secl[ord(secret[i]) - ord('0')] += 1
                gusl[ord(guess[i]) - ord('0')] += 1
        for i in range(len(secl)):
            cow += min(secl[i], gusl[i])
        return '{0}A{1}B'.format(bull, cow)

    def getHint_onepass(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        ct = [0] * 10
        bull, cow = 0, 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                s = ord(secret[i]) - ord('0')
                g = ord(guess[i]) - ord('0')
                if ct[s] < 0:
                    cow += 1
                if ct[g] > 0:
                    cow += 1
                ct[s] += 1
                ct[g] -= 1
        return '{0}A{1}B'.format(bull, cow)

if __name__ == '__main__':
    s = Solution()
    secret = "1123"
    guess = "0111"
    rt1 = s.getHint_onepass(secret, guess)
    rt2 = s.getHint_twopass(secret, guess)

    print rt1
    print rt2