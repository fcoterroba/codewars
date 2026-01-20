using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class ListFilterer
{
   public static IEnumerable<int> GetIntegersFromList(List<object> listOfItems)
   {
      return listOfItems.OfType<int>();
   }
}

// original kata: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
// my solution: https://www.codewars.com/kata/reviews/599559254779a5249700077a/groups/599d60af5c795f105a000e30