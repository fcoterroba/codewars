from itertools import permutations as _permutations

def permutations(s):
    return sorted(set(''.join(p) for p in _permutations(s)))
