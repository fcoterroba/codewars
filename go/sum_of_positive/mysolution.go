package kata

func PositiveSum(numbers []int) int {
    sum := 0
    for _, n := range numbers {
        if n > 0 {
            sum += n
        }
    }
    return sum
}

// original kata: https://www.codewars.com/kata/5715eaedb436cf5606000381
// my solution: https://www.codewars.com/kata/reviews/5ace283463990d6aeb001367/groups/5ad24e671c8578a0e4000166
