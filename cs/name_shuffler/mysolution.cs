using System;

public class Kata
{   
  public static string NameShuffler(string str)
  {
      string[] parts = str.Split(' ');
      return parts[1] + " " + parts[0];
  }
}

// original kata: https://www.codewars.com/kata/559ac78160f0be07c200005a
// my solution: https://www.codewars.com/kata/reviews/5991c1633c5b64d866000025/groups/5cad0fb5b447740001f2cbbd
