def likes(names):
    n = len(names)
    if n == 0:
        return "no one likes this"
    elif n == 1:
        return f"{names[0]} likes this"
    elif n == 2:
        return f"{names[0]} and {names[1]} like this"
    elif n == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {n-2} others like this"

# original kata: https://www.codewars.com/kata/5266876b8f4bf2da9b000362
# my solution: https://www.codewars.com/kata/reviews/564425cc55d0e45b8c000087/groups/5d59cdd4d04619000197f2ce