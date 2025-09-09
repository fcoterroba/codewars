using System.Linq;

public class Kata
{
    public static bool BetterThanAverage(int[] classPoints, int yourPoints)
    {
        double average = classPoints.Average();
        return yourPoints > average;
    }
}

// original kata: https://www.codewars.com/kata/5601409514fc93442500010b
// my solution: https://www.codewars.com/kata/reviews/56014404857a8977c40000ac/groups/68bfbef25ef31a970b44c706