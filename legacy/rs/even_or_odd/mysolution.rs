fn even_or_odd(number: i32) -> &'static str {
    if number % 2 == 0 {
        "Even"
    } else {
        "Odd"
    }
}

// original kata: https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
// my solution: https://www.codewars.com/kata/reviews/581e5bddbdff2d98a600006d/groups/64ec0b9a10bd73000117fdd2