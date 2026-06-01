export function getSum(a: number, b: number): number {
  const min = Math.min(a, b);
  const max = Math.max(a, b);
  return (max - min + 1) * (min + max) / 2;
}

// original kata: https://www.codewars.com/kata/55f2b110f61eb01779000053
// my solution: https://www.codewars.com/kata/reviews/59b795c8677bf1eaa7001f14/groups/5e97d70ce8255200017b2ea4
