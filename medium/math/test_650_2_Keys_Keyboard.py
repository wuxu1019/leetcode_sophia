
def get_prime_numbers(n):
    p = 2
    prime = []
    while n > 1:
        while n%p == 0:
            prime.append(p)
            n = n/p
        p += 1
    return prime

if __name__ == '__main__':
    input = 100
    l = get_prime_numbers(input)
    print 'Prime list of {} is like {}'.format(input, l)
    input = 20
    l = get_prime_numbers(input)
    print 'Prime list of {} is like {}'.format(input, l)
    input = 1
    l = get_prime_numbers(input)
    print 'Prime list of {} is like {}'.format(input, l)
    input = 11
    l = get_prime_numbers(input)
    print 'Prime list of {} is like {}'.format(input, l)
