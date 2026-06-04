<?php

function sudoku(array $puzzle): array {
    solve($puzzle);
    return $puzzle;
}

function solve(array &$grid): bool {
    foreach ($grid as $row => $cols) {
        foreach ($cols as $col => $val) {
            if ($val !== 0) continue;

            foreach (range(1, 9) as $num) {
                if (isValid($grid, $row, $col, $num)) {
                    $grid[$row][$col] = $num;
                    if (solve($grid)) return true;
                    $grid[$row][$col] = 0;
                }
            }

            return false;
        }
    }
    return true;
}

function isValid(array &$grid, int $row, int $col, int $num): bool {
    if (in_array($num, $grid[$row])) return false;

    for ($r = 0; $r < 9; $r++) {
        if ($grid[$r][$col] === $num) return false;
    }

    $br = intdiv($row, 3) * 3;
    $bc = intdiv($col, 3) * 3;
    for ($r = $br; $r < $br + 3; $r++) {
        for ($c = $bc; $c < $bc + 3; $c++) {
            if ($grid[$r][$c] === $num) return false;
        }
    }

    return true;
}

// original kata: https://www.codewars.com/kata/5296bc77afba8baa690002d7
// my solution: https://www.codewars.com/kata/reviews/59aeb94104020f745c000d97/groups/6a212cfdba2ec7e1e2b31d79
