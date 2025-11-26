fn get_age(age: &str) -> u32 {
    age.chars().next().unwrap().to_digit(10).unwrap()
}

// original kata: https://www.codewars.com/kata/557cd6882bfa3c8a9f0000c1
// my solution: https://www.codewars.com/kata/reviews/59a66a9418e0db7dac001944