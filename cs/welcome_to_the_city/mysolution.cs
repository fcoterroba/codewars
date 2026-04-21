public class Kata
{
    public static string SayHello(string[] name, string city, string state)
    {
        return $"Hello, {string.Join(" ", name)}! Welcome to {city}, {state}!";
    }
}

// original kata: https://www.codewars.com/kata/5302d846be2a9189af0001e4
// my solution: https://www.codewars.com/kata/reviews/599c8dc5aa7911eb11002c58/groups/59b3dbec237fb378e900093f
