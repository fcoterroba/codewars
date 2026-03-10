using System;
using System.Linq;

public static class Kata
{
  public static string ReverseWords(string str)
  {
    return string.Join(" ", str.Split(' ').Select(w => new string(w.Reverse().ToArray())));
  }
}

// original kata: https://www.codewars.com/kata/5259b20d6021e9e14c0010d4
// my solution: https://www.codewars.com/kata/reviews/5995dbaff017e425c400089f/groups/5ac633d65f6db4d11c002003
