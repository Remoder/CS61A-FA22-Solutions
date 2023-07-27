# * Question 2: Jacket Weather? *
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    return temp < 60 or raining



# * Question 4: Is Prime? * 
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1)
    False
    """
    k, tot = 0, 0
    while k <= n:
        k = k + 1
        if n % k == 0:
            tot += 1
    return tot == 2



# * Question 5: Fizzbuzz *
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    """
    i = 0
    while i < n:
        i = i + 1
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)



# * Question 6: Unique Digits *
def unique_digits(n):
    """ Return the number of unique digits in positive integer n.
    >>> unique_digits(8675309)
    7
    >>> unique_digits(1313131)
    2
    >>> unique_digits(13173131)
    3
    >>> unique_digits(10000)
    2
    >>> unique_digits(101)
    2
    >>> unique_digits(10)
    2
    """
    k, tot = 0, 0
    while k < 10:
        if has_digit(n, k):
            tot += 1
        k = k + 1
    return tot

def has_digit(n, k):
    """ Returns whether K is a digit in N.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    while n > 0:
        if k == n % 10:
            return True
        n = n // 10
    return False

            
