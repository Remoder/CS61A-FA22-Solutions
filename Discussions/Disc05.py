# * Question 1: Map, Filter, Reduce * 
def my_map(fn, seq):
    """ Applies fn onto each element in seq and returns a list.
    >>> my_map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    """
    return [fn(x) for x in seq]

def my_filter(pred, seq):
    """ Keeps elements in seq only if they satisfy pred.
    >>> my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [2, 4]
    """
    return [x for x in seq if pred(x)]

def my_reduce(combiner, seq):
    """ Combines elements in seq using combiner.
    seq will have at least one element.
    >>> my_reduce(lambda x, y: x + y, [1, 2, 3, 4])
    10
    >>> my_reduce(lambda x, y: x * y, [1, 2, 3, 4])
    24
    >>> my_reduce(lambda x, y: x * y, [4])
    4
    >>> my_reduce(lambda x, y: x + 2 * y, [1, 2, 3])
    11
    """
    res = seq[0]
    for idx in range(1, len(seq)):
        res = combiner(res, seq[idx])
    return res



# * Question 2: Count Palindromes *
def count_palindromes(L):
    """ The number of palindromic strings in the sequence of strings
    L (ignoring case).
    >>> count_palindromes(("Acme", "Madam", "Pivot", "Pip"))
    2
    >>> count_palindromes(["101", "rAcECaR", "much", "wow"])
    3
    """
    return my_reduce(lambda x, y: x + y, my_map(lambda word: 1 if word.lower() == word.lower()[::-1] else 0, L))



# * Tree Data Abstraction Implementation *
def tree(label, branches=[]):
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)



# * Question 4: Height * 
def height(t):
    """ Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
    >>> height(t)
    3
    """
    if is_leaf(t):
        return 0
    return max([height(sub_tree) for sub_tree in branches(t)]) + 1



# * Question 5: Maximum Path Sum *
def max_path_sum(t):
    """ Return the maximum path sum of the tree. 
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return label(t)
    return max([max_path_sum(sub_tree) for sub_tree in branches(t)]) + label(t)



# * Question 6: Find Path * 
def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    """
    if is_leaf(t):
        return [label(t)]
    for sub_tree in branches(t):
        path = [label(t)] + list(find_path(sub_tree, x))
        if path[-1] == x:
            return path



# * Question 7: Perfectly Balanced * 
def sum_tree(t):
    """ Add all elements in a tree.
    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    return label(t) + sum([sum_tree(sub_tree) for sub_tree in branches(t)])

def balanced(t):
    """ Checks if each branch has same sum of all elements and
    if each branch is banlanced.
    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    res = [sum_tree(sub_tree) for sub_tree in branches(t) if balanced(sub_tree)]
    return len(res) == len(branches(t)) and (len(res) == 0 or min(res) == max(res))



# * Question 8: Hailstone Tree *
def hailstone_tree(n, h):
    """ Generates a tree of hailstone numbers that will reach N, with height H.
    >>> print_tree(hailstone_tree(1, 0))
    1
    >>> print_tree(hailstone_tree(1, 4))
    1
        2
            4
                8
                    16
    >>> print_tree(hailstone_tree(8, 3))
    8
        16
            32
                64
            5
                10
    """
    if h == 0:
        return tree(n)
    branches = [hailstone_tree(2 * n, h - 1)]
    if (n - 1) % 3 == 0 and (n - 1) // 3 % 2 != 0 and (n - 1) // 3 > 1:
        branches += [hailstone_tree((n - 1) // 3, h - 1)]
    return tree(n, branches)

def print_tree(t):
    def helper(i, t):
        print("    " * i + str(label(t)))
        for b in branches(t):
            helper(i + 1, b)
    helper(0, t)
