using System;
public static class JadenCase
{
  public static string ToJadenCase(this string phrase)
  {
    return System.Globalization.CultureInfo.CurrentCulture.TextInfo.ToTitleCase(phrase.ToLower());;
  }
}

// original kata: https://www.codewars.com/kata/5390bac347d09b7da40006f6
// my solution: https://www.codewars.com/kata/reviews/57cc54cda362c1394e00004e/groups/58458a301019285e1100004b