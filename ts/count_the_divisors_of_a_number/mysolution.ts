export function divisors(n: number): number {
  let count = 0;
  for (let i = 1; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      count += i === n / i ? 1 : 2;
    }
  }
  return count;
}

// original kata: https://www.codewars.com/kata/542c0f198e077084c0000c2e
// my solution: https://www.codewars.com/kata/reviews/5e26feeed020f10001338c58/groups/67bf0443c36e58d08d36589c
