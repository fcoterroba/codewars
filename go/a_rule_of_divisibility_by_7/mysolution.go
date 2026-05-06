package kata

func Seven(n int64) []int {
    steps := 0

    for n >= 100 {
        lastDigit := n % 10
        rest := n / 10
        n = rest - 2*lastDigit
        steps++
    }

    return []int{int(n), steps}
}

// original kata: https://www.codewars.com/kata/55e6f5e58f7817808e00002e
// my solution: https://www.codewars.com/kata/reviews/5c28c99d7fe79c00012c6d90/groups/681b18d20fae3cc60d043317
