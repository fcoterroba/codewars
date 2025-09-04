<?php
function reverseWords($str) {
    return implode(' ', array_map('strrev', explode(' ', $str)));
}

// original kata: https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/php
// my solution: https://www.codewars.com/kata/reviews/5d17c71a5701e50001472c20/groups/674c5f397f355022c00603a4