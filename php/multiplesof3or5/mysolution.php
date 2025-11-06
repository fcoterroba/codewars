<?php

function solution(int $number): int
{
    $result = 0;
    for ($i = 3; $i < $number; $i++) {
        if ($i % 3 === 0 || $i % 5 === 0) {
            $result += $i;
        }
    }
    return $result;
}

// original kata: https://www.codewars.com/kata/514b92a657cdc65150000006
// my solution: https://www.codewars.com/kata/reviews/578840b8ea6a1ce290000002/groups/690c4c30b55cd112489915fb