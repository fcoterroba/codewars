fn is_square(n: i64) -> bool {
    let sqrt = (n as f64).sqrt() as i64;
    sqrt * sqrt == n || (sqrt + 1) * (sqrt + 1) == n
}

// original kata: https://www.codewars.com/kata/54c27a33fb7da0db0100040e
// my solution: https://www.codewars.com/kata/reviews/62b09d861d88d8000140e746/groups/69708a331ad9fa17470c3a3f