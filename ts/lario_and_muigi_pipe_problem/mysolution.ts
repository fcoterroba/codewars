export function pipeFix(numbers: number[]): number[] {
  const min = numbers[0];
  const max = numbers[numbers.length - 1];
  return Array.from({ length: max - min + 1 }, (_, i) => min + i);
}

// original kata: https://www.codewars.com/kata/56b29582461215098d00000f
// my solution: https://www.codewars.com/kata/reviews/64908126adeebf0001a0c7e0/groups/64b521d30fbb190001baaee0
