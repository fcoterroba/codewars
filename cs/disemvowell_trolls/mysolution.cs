using System;

public static class Kata
{
    public static string Disemvowel(string str)
    {
        return str.Replace("a", "").Replace("e", "").Replace("i", "").Replace("o", "").Replace("u", "").Replace("A", "").Replace("E", "").Replace("I", "").Replace("O", "").Replace("U", "");
    }
}

// original kata: https://www.codewars.com/kata/52fba66badcd10859f00097e
// my solution: https://www.codewars.com/kata/reviews/550af1f4595138841700089f/groups/5511636cce486c123f000bbe