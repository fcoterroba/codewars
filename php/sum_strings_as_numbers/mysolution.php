<?php

function sum_strings(string $a, string $b): string
{
    $i = strlen($a) - 1;
    $j = strlen($b) - 1;
    $carry = 0;
    $result = '';

    while ($i >= 0 || $j >= 0 || $carry) {
        $carry += ($i >= 0 ? $a[$i--] : 0) + ($j >= 0 ? $b[$j--] : 0);
        $result = ($carry % 10) . $result;
        $carry = intdiv($carry, 10);
    }

    return ltrim($result, '0') ?: '0';
}

// original kata: https://www.codewars.com/kata/5324945e2ece5e1f32000370
// my solution: https://www.codewars.com/kata/reviews/57bb88c87188e11b930001ba/groups/6968abf2ad72ad7cbc5a4793