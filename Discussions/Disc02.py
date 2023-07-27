# * Question 5: Make Keeper *
def make_keeper(n):
    """Returns a function which takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def inner(f):
        k = 0
        while k < n:
            k = k + 1
            if f(k):
                print(k)
    return inner



# * Question 6: Make Your Own Lambdas *
def f1():
    """
    >>> f1()
    3
    """
    return 3

def f2():
    """
    >>> f2()()
    3
    >>>
    """
    return lambda: 3

def f3():
    """
    >>> f3()(3)
    3
    """
    return lambda x: x

def f4():
    """
    >>> f4()()(3)()
    3
    """
    return lambda: lambda x: lambda: x



# * Question 8: Match Maker *
def match_k(k):
    """ Return a function that checks if digits k apart match
    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(21111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def inner(n):
        i = 0
        while pow(10, i + k) <= n:
            if n // pow(10, i) % 10 != n // pow(10, i + k) % 10:
                return False
            i = i + 1
        return True
    return inner
