"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".


"""

def find_reconstruct_palindrome(s):

    l, r = 0, 0
    minlth = float('INF')
    ans = ''
    while l < len(s) and r < len(s):
        i, j = find_palindrome(s, l, r)
        if i < 0 or j >= len(s):
            if i < 0:
                combine = s[j:][::-1] + s
                lth = len(combine)
            else:
                combine = s + s[:i+1][::-1]
                lth = len(combine)

            if lth < minlth:
                ans = combine
                minlth = lth
            elif lth == minlth:
                ans = min(combine, ans)
        if l == r:
            r += 1
        else:
            l += 1
    return ans


def find_palindrome(s, i, j):

    while i >= 0 and j < len(s) and s[i] == s[j]:
        i, j = i-1, j+1
    return (i, j)



if __name__ == '__main__':
    l1 = 'google'
    rt1 = find_reconstruct_palindrome(l1)
    print rt1

    l2 = 'race'
    rt2 = find_reconstruct_palindrome(l2)
    print rt2

    l3 = 'ababababa'
    rt3 = find_reconstruct_palindrome(l3)
    print rt3

    l4 = 'a'
    rt4 = find_reconstruct_palindrome(l4)
    print rt4