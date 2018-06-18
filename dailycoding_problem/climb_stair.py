"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.


"""

def count_times(n):
    a, b = 1, 1
    if n < 2:
        return 1
    for i in range(2, n+1):
        c = a + b
        a, b = b, c
    return c

def count_times_multi(n, interval):
    ct = [0] * (n + 1)
    ct[0] = 1

    for i in range(1, n+1):
        ct[i] = sum(ct[i-j] for j in interval if i-j >= 0)

    return ct[n]

if __name__ == '__main__':
    ans = count_times(5)
    print ans

    ans = count_times_multi(4, [1, 3, 5])
    print ans

