export function isIsogram(str: string): boolean {
  const lower = str.toLowerCase();
  return new Set(lower).size === lower.length;
}

// original kata: https://www.codewars.com/kata/54ba84be607a92aa900000f1
// my solution: https://www.codewars.com/kata/reviews/5e0176bf8c89df000187c43f/groups/683546a28c715773ce65a51d
