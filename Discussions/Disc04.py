# * Question 1: Count Stair Ways *
def count_stair_ways(n):
    """ Return the number of ways to climb up a flight of n stairs,
    moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    if n == 0 or n == 1:
        return 1
    return count_stair_ways(n-1) + count_stair_ways(n-2)



# * Question 2: Count k *
def count_k(n, k):
    """ Countsthe number of paths up a flight of n stairs when 
    takin gup to and including k steps at a time.
    >>> count_k(3, 3)
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1)
    1
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    tot = 0
    for i in range(k):
        tot += count_k(n-i-1, k)
    return tot



# * Question 4: Even Weighted *
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[idx] * idx for idx in range(len(s)) if idx % 2 == 0]



# * Question 5: Max Product *
def max_product(s):
    """ Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10, 3, 1, 9, 2])
    90
    >>> max_product([5, 10, 5, 10, 5])
    125
    >>> max_product([])
    1
    """
    def mul(t):
        tmp = 1
        for i in t:
            tmp *= i
        return tmp

    ans = 1
    for stp in range(2, len(s)):
        ans = max(ans, mul([s[idx] for idx in range(0, len(s), stp)]))
    return ans
