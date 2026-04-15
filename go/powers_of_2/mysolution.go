package kata

func PowersOfTwo(n int) []uint64 {
    result := make([]uint64, n+1)
    for i := range result {
        result[i] = 1 << uint(i)
    }
    return result
}

// original kata: https://www.codewars.com/kata/57a083a57cb1f31db7000028
// my solution: https://www.codewars.com/kata/reviews/62c5e8f3d969240001321456/groups/66e6873dc4066547c2e5c350
