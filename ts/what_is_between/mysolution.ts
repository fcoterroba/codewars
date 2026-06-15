export function between(a: number, b: number): number[] {
  return Array.from({ length: b - a + 1 }, (_, i) => a + i);
}

// original kata: https://www.codewars.com/kata/55ecd718f46fba02e5000029
// my solution: https://www.codewars.com/kata/reviews/61348fddea17950001869f0f/groups/61349445fdc3550001d4c373
