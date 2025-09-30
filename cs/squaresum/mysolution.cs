public static class Kata
{
  public static int SquareSum(int[] numbers)
  {
      int sum = 0;
      foreach (int num in numbers)
      {
          sum += num * num;
      }
      return sum;
  }
}

// original kata: https://www.codewars.com/kata/515e271a311df0350d00000f
// my solution: https://www.codewars.com/kata/reviews/599189e5598b9eeb63000004/groups/5fea476429d10800018dc99d