using System;
using System.Linq;

public static class Kata
{
  public static int CountSheeps(bool[] sheeps)
  {
    return sheeps.Count(c => c);
  }
}

// original kata: https://www.codewars.com/kata/54edbc7200b811e956000556
// my solution: https://www.codewars.com/kata/reviews/550afbfa595138b5d1000a00/groups/5510042f490732b770000910