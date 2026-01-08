<?php

function convertFrac(array $lst): string {
    if (empty($lst)) {
        return "";
    }

    $gcd = function (int $a, int $b): int {
        while ($b !== 0) {
            $a %= $b;
            [$a, $b] = [$b, $a];
        }
        return $a;
    };

    $lcm = function (int $a, int $b) use ($gcd): int {
        return ($a === 0 || $b === 0) ? 0 : (int)abs(($a / $gcd($a, $b)) * $b);
    };

    $simplified = array_map(function ($f) use ($gcd) {
        $common = $gcd($f[0], $f[1]);
        return [(int)($f[0] / $common), (int)($f[1] / $common)];
    }, $lst);

    $commonDenom = array_reduce($simplified, function ($acc, $f) use ($lcm) {
        return $lcm($acc, $f[1]);
    }, 1);

    return array_reduce($simplified, function ($acc, $f) use ($commonDenom) {
        $newNumerator = $f[0] * ($commonDenom / $f[1]);
        return $acc . "($newNumerator,$commonDenom)";
    }, "");
}

// original kata: https://www.codewars.com/kata/54d7660d2daf68c619000d95
// my solution: https://www.codewars.com/kata/reviews/5794bf2a1051be6bd800003d/groups/695f61eaa535086eee92fce8