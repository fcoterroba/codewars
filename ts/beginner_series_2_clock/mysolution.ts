export function past(h: number, m: number, s: number): number {
  return ((h * 60 + m) * 60 + s) * 1000;
}

// original kata: https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a
// my solution: https://www.codewars.com/kata/reviews/5e47a657ffda370001ee5995/groups/5e47a657ffda370001ee5999
