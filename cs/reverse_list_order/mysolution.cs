using System.Collections.Generic;
using System.Linq;

public class Kata
{
  public static List<int> ReverseList(List<int> list)
  {
    return Enumerable.Reverse(list).ToList();
  }
}

// original kata: https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b
// my solution: https://www.codewars.com/kata/reviews/5991c1063c5b647f37000004/groups/5991ee59583995efe0000a0c