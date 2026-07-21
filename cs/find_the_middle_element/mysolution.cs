public class Kata
{
  public static int Gimme(double[] inputArray)
  {
    for (int i = 0; i < 3; i++)
    {
      double a = inputArray[i];
      double b = inputArray[(i + 1) % 3];
      double c = inputArray[(i + 2) % 3];

      if ((a > b && a < c) || (a < b && a > c))
        return i;
    }

    throw new System.ArgumentException("No middle element found");
  }
}

// original kata: https://www.codewars.com/kata/545a4c5a61aa4c6916000755
// my solution: https://www.codewars.com/kata/reviews/5990b3db35fd2f1876000061/groups/6a5f1ead5456639bbe45bb7e
