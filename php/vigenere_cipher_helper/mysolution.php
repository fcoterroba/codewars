<?php

class VigenèreCipher {
    private $key;
    private $alphabet;

    public function __construct($key, $alphabet) {
        $this->key      = $key;
        $this->alphabet = $alphabet;
    }

    public function encode($s) {
        return $this->process($s, true);
    }

    public function decode($s) {
        return $this->process($s, false);
    }

    private function process($s, $encode) {
        $result  = '';
        $len     = mb_strlen($s);
        $keyLen  = mb_strlen($this->key);
        $alphaLen = mb_strlen($this->alphabet);

        for ($i = 0; $i < $len; $i++) {
            $char     = mb_substr($s, $i, 1);
            $pos      = mb_strpos($this->alphabet, $char);

            if ($pos === false) {
                $result .= $char;
                continue;
            }

            $keyChar  = mb_substr($this->key, $i % $keyLen, 1);
            $shift    = mb_strpos($this->alphabet, $keyChar);

            if ($encode) {
                $newPos = ($pos + $shift) % $alphaLen;
            } else {
                $newPos = (($pos - $shift) % $alphaLen + $alphaLen) % $alphaLen;
            }

            $result .= mb_substr($this->alphabet, $newPos, 1);
        }

        return $result;
    }
}

// original kata: https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3
// my solution: https://www.codewars.com/kata/reviews/57bfc21c939079b2b4000020/groups/69f301d50e953f66a918e248
