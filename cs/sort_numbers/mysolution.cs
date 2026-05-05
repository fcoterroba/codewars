using System;

public class Kata
{
  public static int[] SortNumbers(int[] nums)
  {
    if (nums == null || nums.Length == 0)
      return new int[0];

    Array.Sort(nums);
    return nums;
  }
}

// original kata: https://www.codewars.com/kata/5174a4c0f2769dd8b1000003
// my solution: https://www.codewars.com/kata/reviews/57b9e2ee5b446c654e0000f4/groups/57c00268b195053ace0001bb
