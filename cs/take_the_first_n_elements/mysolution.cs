using System;
public static class Kata
{
    public static int[] Take(int[] arr, int n)
    {
        return arr[..Math.Min(n, arr.Length)];
    }
}

// original kata: https://www.codewars.com/kata/545afd0761aa4c3055001386
// my solution: https://www.codewars.com/kata/reviews/615700a77f9b160001c446bd/groups/615734c9de703d0001fbd466
