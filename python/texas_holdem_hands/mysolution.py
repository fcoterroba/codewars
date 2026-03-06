from itertools import combinations
from collections import Counter

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
RANK_VAL = {r: i for i, r in enumerate(RANKS)}
HAND_RANK = {
    "straight-flush": 8, "four-of-a-kind": 7, "full house": 6, "flush": 5, "straight": 4, "three-of-a-kind": 3, "two pair": 2, "pair": 1, "nothing": 0
}

def hand(hole_cards: list[str], community_cards: list[str]) -> tuple[str, list[str]]:
    def evaluate(cards):
        ranks_sorted = sorted((RANK_VAL[c[:-1]] for c in cards), reverse=True)
        suits = [c[-1] for c in cards]
        is_flush = len(set(suits)) == 1
        is_straight = ranks_sorted == list(range(ranks_sorted[0], ranks_sorted[0] - 5, -1))
        counts = Counter(ranks_sorted)
        groups = sorted(counts, key=lambda r: (counts[r], r), reverse=True)
        gc = [counts[r] for r in groups]
        gn = [RANKS[r] for r in groups]
        all_ranks = [RANKS[r] for r in ranks_sorted]
        match gc:
            case _ if is_straight and is_flush: 
                return "straight-flush", all_ranks
            case [4, *_]:
                return "four-of-a-kind", gn
            case [3, 2]:
                return "full house", gn
            case _ if is_flush:
                return "flush", all_ranks
            case _ if is_straight:
                return "straight", all_ranks
            case [3, *_]:
                return "three-of-a-kind", gn
            case [2, 2, *_]:
                return "two pair", gn
            case [2, *_]:
                return "pair", gn
            case _:
                return "nothing", all_ranks

    return max(
        (evaluate(combo) for combo in combinations(hole_cards + community_cards, 5)),
        key=lambda e: (HAND_RANK[e[0]], [RANK_VAL[r] for r in e[1]])
    )

# original kata: https://www.codewars.com/kata/524c74f855025e2495000262
# my solution: https://www.codewars.com/kata/reviews/61263db4c759a0000115e0b4/groups/69aa8865c66e789bda876b4d
