from itertools import islice, count
from functools import partial
from skynet.decorators import memoize
from fractions import Fraction

def Fibonacci() :
    '''A Generator for the Fibonacci numbers.'''
    p, q = 0, 1

    while True :
        yield p
        p, q = q, p + q

@memoize
def fibonacci(n) :
    '''Computes the nth Fibonacci number.'''

    if n in (0, 1) :
        return n

    if n % 2 :
        return fibonacci((n - 1) // 2) ** 2 + fibonacci((n + 1) // 2) ** 2
    else :
        return (2 * fibonacci((n // 2) - 1) + fibonacci(n // 2)) * fibonacci(n // 2)

def primes_until(n) :
    '''Generates all prime numbers below a given upper bound.'''

    if n < 2 :
        return []

    length = n // 2 - 1 + (n % 2)

    sieve = [True] * (length + 1)

    for i in range(int(n**0.5) >> 1) :
        if not sieve[i] :
            continue

        start = 3 + (i * (i + 3) << 1)
        step = 3 + (i << 1)

        div, mod = divmod(length - start, step)
        sieve[start:length:step] = [False] * (div + bool(mod))

    primes = [2]
    primes.extend([(i << 1) + 3 for i in range(length) if sieve[i]])

    return primes

def primes_between(m, n) :
    '''Generates all primes between given lower and upper bounds.'''

    d = n - m + 1
    bitmap = [True] * d
    bitmap[(m % 2)::2] = [False] * int(round((1 + d - (m % 2)) // 2))

    for i in range(3, int(n ** 0.5) + 1, 2) :
        if i > m and not bitmap[i - m] :
            continue

        j = m // i*i

        if j < m :
            j += i

        if j == i :
            j += i

        j -= m

        bitmap[j::i] = [False] * len(bitmap[j::i])

    if m <= 1 :
        bitmap[1 - m] = False

    if m <= 2 :
        bitmap[2 - m] = True

    return [m + i for i in range(d) if bitmap[i]]

def prime_generator() :
    '''A generator for the sequence of prime numbers.'''

    composites = {}

    yield 2

    for q in islice(count(3), 0, None, 2) :
        p = composites.pop(q, None)
        if p is None :
            composites[q * q] = q
            yield q
        else :
            x = p + q
            while x in composites or not x % 2 :
                x += p
            composites[x] = p

def primes(start = None, stop = None) :
    '''Computes all primes numbers within the given specifications.'''
    if start is None :
        return prime_generator()

    if stop is None :
        return primes_until(start)

    return primes_between(start, stop)

def polygonal_numbers(r) :
    '''Generates a sequence of all r-gonal numbers.'''

    term = 0
    for k in count(0) :
        yield term
        increment = k * r - 2 * k + 1
        term += increment

triangular_numbers = partial(polygonal_numbers, r = 3)
triangular_numbers.__doc__ = 'Generates a sequence of all triangular numbers.'
pentagonal_numbers = partial(polygonal_numbers, r = 5)
pentagonal_numbers.__doc__ = 'Generates a sequence of all pentagonal numbers.'
hexagonal_numbers = partial(polygonal_numbers, r = 6)
hexagonal_numbers.__doc__ = 'Generates a sequence of all hexagonal numbers.'

def polygonal_number(n, r) :
    '''Computes the nth r-gonal number.'''

    return n * ((n - 1) * r - 2 * (n - 2)) // 2

triangular_number = partial(polygonal_number, r = 3)
triangular_number.__doc__ = 'Computes the nth triangular number.'
pentagonal_number = partial(polygonal_number, r = 5)
pentagonal_number.__doc__ = 'Computes the nth pentagonal number.'
hexagonal_number = partial(polygonal_number, r = 6)
hexagonal_number.__doc__ = 'Computes the nth hexagonal number.'

def rationals(now = Fraction(0, 1)) :

    while True :
        now = Fraction(
            now.denominator,
            now.denominator * (now.numerator // now.denominator) +
            now.denominator - (now.numerator % now.denominator)
        )

        yield now

    return

def coprime_pairs(n, a = 1, b = 1) :
    yield (a, b)

    k = 1
    while a * k + b <= n :
        for i in coprime_pairs(n, a * k + b, a) :
            yield i

        k += 1

    return
