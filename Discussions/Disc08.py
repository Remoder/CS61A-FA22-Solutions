# * Question 3: Sum Nums *
def sum_nums(s):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    res = 0
    while s is not Link.empty:
        res += s.first
        s = s.rest
    return res



# * Question 4: Multiply Links *
def DEBUG(lst_of_lnks):
    for link in lst_of_lnks:
        print(link)

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first 
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    res = Link(1)
    for link in lst_of_lnks:
        if link is Link.empty:
            return Link.empty
        res.first = res.first * link.first
    res.rest = multiply_lnks([link.rest for link in lst_of_lnks])
    return res



# * Question 5: Flip Two *
def recursive_flip_two(s):
    """
    >>> one_lnk = Link(1)
    >>> recursive_flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> recursive_flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if s.rest is not Link.empty:
        s.first, s.rest.first = s.rest.first, s.first
        recursive_flip_two(s.rest.rest)

def iterative_flip_two(s):
    """
    >>> one_lnk = Link(1)
    >>> iterative_flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> iterative_flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    while True:
        if s.rest is not Link.empty:
            s.first, s.rest.first = s.rest.first, s.first
            s = s.rest.rest
        else:
            break



# * Question 6: Make Even *
def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    t.label += t.label % 2
    if not t.is_leaf():
        for sub_tree in t.branches:
            make_even(sub_tree)



# * Question 7: Add Leaves *
def add_d_leaves(t, v):
    """ 
    >>> t_one_to_four = Tree(1, [Tree(2), Tree(3, [Tree(4)])])
    >>> print(t_one_to_four)
    1
      2
      3
        4
    >>> add_d_leaves(t_one_to_four, 5)
    >>> print(t_one_to_four)
    1
      2
        5
      3
        4
          5
          5
        5

    >>> t1 = Tree(1, [Tree(3)])
    >>> add_d_leaves(t1, 4)
    >>> t1
    Tree(1, [Tree(3, [Tree(4)])])
    >>> t2 = Tree(2, [Tree(5), Tree(6)])
    >>> t3 = Tree(3, [t1, Tree(0), t2])
    >>> print(t3)
    3
      1
        3
          4
      0
      2
        5
        6
    >>> add_d_leaves(t3, 10)
    >>> print(t3)
    3
      1
        3
          4
            10
            10
            10
          10
          10
        10
      0
        10
      2
        5
          10
          10
        6
          10
          10
        10
    """
    def inner(t, depth):
        for sub_tree in t.branches:
            inner(sub_tree, depth+1)
        for _ in range(depth):
            if t.branches:
                t.branches.append(Tree(v))
            else:
                t.branches = [Tree(v)]
    inner(t, 0)




# * Link Class *
class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
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



# * Tree Class *
class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches
    
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + '\n'
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()
            

