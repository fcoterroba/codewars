fn better_than_average(class_points: &[u16], your_points: u16) -> bool {
    let sum: u16 = class_points.iter().sum();
    let average = sum / class_points.len() as u16;
    your_points > average
}

// original kata: https://www.codewars.com/kata/5601409514fc93442500010b
// my solution: https://www.codewars.com/kata/reviews/67dd1436f72017e870178ce5/groups/680e40cef7b38eab942f471f