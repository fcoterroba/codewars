<?php

function doubles($maxk, $maxn) {
    $s = 0.0;
    for ($k = 1; $k <= $maxk; $k++) {
        for ($n = 1; $n <= $maxn; $n++) {
            $s += 1 / ($k * pow($n + 1, 2 * $k));
        }
    }
    return $s;
}

// original kata: https://www.codewars.com/kata/56c04261c3fcf33f2d000534
// my solution: https://www.codewars.com/kata/reviews/57922354a50773651c000171/groups/6aaba8ccd26c34cc34ee2eca
