<?php

function justify($str, $len) {
    if (empty(trim($str))) return '';
    
    $words = preg_split('/\s+/', trim($str));
    $lines = [];
    $currentLine = [];
    $currentLen = 0;

    foreach ($words as $word) {
        $wordLen = strlen($word);
        $neededLen = $currentLen === 0 ? $wordLen : $currentLen + 1 + $wordLen;
        
        if ($neededLen <= $len) {
            $currentLine[] = $word;
            $currentLen = $neededLen;
        } else {
            if (!empty($currentLine)) $lines[] = $currentLine;
            $currentLine = [$word];
            $currentLen = $wordLen;
        }
    }
    if (!empty($currentLine)) $lines[] = $currentLine;
    
    $result = [];
    $lastIndex = count($lines) - 1;
    
    foreach ($lines as $i => $line) {
        $wordCount = count($line);

        if ($i === $lastIndex || $wordCount === 1) {
            $result[] = implode(' ', $line);
            continue;
        }
        
        $totalChars = array_sum(array_map('strlen', $line));
        $totalSpaces = $len - $totalChars;
        $gaps = $wordCount - 1;
        
        $baseSpace = intdiv($totalSpaces, $gaps);
        $extraSpaces = $totalSpaces % $gaps;
        
        $lineStr = '';
        for ($j = 0; $j < $wordCount; $j++) {
            $lineStr .= $line[$j];
            if ($j < $gaps) {
                $lineStr .= str_repeat(' ', $baseSpace + ($j < $extraSpaces ? 1 : 0));
            }
        }
        $result[] = $lineStr;
    }
    
    return implode("\n", $result);
}

// original kata: https://www.codewars.com/kata/537e18b6147aa838f600001b
// my solution: https://www.codewars.com/kata/reviews/597bffcba05707b8820000d0/groups/69c4f80553f32111077ceccb
