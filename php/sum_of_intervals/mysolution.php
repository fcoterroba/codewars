<?php

function sum_intervals(array $intervals): int {
    usort($intervals, fn($a, $b) => $a[0] <=> $b[0]);

    $sum = 0;
    $current_start = $intervals[0][0];
    $current_end   = $intervals[0][1];

    for ($i = 1; $i < count($intervals); $i++) {
        [$start, $end] = $intervals[$i];

        if ($start <= $current_end) {
            $current_end = max($current_end, $end);
        } else {
            $sum += $current_end - $current_start;
            $current_start = $start;
            $current_end   = $end;
        }
    }

    $sum += $current_end - $current_start;

    return $sum;
}

// original kata: https://www.codewars.com/kata/52b7ed099cdc285c300001cd
// my solution: https://www.codewars.com/kata/reviews/59946696d433e79e10000021/groups/69e9c20097c6200725381d27
