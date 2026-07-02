<?php

function determinant(array $matrix): int {
    $n = count($matrix);

    if ($n === 1) {
        return $matrix[0][0];
    }

    if ($n === 2) {
        return $matrix[0][0] * $matrix[1][1] - $matrix[0][1] * $matrix[1][0];
    }

    $det = 0;
    $sign = 1;

    for ($col = 0; $col < $n; $col++) {
        $minor = getMinor($matrix, 0, $col);
        $det += $sign * $matrix[0][$col] * determinant($minor);
        $sign *= -1;
    }

    return $det;
}

function getMinor(array $matrix, int $rowToRemove, int $colToRemove): array {
    $minor = [];

    foreach ($matrix as $i => $row) {
        if ($i === $rowToRemove) {
            continue;
        }

        $newRow = [];
        foreach ($row as $j => $value) {
            if ($j === $colToRemove) {
                continue;
            }
            $newRow[] = $value;
        }

        $minor[] = $newRow;
    }

    return $minor;
}

// original kata: https://www.codewars.com/kata/52a382ee44408cea2500074c
// my solution: https://www.codewars.com/kata/reviews/5991c2973c5b647f3700002b/groups/6a463608617066463b148036
