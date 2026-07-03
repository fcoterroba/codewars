def cut(cake):
    cake = cake.strip('\n')
    rows = cake.split('\n')
    H = len(rows)
    W = len(rows[0])
    raisins = [(r, c) for r in range(H) for c in range(W) if rows[r][c] == 'o']
    n = len(raisins)
    total_area = H * W

    if n == 0 or total_area % n != 0:
        return []
    unit = total_area // n

    def raisins_in(r0, r1, c0, c1):
        return [(r, c) for (r, c) in raisins if r0 <= r < r1 and c0 <= c < c1]

    memo = {}

    def solve(r0, r1, c0, c1):
        key = (r0, r1, c0, c1)
        if key in memo:
            return memo[key]

        rs = raisins_in(r0, r1, c0, c1)
        k = len(rs)
        area = (r1 - r0) * (c1 - c0)
        result = []

        if k == 0:
            result = []
        elif k == 1:
            result = [[(r0, r1, c0, c1)]] if area == unit else []
        else:
            if area == k * unit:
                for c in range(c0 + 1, c1):
                    leftR = [p for p in rs if p[1] < c]
                    rightR = [p for p in rs if p[1] >= c]
                    if not leftR or not rightR:
                        continue
                    leftArea = (r1 - r0) * (c - c0)
                    rightArea = (r1 - r0) * (c1 - c)
                    if leftArea == len(leftR) * unit and rightArea == len(rightR) * unit:
                        for ls in solve(r0, r1, c0, c):
                            for rsn in solve(r0, r1, c, c1):
                                result.append(ls + rsn)
                for r in range(r0 + 1, r1):
                    topR = [p for p in rs if p[0] < r]
                    botR = [p for p in rs if p[0] >= r]
                    if not topR or not botR:
                        continue
                    topArea = (r - r0) * (c1 - c0)
                    botArea = (r1 - r) * (c1 - c0)
                    if topArea == len(topR) * unit and botArea == len(botR) * unit:
                        for ts in solve(r0, r, c0, c1):
                            for bs in solve(r, r1, c0, c1):
                                result.append(ts + bs)

        memo[key] = result
        return result

    all_solutions = solve(0, H, 0, W)
    if not all_solutions:
        return []

    best = None
    best_key = None
    for sol in all_solutions:
        ordered = sorted(sol, key=lambda rect: (rect[0], rect[2]))
        widths_key = tuple(rect[3] - rect[2] for rect in ordered)
        if best_key is None or widths_key > best_key:
            best_key = widths_key
            best = ordered

    return ['\n'.join(rows[r][c0:c1] for r in range(r0, r1)) for (r0, r1, c0, c1) in best]

# original kata: https://www.codewars.com/kata/586214e1ef065414220000a8
# my solution: https://www.codewars.com/kata/reviews/5a93b5df8cf4849b8c0022c2/groups/6a47a6e676bc2e73bec9bc27
