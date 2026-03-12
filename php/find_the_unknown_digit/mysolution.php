<?php

function solve_expression(string $expression): int {
    preg_match_all('/\d/', $expression, $digitMatches);
    $usedDigits = array_unique($digitMatches[0]);

    $hasQuestionMark = str_contains($expression, '?');

    if (!$hasQuestionMark) {
        if (!preg_match('/^(-?\d+)([+\-*])(-?\d+)=(-?\d+)$/', $expression, $m)) {
            return -1;
        }
        $left = (int)$m[1];
        $op   = $m[2];
        $right = (int)$m[3];
        $result = (int)$m[4];

        $computed = match($op) {
            '+' => $left + $right,
            '-' => $left - $right,
            '*' => $left * $right,
        };

        return $computed === $result ? -1 : -1;
    }

    for ($digit = 0; $digit <= 9; $digit++) {
        if (in_array((string)$digit, $usedDigits, true)) {
            continue;
        }

        $candidate = str_replace('?', (string)$digit, $expression);

        if (!preg_match('/^(-?\d+)([+\-*])(-?\d+)=(-?\d+)$/', $candidate, $m)) {
            continue;
        }

        $left   = $m[1];
        $op     = $m[2];
        $right  = $m[3];
        $result = $m[4];

        foreach ([$left, $right, $result] as $num) {
            $abs = ltrim($num, '-');
            if (strlen($abs) > 1 && $abs[0] === '0') {
                continue 2;
            }
        }

        $left   = (int)$left;
        $right  = (int)$right;
        $result = (int)$result;

        $computed = match($op) {
            '+' => $left + $right,
            '-' => $left - $right,
            '*' => $left * $right,
        };

        if ($computed === $result) {
            return $digit;
        }
    }

    return -1;
}

// original kata: https://www.codewars.com/kata/546d15cebed2e10334000ed9
// my solution: https://www.codewars.com/kata/reviews/59bb71499fc229ca460002b8/groups/69b282d67714de131500765b
