using System;

public static class Kata{
    public static int summation(int num){
        int result = 0;
        for (int i = 1; i <= num; i++){
            result += i;
        }
      return result;
    }

    public static void Main(string[] args){
        System.Console.WriteLine(summation(8));
    }
}

// Original kata: https://www.codewars.com/kata/55d24f55d7dd296eb9000030
// My solution: https://www.codewars.com/kata/reviews/57bb7fd77188e1cdfe0000eb/groups/57ccbca058da9eba3800284a