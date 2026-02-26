<?php

function format_duration(int $seconds): string {
    if ($seconds === 0) return 'now';

    $units = [
        'year'   => 365 * 24 * 3600,
        'day'    => 24 * 3600,
        'hour'   => 3600,
        'minute' => 60,
        'second' => 1,
    ];

    $parts = [];
    foreach ($units as $name => $value) {
        if ($seconds >= $value) {
            $count = intdiv($seconds, $value);
            $seconds %= $value;
            $parts[] = "$count " . ($count > 1 ? "{$name}s" : $name);
        }
    }

    $last = array_pop($parts);
    return $parts ? implode(', ', $parts) . ' and ' . $last : $last;
}

// original kata: https://www.codewars.com/kata/52742f58faf5485cae000b9a
// my solution: https://www.codewars.com/kata/reviews/5a2e308b7a3bfc50df000d17/groups/699ffb6c2ac2aa768b4ff6b9
