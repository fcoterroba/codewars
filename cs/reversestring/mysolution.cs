using System;

public static class Kata
{
  public static string Solution(string str) 
  {
    char[] arr = str.ToCharArray();
    Array.Reverse(arr);
    return new string(arr);
  }
}

// original kata: https://www.codewars.com/kata/5168bb5dfe9a00b126000018
// my solution: https://www.codewars.com/kata/reviews/59ad726ac2479b7127000bcb/groups/59ae4caa9df6f56215000a80