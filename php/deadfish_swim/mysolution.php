<?php

function parse($data) {
    $value = 0;
    $output = [];
    for ($i = 0, $len = strlen($data); $i < $len; ++$i) {
        switch ($data[$i]) {
            case 'i': ++$value; break;
            case 'd': --$value; break;
            case 's': $value *= $value; break;
            case 'o': $output[] = $value; break;
        }
    }
    return $output;
}

// original kata: https://www.codewars.com/kata/51e0007c1f9378fa810002a9
// my solution: https://www.codewars.com/kata/reviews/5b8e53645a5f104129000811/groups/69313df175d405af6a53cc9f