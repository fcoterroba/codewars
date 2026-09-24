<?php

class RomanNumerals {
  private static array $romanMap = [
    'M'  => 1000,
    'CM' => 900,
    'D'  => 500,
    'CD' => 400,
    'C'  => 100,
    'XC' => 90,
    'L'  => 50,
    'XL' => 40,
    'X'  => 10,
    'IX' => 9,
    'V'  => 5,
    'IV' => 4,
    'I'  => 1,
  ];

  public static function toRoman(int $num): string {
    $roman = '';
    
    foreach (self::$romanMap as $symbol => $value) {
      while ($num >= $value) {
        $roman .= $symbol;
        $num -= $value;
      }
    }
    
    return $roman;
  }

  public static function fromRoman(string $str): int {
    $num = 0;
    $i = 0;
    $len = strlen($str);
    
    while ($i < $len) {
      if ($i + 1 < $len) {
        $twoChar = substr($str, $i, 2);
        if (isset(self::$romanMap[$twoChar])) {
          $num += self::$romanMap[$twoChar];
          $i += 2;
          continue;
        }
      }

      $oneChar = $str[$i];
      if (isset(self::$romanMap[$oneChar])) {
        $num += self::$romanMap[$oneChar];
      }
      $i++;
    }
    
    return $num;
  }
}

// original kata: https://www.codewars.com/kata/51b66044bce5799a7f000003
// my solution: https://www.codewars.com/kata/reviews/6ab2a8467624f70319c58395/groups/6ab4ebcddfe587b9f184dd5a
