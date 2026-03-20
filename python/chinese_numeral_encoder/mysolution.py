from preloaded import numerals


def to_chinese_numeral(n):
    digits = '零一二三四五六七八九'
    units = [(10000,'万'),(1000,'千'),(100,'百'),(10,'十')]

    def int_to_chinese(n):
        if n == 0: return '零'
        res, prev_zero = '', False
        for val, char in units:
            if n >= val:
                d, n = divmod(n, val)
                res += ('零' if prev_zero else '') + ('' if res == '' and d == 1 and val == 10 else digits[d]) + char
                prev_zero = False
            elif res:
                prev_zero = True
        if n: res += ('零' if prev_zero else '') + digits[n]
        return res

    neg = n < 0
    s = f'{abs(n):.8f}'.rstrip('0').rstrip('.')
    i, *d = s.split('.')
    res = int_to_chinese(int(i)) + ('点' + ''.join(digits[int(c)] for c in d[0]) if d else '')
    return ('负' if neg else '') + res

# original kata: https://www.codewars.com/kata/52608f5345d4a19bed000b31
# my solution: https://www.codewars.com/kata/reviews/5ec28cda52dd7a0001f33510/groups/69bd11e4e3b935231f937a6d
