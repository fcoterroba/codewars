<?php

function same_structure_as(array $a, array $b): bool {
    if (count($a) !== count($b)) return false;
    
    foreach ($a as $i => $val) {
        $aIsArray = is_array($val);
        $bIsArray = is_array($b[$i]);
        
        if ($aIsArray !== $bIsArray) return false;
        if ($aIsArray && !same_structure_as($val, $b[$i])) return false;
    }
    
    return true;
}

// original kata: https://www.codewars.com/kata/520446778469526ec0000001
// my solution: https://www.codewars.com/kata/reviews/59c9e408e79537a29d0004e8/groups/6a0570f451bcfaa2e2053d22
