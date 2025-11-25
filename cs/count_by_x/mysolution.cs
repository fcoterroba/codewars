using System;
using System.Linq;

public static class Kata
{
    public static int[] CountBy(int x, int n) =>
        Enumerable.Range(1, n)
                  .Select(i => i * x)
                  .ToArray();
}

// original kata: https://www.codewars.com/kata/5513795bd3fafb56c200049e
// my solution: https://www.codewars.com/kata/reviews/575dc7fe8d77362a3d00006a/groups/587dbf0d9c119230d9001123