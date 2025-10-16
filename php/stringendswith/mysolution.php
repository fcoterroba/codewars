<?php

function solution($str, $ending) {
    if ($ending === '') return true;
    if (strlen($ending) > strlen($str)) return false;
    return substr($str, -strlen($ending)) === $ending;
}

// original kata: https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d
// my solution: https://www.codewars.com/kata/reviews/5d46f8e957245b000139a0aa/groups/64e3f1e8b67d7100010e5534