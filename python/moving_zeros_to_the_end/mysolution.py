def move_zeros(lst):
    return lambda lst: sorted(lst, key=lambda x: x == 0)

# original kata: https://www.codewars.com/kata/52597aa56021e91c93000cb0
# my solution: https://www.codewars.com/kata/reviews/57cb52c733c32f4c48000076/groups/62c3e7671911440001a37e3c