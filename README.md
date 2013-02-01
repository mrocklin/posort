Partially Ordered Sort
======================

An algorithm to sort a collection by a sequence of comparators.

Comparators
-----------

A comparator takes two elements `a` and `b` and returns
    
    `0` - if they are equal
    a positive number if `a > b`
    a negative number if `a < b`

For example the natural comparator on the integers is 

    def small_first(a, b):
        return a - b

The Python `sort` function takes a comparator function as a keyword input

    >>> sort((1,5,2,4,3), cmp=small_first)
    (1, 2, 3, 4, 5)

We may choose to sort by different criteria.  For example we might choose to
prefer even numbers

    def evens_first(a, b):
        return a%2 - b%2
    
    >>> sort((1, 5, 2, 4, 3), cmp=evens_first)
    (4, 2, 5, 1, 3)

Note in the example above that all of even numbers precede all of the odd numbers; `cmp` is satisfied.  Also note that there are several possible solutions.  For example we may want even numbers to precede odd numbers and, given extra freedom, smaller numbers to precede larger ones.

`posort`
--------

The `posort` function attempts to satisfy a sequence of comparator functions of decreasing precedence.

    >>> posort((1, 5, 2, 4, 3), evens_first, small_first)
    (2, 4, 1, 3, 5)

The rule for even numbers dominates the rule for small numbers. 


Equivalent structures
---------------------

A comparator function completely specifies a 
[partial order](http://en.wikipedia.org/wiki/Partial_order#Formal_definition).  

A comparator function can describe any 
[directed acyclic graph (DAG)](http://en.wikipedia.org/wiki/Directed_acyclic_graph)
