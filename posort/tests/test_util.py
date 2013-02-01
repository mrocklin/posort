from posort.util import reverse_dict, key_to_cmp

def test_reverse_dict():
    d = {'a': (1, 2), 'b': (2, 3), 'c': ()}
    assert reverse_dict(d) == {1: {'a'}, 2: {'a', 'b'}, 3: {'b'}}

def test_key_to_cmp():
    key = lambda x: x
    cmp = key_to_cmp(key)
    assert cmp(2, 3) < 0
    assert cmp(2, 2) == 0
    assert cmp(3, 2) > 0
