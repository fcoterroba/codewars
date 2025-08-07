<?php

function detect_pangram($string)
{
    $alphabet = range('a', 'z');
    $string = strtolower($string);

    foreach ($alphabet as $letter) {
        if (strpos($string, $letter) === false) {
            return false;
        }
    }
    return true;
}

// original kata: https://www.codewars.com/kata/545cedaa9943f7fe7b000048
// my solution: https://www.codewars.com/kata/reviews/5e5fceb44013f000019872a9/groups/68944628475cd5cf878a8540