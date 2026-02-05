<?php

function rgb($r,$g,$b){
  $r = max(0, min(255, (int)$r));
  $g = max(0, min(255, (int)$g));
  $b = max(0, min(255, (int)$b));
  return strtoupper(str_pad(dechex($r), 2, '0', STR_PAD_LEFT).str_pad(dechex($g), 2, '0', STR_PAD_LEFT).str_pad(dechex($b), 2, '0', STR_PAD_LEFT));
}

// original kata: https://www.codewars.com/kata/513e08acc600c94f01000001
// my solution: https://www.codewars.com/kata/reviews/5cfdbc69a535d5000183e806/groups/6984400d13e1b430a9fa0d9d
