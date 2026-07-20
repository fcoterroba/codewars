export function sumTwoSmallestNumbers(numbers: Array<number>): number {
  const sorted = [...numbers].sort((a, b) => a - b);
  return sorted[0] + sorted[1];
}

// original kata: https://www.codewars.com/kata/558fc85d8fd1938afb000014
// my solution: https://www.codewars.com/kata/reviews/66a1183cd2306a7d179dda86/groups/66c3555b783763dad52ec3a1
