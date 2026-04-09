<?php
  
function simplify(string $poly): string
{ 
    $tokens = [];
    preg_match_all('/[+-]?[^+-]+/', $poly, $matches);
    
    foreach ($matches[0] as $token) {
        $token = trim($token);
        if ($token === '') continue;
        
        if (preg_match('/^([+-]?\d*)([a-z].*)$/', $token, $m)) {
            $coef_str = $m[1];
            $vars_str = $m[2];
            
            if ($coef_str === '' || $coef_str === '+') $coef = 1;
            elseif ($coef_str === '-') $coef = -1;
            else $coef = (int)$coef_str;
            
            $vars = str_split($vars_str);
            sort($vars);
            $key = implode('', $vars);
            
            if (!isset($monomials[$key])) $monomials[$key] = 0;
            $monomials[$key] += $coef;
        }
    }
    
    $monomials = array_filter($monomials, fn($c) => $c !== 0);

    uksort($monomials, function($a, $b) {
        $lenA = strlen($a);
        $lenB = strlen($b);
        if ($lenA !== $lenB) return $lenA - $lenB;
        return strcmp($a, $b);
    });

    $result = '';
    foreach ($monomials as $vars => $coef) {
        if ($coef === 1) {
            $term = $vars;
        } elseif ($coef === -1) {
            $term = '-' . $vars;
        } else {
            $term = $coef . $vars;
        }
        
        if ($result === '') {
            $result = $term;
        } else {
            if ($coef > 0) {
                $result .= '+' . $term;
            } else {
                $result .= $term;
            }
        }
    }
    
    return $result;
}

// original kata: https://www.codewars.com/kata/55f89832ac9a66518f000118
// my solution: https://www.codewars.com/kata/reviews/5828464d20dd263d96000024/groups/69d769cc139f54ca1643895d
