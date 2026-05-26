using System.Linq;

namespace Solution
{
  class Digitizer
  {
    public static long[] Digitize(long n) => n.ToString().Select(c => (long)(c - '0')).Reverse().ToArray();
  }
}

// original kata: https://www.codewars.com/kata/5583090cbe83f4fd8c000051
// my solution: https://www.codewars.com/kata/reviews/575b2b95b74dcc3c7f000007/groups/631907e55f59a40001efe11c
