def get_generation(cells: list[list[int]], generations: int) -> list[list[int]]:
    live = set()
    for r, row in enumerate(cells):
        for c, val in enumerate(row):
            if val == 1:
                live.add((r, c))
    
    for _ in range(generations):
        candidates = set()
        for r, c in live:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    candidates.add((r + dr, c + dc))
        
        next_live = set()
        for r, c in candidates:
            neighbors = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if (dr, dc) != (0, 0) and (r + dr, c + dc) in live:
                        neighbors += 1
            
            is_alive = (r, c) in live
            
            # Apply game rules
            if is_alive and neighbors in [2, 3]:
                next_live.add((r, c))
            elif not is_alive and neighbors == 3:
                next_live.add((r, c))
        
        live = next_live
    
    if not live:
        return [[]]
    
    min_r = min(r for r, c in live)
    max_r = max(r for r, c in live)
    min_c = min(c for r, c in live)
    max_c = max(c for r, c in live)
    
    result = []
    for r in range(min_r, max_r + 1):
        row = []
        for c in range(min_c, max_c + 1):
            row.append(1 if (r, c) in live else 0)
        result.append(row)
    
    return result

# original kata: https://www.codewars.com/kata/52423db9add6f6fc39000354
# my solution: https://www.codewars.com/kata/reviews/54a61ed837f43531e90000d0/groups/6969d6dae928d460096c0ff7