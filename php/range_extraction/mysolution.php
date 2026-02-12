<?php

function solution(array $list): string
{
    if (empty($list)) {
        return '';
    }
    $ranges = [];
    $start = $list[0];
    $end = $list[0];
    for ($i = 1; $i <= count($list); $i++) {
        if ($i === count($list) || $list[$i] !== $end + 1) {
            if ($end - $start >= 2) {
                $ranges[] = "{$start}-{$end}";
            } else {
                for ($j = $start; $j <= $end; $j++) {
                    $ranges[] = $j;
                }
            }
            if ($i < count($list)) {
                $start = $list[$i];
                $end = $list[$i];
            }
        } else {
            $end = $list[$i];
        }
    }
    return implode(',', $ranges);
}

// original kata: https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
// my solution: https://www.codewars.com/kata/reviews/6131e2b4b5d9660001880080/groups/698d9aea1b15258cdd56958a