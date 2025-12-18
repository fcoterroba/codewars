<?php

function is_solved(array $board): int
{
    for ($i = 0; $i < 3; $i++) {
        // Check Row
        if ($board[$i][0] !== 0 && $board[$i][0] === $board[$i][1] && $board[$i][1] === $board[$i][2]) {
            return $board[$i][0];
        }
        if ($board[0][$i] !== 0 && $board[0][$i] === $board[1][$i] && $board[1][$i] === $board[2][$i]) {
            return $board[0][$i];
        }
    }

    if ($board[1][1] !== 0) {
        if (
            ($board[0][0] === $board[1][1] && $board[1][1] === $board[2][2]) ||
            ($board[0][2] === $board[1][1] && $board[1][1] === $board[2][0])
        ) {
            return $board[1][1];
        }
    }

    foreach ($board as $row) {
        if (in_array(0, $row, true)) {
            return -1;
        }
    }

    return 0;
}

// original kata: https://www.codewars.com/kata/525caa5c1bf619d28c000335
// my solution: https://www.codewars.com/kata/reviews/59c62fdc8ef0c07712000214/groups/6943b77ad0d5121c9cc5bb1f