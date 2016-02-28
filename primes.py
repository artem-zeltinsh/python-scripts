import math


def sieve(n):
    """
    Finds prime numbers up to a given n with the sieve of Eratosthenes.
    :param n: sieve boundary
    :return: prime numbers less or equal to a given n
    """
    if n < 2:
        return []

    sieve_size = n + 1
    sieve = [True] * sieve_size
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if not sieve[i]:
            continue
        m = i * 2
        while m < sieve_size:
            sieve[m] = False
            m += i

    primes = []
    for i in range(sieve_size):
        if sieve[i]:
            primes.append(i)

    return primes


if __name__ == "__main__":
    for n in range(-1, 100):
        print "sieve(%d)=%s" % (n, str(sieve(n)))