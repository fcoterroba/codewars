def beeramid(bonus, price):
    cans = bonus // price
    level = 0
    while cans >= (level + 1)**2:
        level += 1
        cans -= level**2
    return level

# original kata: https://www.codewars.com/kata/51e04f6b544cf3f6550000c1
# my solution: https://www.codewars.com/kata/reviews/5b1c43c073bf59625c0006fb/groups/5ea6969ca52d7e000156f575