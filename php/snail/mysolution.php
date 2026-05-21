<?php

function snail(array $array): array {
    if (empty($array) || empty($array[0])) return [];
    
    $result = [];
    
    while (!empty($array)) {
        $result = array_merge($result, array_shift($array));

        foreach ($array as &$row) {
            if (!empty($row)) $result[] = array_pop($row);
        }

        if (!empty($array)) {
            $result = array_merge($result, array_reverse(array_pop($array)));
        }

        foreach (array_reverse($array) as $key => $row) {
            if (!empty($array[$key])) $result[] = array_shift($array[count($array) - 1 - $key]);
        }
    }
    
    return $result;
}

// original kata: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
// my solution: https://www.codewars.com/kata/reviews/59c6404b8d0bd6f95e000b7a/groups/6a0eb2550ee4022c28f86ff6
