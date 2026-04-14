public static class Kata
{
  public static string RemoveUrlAnchor(string url)
  {
      int i = url.IndexOf('#');
      return i >= 0 ? url[..i] : url;
  }
}

// original kata: https://www.codewars.com/kata/51f2b4448cadf20ed0000386
// my solution: https://www.codewars.com/kata/reviews/59bc2990134e4fb55b000e77/groups/69dde789e475b47695b6e378
