package kata

import (
    "strconv"
    "strings"
)

func NbDig(n int, d int) int {
    count := 0
    digit := strconv.Itoa(d)
    for k := 0; k <= n; k++ {
        count += strings.Count(strconv.Itoa(k*k), digit)
    }
    return count
}

// original kata: https://www.codewars.com/kata/566fc12495810954b1000030
// my solution: https://www.codewars.com/kata/reviews/5c263b2f2bb8430001810948/groups/69e87196403726b59f5aeb4e
