from fractions import Fraction


def equal_to_24(a, b, c, d):

    nums = [
        (Fraction(a), str(a)),
        (Fraction(b), str(b)),
        (Fraction(c), str(c)),
        (Fraction(d), str(d)),
    ]

    def solve(arr):

        n = len(arr)

        if n == 1:
            if arr[0][0] == 24:
                return arr[0][1]
            return None

        for i in range(n):

            for j in range(i + 1, n):

                x, sx = arr[i]
                y, sy = arr[j]

                rest = [
                    arr[k]
                    for k in range(n)
                    if k != i and k != j
                ]

                candidates = [
                    (x + y, f"({sx}+{sy})"),
                    (x - y, f"({sx}-{sy})"),
                    (y - x, f"({sy}-{sx})"),
                    (x * y, f"({sx}*{sy})"),
                ]

                if y:
                    candidates.append(
                        (x / y, f"({sx}/{sy})")
                    )

                if x:
                    candidates.append(
                        (y / x, f"({sy}/{sx})")
                    )

                for val, expr in candidates:

                    res = solve(rest + [(val, expr)])

                    if res:
                        return res

        return None

    ans = solve(nums)

    return ans if ans else "It's not possible!"

# original kata: https://www.codewars.com/kata/574e890e296e412a0400149c
# my solution: https://www.codewars.com/kata/reviews/5d68569a14e5030001badc61/groups/69fd9465c9224b4977eeb6de
