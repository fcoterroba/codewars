fn rental_car_cost(d: u32) -> u32 {
    let discount = match d {
        7..=u32::MAX => 50,
        3..=6 => 20,
        _ => 0,
    };
    40 * d - discount
}

// original kata: https://www.codewars.com/kata/568d0dd208ee69389d000016
// my solution: https://www.codewars.com/kata/reviews/6661687cdd6b07e17d41b817/groups/69149d249414ca9009196109