export const longest = (s1: string, s2: string): string => {
  const combined = s1 + s2;
  const uniqueChars = [...new Set(combined)];
  return uniqueChars.sort().join('');
}

// original kata: https://www.codewars.com/kata/5656b6906de340bd1b0000ac
// my solution: https://www.codewars.com/kata/reviews/587e433667ec24b86c001445/groups/6989b42e5d8fb92decca28ab