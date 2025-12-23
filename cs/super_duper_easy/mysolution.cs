using System;

public static class Kata
{
  public static string Problem(string a)
  {
    double result;
    if (!Double.TryParse(a, out result))
    {
      return "Error";
    }
    return (result * 50.0 + 6.0).ToString("0.00");
  }
}

// original kata: https://www.codewars.com/kata/55a5bfaa756cfede78000026
// my solution: https://www.codewars.com/kata/reviews/565f404cb8893327120000b0/groups/694a50ccbeddf043d6cba6fd