<?php

class CaesarCipher {
  private $shift;

  public function __construct($shift) {
    $this->shift = $shift % 26;
  }

  public function encode($str) {
    return $this->transform($str, $this->shift);
  }

  public function decode($str) {
    return $this->transform($str, -$this->shift);
  }

  private function transform($str, $shift) {
    $result = '';
    $str = strtoupper($str);

    foreach (str_split($str) as $char) {
      if (ctype_alpha($char)) {
        $charCode = ord($char) - ord('A');
        $newCharCode = ($charCode + $shift) % 26;
        if ($newCharCode < 0) {
          $newCharCode += 26;
        }
        $result .= chr($newCharCode + ord('A'));
      } else {
        $result .= $char;
      }
    }
    return $result;
  }
}

// original kata: https://www.codewars.com/kata/526d42b6526963598d0004db
// my solution: https://www.codewars.com/kata/reviews/57bb88bd7188e11b930001b2/groups/697b1b1c9bf880453ea06ac7