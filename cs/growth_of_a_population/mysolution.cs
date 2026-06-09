using System;

class Arge {
    
    public static int NbYear(int p0, double percent, int aug, int p) {
      int years = 0;
      while (p0 < p) {
          p0 = (int)(p0 + p0 * percent / 100 + aug);
          years++;
      }
      return years;
  }
}

// original kata: https://www.codewars.com/kata/563b662a59afc2b5120000c6
// my solution: https://www.codewars.com/kata/reviews/563b6d19c411980ae20000f8/groups/61d51644aa01b700014a31a8
