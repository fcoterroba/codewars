<?php

function encode(string $s): array
{
    $n = strlen($s);

    if ($n === 0) {
        return ["", 0];
    }

    $rotations = [];

    for ($i = 0; $i < $n; $i++) {
        $rotations[] = substr($s, $i) . substr($s, 0, $i);
    }

    $sorted = $rotations;
    sort($sorted, SORT_STRING);

    $lastColumn = '';
    $index = 0;

    foreach ($sorted as $i => $row) {
        $lastColumn .= $row[$n - 1];

        if ($row === $s) {
            $index = $i;
        }
    }

    return [$lastColumn, $index];
}

function decode(string $s, int $index): string
{
    $n = strlen($s);

    if ($n === 0) {
        return '';
    }

    $L = str_split($s);

    $counts = [];
    $ranks = [];

    foreach ($L as $c) {
        $counts[$c] = ($counts[$c] ?? 0) + 1;
        $ranks[] = $counts[$c];
    }

    $F = $L;
    sort($F, SORT_STRING);

    $counts = [];
    $first = [];

    foreach ($F as $i => $c) {
        $counts[$c] = ($counts[$c] ?? 0) + 1;
        $first[$c][$counts[$c]] = $i;
    }

    $next = [];

    foreach ($L as $i => $c) {
        $next[$i] = $first[$c][$ranks[$i]];
    }

    $result = array_fill(0, $n, '');
    $row = $index;

    for ($i = $n - 1; $i >= 0; $i--) {
        $result[$i] = $L[$row];
        $row = $next[$row];
    }

    return implode('', $result);
}

// original kata: https://www.codewars.com/kata/54ce4c6804fcc440a1000ecb
// my solution: https://www.codewars.com/kata/reviews/5f281ae5d3428e0001c96b0d/groups/6a33af8188b999fb7c7a2659
