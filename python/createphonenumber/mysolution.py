def create_phone_number(n):
    s = ''.join(str(d) for d in n)
    return f'({s[:3]}) {s[3:6]}-{s[6:]}'

# original kata: https://www.codewars.com/kata/525f50e3b73515a6db000b83
# my solution: https://www.codewars.com/kata/reviews/59b1a938182024506b00081d/groups/5ec961fac602900001c96232