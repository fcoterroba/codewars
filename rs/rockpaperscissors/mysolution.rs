fn rps(p1: &str, p2: &str) -> &'static str  {
    match (p1, p2) {
        ("rock", "scissors") => "Player 1 won!",
        ("scissors", "rock") => "Player 2 won!",
        ("paper", "rock") => "Player 1 won!",
        ("rock", "paper") => "Player 2 won!",
        ("scissors", "paper") => "Player 1 won!",
        ("paper", "scissors") => "Player 2 won!",
        _ => "Draw!",
    }
}

// original kata: https://www.codewars.com/kata/5672a98bdbdd995fad00000f
// my solution: https://www.codewars.com/kata/reviews/62ba5a97afd1270001ed845f/groups/65259bef6a585b0001ec2622