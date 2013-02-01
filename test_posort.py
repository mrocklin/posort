from dagsort import reverse_dict, toposort, posort


def test_reverse_dict():
    d = {'a': (1, 2), 'b': (2, 3), 'c': ()}
    assert reverse_dict(d) == {1: {'a'}, 2: {'a', 'b'}, 3: {'b'}}


def test_toposort():
    edges = {1: set((4, 6, 7)), 2: set((4, 6, 7)),
             3: set((5, 7)),    4: set((6, 7)), 5: set((7,))}
    order = toposort(edges)
    assert not any(a in edges.get(b, ()) for i, a in enumerate(order)
                                         for b    in order[i:])


def test_posort_easy():
    nodes = "asdfghjkl"

    def cmp(a, b):
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0

    assert posort(nodes, cmp) == list("adfghjkls")


def test_posort():
    l = range(1, 20)
    cmps = [lambda a, b: a % 10 - b % 10,
            lambda a, b: (a / 10) % 2 - (b / 10) % 2,
            lambda a, b: a - b]
    assert posort(l, *cmps) == \
            [10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19]
