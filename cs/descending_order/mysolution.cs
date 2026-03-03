using System;
using System.Linq;

public static class Kata
{
  public static int DescendingOrder(int num)
  {
    return int.Parse(string.Concat(num.ToString().OrderByDescending(c => c)));
  }
}

// original kata: https://www.codewars.com/kata/5467e4d82edf8bbf40000155
// my solution: https://www.codewars.com/kata/reviews/550b0be906815114a70017d2/groups/5571c4e6994ef9f22400006e
