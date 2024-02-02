# * Question 1: Paths List *
def paths(x, y):
    """ Return a list of ways to reach y from x by reapeated
    incrementing or doubling.
    >>> paths(3, 5)
    [[3, 4, 5]]
    >>> sorted(paths(3, 6))
    [[3, 4, 5, 6], [3, 6]]
    >>> sorted(paths(3, 9))
    [[3, 4, 5, 6, 7, 8, 9], [3, 4, 8, 9], [3, 6, 7, 8, 9]]
    >>> paths(3, 3)
    [[3]]
    >>> paths(5, 3)
    []
    """
    if x > y:
        return []
    elif x == y:
        return [[x]]
    else:
        a = list(map(lambda lst: [x] + lst, paths(x+1, y)))
        b = list(map(lambda lst: [x] + lst, paths(x*2, y)))
        return a + b



# * Question 2: Reverse *
def reverse(lst):
    """ Reverse lst using mutation.
    >>> original_list = [5, -1, 29, 0]
    >>> reverse(original_list)
    >>> original_list
    [0, 29, -1, 5]
    >>> odd_list = [42, 72, -8]
    >>> reverse(odd_list)
    >>> odd_list
    [-8, 72, 42]
    """
    for i in range(1, len(lst)+1):
        lst[:-i], lst[-i] = lst[1:(-i+1 if -i+1 else None)], lst[0]



# * Tree Data Abstraction Implementation *
class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)
    
    def is_leaf(self):
        return not self.branches



# * Question 3: Widest Level *
def widest_level(t):
    """ Returns the elements at the depth with the most elements.
    >>> sum([[1], [2]], [])
    [1, 2]
    >>> t = Tree(3, [Tree(1, [Tree(1), Tree(5)]),
    ...              Tree(4, [Tree(9, [Tree(2)])])])
    >>> widest_level(t)
    [1, 5, 9]
    """
    levels = []
    x = [t]
    while x:
        levels.append([t.label for t in x])
        x = sum([t.branches for t in x], [])
    return max(levels, key=len)



# * Question 4: In-order Traversal *
def in_order_traversal(t):
    """ Generator function that generates an "in-order" traversal,
    assuming that each node has either 0 or 2 branches.
    >>> t = Tree(1, [Tree(2, [Tree(4), Tree(5, [Tree(6), Tree(7)])]), Tree(3)])
    >>> list(in_order_traversal(t))
    [4, 2, 6, 5, 7, 1, 3]
    """
    yield from in_order_traversal(t.branches[0]) if not t.is_leaf() else ()
    yield t.label
    yield from in_order_traversal(t.branches[1]) if not t.is_leaf() else ()



# * Linked Lists Data Abstraction Implementation *
class Link:
    empty = ()
    
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    
    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'
    
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'



# * Question 5: Deep Map *
def deep_map(f, link):
    """ Return a Link with the same structure as link but with fn mapped over 
    its element. If an element is an instance of a linked List, recursively 
    apply fn inside that list as well.
    >>> s = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(deep_map(lambda x: x * x, s))
    <1 <4 9> 16>
    >>> print(s)
    <1 <2 3> 4>
    >>> print(deep_map(lambda x: 2 * x, Link(s, Link(Link(Link(5))))))
    <<2 <4 6> 8> <<10>>>
    """
    if not link:
        return Link.empty
    if not isinstance(link.first, Link):
        return Link(f(link.first), deep_map(f, link.rest))
    else:
        return Link(deep_map(f, link.first), deep_map(f, link.rest))



# * Question 6: Repeated *
def repeated(f):
    """ Yields functions that are repeated applications of a one-argument function f.
    The first function yielded should apply f 0 times, while the second one apply f once, etc.
    >>> double = lambda x: 2 * x
    >>> funcs = repeated(double)
    >>> identity = next(funcs)
    >>> double = next(funcs)
    >>> quad = next(funcs)
    >>> oct = next(funcs)
    >>> quad(1)
    4
    >>> oct(1)
    8
    >>> [g(1) for _, g in zip(range(5), repeated(lambda x: 2 * x))]
    [1, 2, 4, 8, 16]
    """
    g = lambda x: x
    while True:
        yield g
        g = (lambda y: lambda x: f(y(x))) (g)
        # g = lambda x: f(g(x)) #
        # In this way, g() will call itself, causing error. #
