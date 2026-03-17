using System;
using System.Linq;

public static class Kata
{
  public static int[] Capitals(string word)
  {
      return word.Select((c, i) => (c, i)).Where(x => char.IsUpper(x.c)).Select(x => x.i).ToArray();
  }
}

// original kata: https://www.codewars.com/kata/539ee3b6757843632d00026b
// my solution: https://www.codewars.com/kata/reviews/552d2c7499020706f7000190/groups/69b90becd4463dadf4111c0c
