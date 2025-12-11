<?php

function solution($str) {
    if (empty($str)) {
        return [];
    }
    if (strlen($str) % 2 !== 0) {
        $str .= '_';
    }
    return str_split($str, 2);
}

// original kata: https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
// my solution: https://www.codewars.com/kata/reviews/57cb045535ef62f92d0000f1/groups/5e87fb9bce440600012d0410