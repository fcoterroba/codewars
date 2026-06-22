export function sumDigits(n: number): number {
  return Math.abs(n).toString().split('').reduce((sum, d) => sum + +d, 0);
}

// original kata: https://www.codewars.com/kata/52f3149496de55aded000410
// my solution: https://www.codewars.com/kata/reviews/5dff858388417400012c289a/groups/6a39121f7ba2b7d277fb4328
