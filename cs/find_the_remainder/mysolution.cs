using System;

public class Kata
{
  public static int Remainder(int a, int b)
  {
    int mayor = Math.Max(a, b);
    int menor = Math.Min(a, b);

    if (menor == 0)
      throw new DivideByZeroException();

    return mayor % menor;
  }
}

// original kata: https://www.codewars.com/kata/524f5125ad9c12894e00003f
// my solution: https://www.codewars.com/kata/reviews/59af4e4bc311399190000a1f/groups/6ab24fcec800086259846903
