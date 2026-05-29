def dig_pow(n, p):
    total = sum(int(d) ** (p + i) for i, d in enumerate(str(n)))
    return total // n if total % n == 0 else -1

# original kata: https://www.codewars.com/kata/5552101f47fc5178b1000050
# my solution: https://www.codewars.com/kata/reviews/555212a93254791a20000021/groups/5e46f968bffa5a00014a24aa
