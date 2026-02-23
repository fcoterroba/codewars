export function addBinary(a: number, b: number): string {
  return (BigInt(a) + BigInt(b)).toString(2);
}

// original kata: https://www.codewars.com/kata/551f37452ff852b7bd000139
// my solution: https://www.codewars.com/kata/reviews/66a12981b8977d2f42edf7e5/groups/67f0362c6776460300554b56
