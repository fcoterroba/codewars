fn digitize(n: u64) -> Vec<u8> {
    n.to_string().chars().rev().map(|c| c.to_digit(10).unwrap() as u8).collect()
}

// original kata: https://www.codewars.com/kata/5583090cbe83f4fd8c000051
// my solution: https://www.codewars.com/kata/reviews/5e42dbd090bbd20001e5810f/groups/5e4ac44577d51a0001da2c1b