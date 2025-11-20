<?php

function alphabet_position(string $s): string
{
    $positions = [];
    $s = strtolower($s);
    for ($i = 0; $i < strlen($s); $i++) {
        $character = $s[$i];
        if (ctype_alpha($character)) {
            $positions[] = ord($character) - ord('a') + 1;
        }
    }
    return implode(' ', $positions);
}

// original kata: https://www.codewars.com/kata/546f922b54af40e1e90001da
// my solution: https://www.codewars.com/kata/reviews/59b3c8bfd0ca2d061400014d/groups/691eaec4c0db6464e10419ba