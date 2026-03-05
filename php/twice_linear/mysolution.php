<?php

function dblLinear(int $n): int
{
    $u = [1];
    $i2 = 0;
    $i3 = 0;

    for ($k = 0; $k < $n; $k++) {
        $y = 2 * $u[$i2] + 1;
        $z = 3 * $u[$i3] + 1;

        if ($y < $z) {
          $u[] = $y; $i2++;
        } elseif ($y > $z) {
          $u[] = $z; $i3++; 
        } else {
          $u[] = $y; $i2++; $i3++; 
        }
    }

    return end($u);
}

//original kata: https://www.codewars.com/kata/5672682212c8ecf83e000050
// my solution: https://www.codewars.com/kata/reviews/5798bc8d964d77282d000037/groups/69a9486158521efd8c193c9e
