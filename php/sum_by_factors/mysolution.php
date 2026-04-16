<?php

function sumOfDivided($lst) {
    if (empty($lst)) return [];

    $result = [];
    $max = max(array_map('abs', $lst));

    for ($p = 2; $p <= $max; $p++) {
        $prime = $p >= 2;
        for ($i = 2; $i <= sqrt($p) && $prime; $i++) {
            if ($p % $i === 0) $prime = false;
        }
        if (!$prime) continue;

        $divisibles = array_filter($lst, fn($n) => $n % $p === 0);
        if (!empty($divisibles)) {
            $result[] = [$p, array_sum($divisibles)];
        }
    }

    return $result;
}

// original kata: https://www.codewars.com/kata/54d496788776e49e6b00052f
// my solution: https://www.codewars.com/kata/reviews/57946f4ef895cb6dcb000172/groups/69e087d569ec8d914321bfd0
