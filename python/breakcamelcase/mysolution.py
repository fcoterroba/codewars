def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

# original kata: https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
# my solution: https://www.codewars.com/kata/reviews/5e444a24733cf90001396219/groups/5e4459ba284c32000194d950