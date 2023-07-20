# * Question 1: Recursive Multiplication *
def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    return m + multiply(m, n - 1)



# * Question 4: Is Prime *
def is_prime(n):
    """ Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def divided_by(k):
        if k == 1:
            return True
        elif n % k == 0:
            return False
        else:
            return divided_by(k-1)
    if n == 1:
        return False
    else:
        return divided_by(n-1)



# * Question 5: Recursive Hailstone *
def hailstone(n):
    """ Print out the hailstone sequence starting at n, and return the number of elements in the sequence. 
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n == 1:
        return 1
    if n % 2:
        return hailstone(3 * n + 1) + 1
    else:
        return hailstone(n // 2) + 1



# * Question 6: Merge Numbers *
def merge(n1, n2):
    """ Merges two number by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge(21, 31)
    3211
    """
    if n1 == 0 or n2 == 0:
        return n1 + n2
    if n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10


        

