using System;

public class Kata
{
  public static long FindNextSquare(long num)
  {
    long sqrt = (long)Math.Sqrt(num);
    if (sqrt * sqrt != num) return -1;
    return (sqrt + 1) * (sqrt + 1);
  }
}

// original kata: https://www.codewars.com/kata/56269eb78ad2e4ced1000013
// my solution: https://www.codewars.com/kata/reviews/56b3b92231701df3eb000017/groups/5ac4772ad7d25faa77001e90
