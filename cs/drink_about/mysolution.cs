public class Kata
{
  public static string PeopleWithAgeDrink(int old) =>
    old < 14 ? "drink toddy" :
    old < 18 ? "drink coke"  :
    old < 21 ? "drink beer"  :
               "drink whisky";
}

// original kata: https://www.codewars.com/kata/56170e844da7c6f647000063
// my solution: https://www.codewars.com/kata/reviews/599831c4ec08e20b4d00006e/groups/5abfd0c33f0cbf2da7001471
