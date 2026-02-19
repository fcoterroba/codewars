<?php

function part($n) {
    $products = [];
    
    $stack = [[$n, $n, 1]];
    
    while (!empty($stack)) {
        [$remaining, $maxPart, $currentProduct] = array_pop($stack);
        
        if ($remaining === 0) {
            $products[$currentProduct] = true;
            continue;
        }
        
        $limit = min($remaining, $maxPart);
        for ($i = $limit; $i >= 1; $i--) {
            $stack[] = [$remaining - $i, $i, $currentProduct * $i];
        }
    }
    
    $prod = array_keys($products);
    sort($prod);
    
    $count = count($prod);
    
    $range = $prod[$count - 1] - $prod[0];
    
    $sum = array_sum($prod);
    $average = $sum / $count;
    
    if ($count % 2 === 1) {
        $median = $prod[($count - 1) / 2];
    } else {
        $median = ($prod[$count / 2 - 1] + $prod[$count / 2]) / 2;
    }
    
    return sprintf("Range: %d Average: %.2f Median: %.2f", $range, $average, $median);
}

// original kata: https://www.codewars.com/kata/55cf3b567fc0e02b0b00000b
// my solution: https://www.codewars.com/kata/reviews/57ab4648fefb4eb7e50000c7/groups/6996cc6623a33fd213f7dac3
