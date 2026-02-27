from itertools import permutations as _permutations

def permutations(s):
    return sorted(set(''.join(p) for p in _permutations(s)))

// original kata: https://www.codewars.com/kata/5254ca2719453dcc0b00027d
// my solution: https://www.codewars.com/kata/reviews/555acc3335d4c449750001b5/groups/69a14dc745ea47da82621196
