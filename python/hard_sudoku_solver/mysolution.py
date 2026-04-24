def sudoku_solver(puzzle):
    for r in range(9):
        for c in range(9):
            v = puzzle[r][c]

    PEERS = {}
    for r in range(9):
        for c in range(9):
            p = set()
            for i in range(9):
                p.add((r, i)); p.add((i, c))
            br, bc = (r//3)*3, (c//3)*3
            for dr in range(3):
                for dc in range(3):
                    p.add((br+dr, bc+dc))
            p.discard((r, c))
            PEERS[(r, c)] = p

    def assign(values, r, c, d):
        other = values[(r, c)] - {d}
        for d2 in other:
            if not eliminate(values, r, c, d2):
                return False
        return True

    def eliminate(values, r, c, d):
        if d not in values[(r, c)]:
            return True
        values[(r, c)].discard(d)
        n = len(values[(r, c)])
        if n == 0:
            return False
        if n == 1:
            d2 = next(iter(values[(r, c)]))
            for pr, pc in PEERS[(r, c)]:
                if not eliminate(values, pr, pc, d2):
                    return False
        for unit in UNITS[(r, c)]:
            places = [(ur, uc) for ur, uc in unit if d in values[(ur, uc)]]
            if len(places) == 0:
                return False
            if len(places) == 1:
                if not assign(values, places[0][0], places[0][1], d):
                    return False
        return True

    UNITS = {}
    for r in range(9):
        for c in range(9):
            row_unit = [(r, i) for i in range(9)]
            col_unit = [(i, c) for i in range(9)]
            br, bc = (r//3)*3, (c//3)*3
            box_unit = [(br+dr, bc+dc) for dr in range(3) for dc in range(3)]
            UNITS[(r, c)] = [row_unit, col_unit, box_unit]

    def parse_grid(puzzle):
        values = {(r, c): set(range(1, 10)) for r in range(9) for c in range(9)}
        for r in range(9):
            for c in range(9):
                d = puzzle[r][c]
                if d != 0:
                    if not assign(values, r, c, d):
                        return False
        return values

    def solve(values, limit):
        if values is False:
            return []
        if all(len(values[(r, c)]) == 1 for r in range(9) for c in range(9)):
            return [values]
        _, r, c = min(
            (len(values[(r, c)]), r, c)
            for r in range(9) for c in range(9)
            if len(values[(r, c)]) > 1
        )
        results = []
        for d in values[(r, c)]:
            v2 = {k: s.copy() for k, s in values.items()}
            if assign(v2, r, c, d):
                results.extend(solve(v2, limit - len(results)))
            if len(results) >= limit:
                break
        return results

    for r in range(9):
        for c in range(9):
            val = puzzle[r][c]
            if val != 0:
                for pr, pc in PEERS[(r, c)]:
                    if puzzle[pr][pc] == val:
                        raise ValueError(f"Invalid gri: duplicated {val} in ({r},{c})")

    values = parse_grid(puzzle)

    solutions = solve(values, limit=2)

    if len(solutions) == 0:
        raise ValueError("This puzzle doesn't have solution")
    if len(solutions) >= 2:
        raise ValueError("This puzzle got multiple solutions")

    return [[next(iter(solutions[0][(r, c)])) for c in range(9)] for r in range(9)]

# original kata: https://www.codewars.com/kata/5588bd9f28dbb06f43000085
# my solution: https://www.codewars.com/kata/reviews/5589b8d78c114b4d5400002c/groups/69eb1a79e7bacf56952aaeee
