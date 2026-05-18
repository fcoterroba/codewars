export function basicOp(operation: string, value1: number, value2: number): number {
  const ops: Record<string, (a: number, b: number) => number> = {
    '+': (a, b) => a + b,
    '-': (a, b) => a - b,
    '*': (a, b) => a * b,
    '/': (a, b) => a / b,
  };

  return ops[operation](value1, value2);
}

// original kata: https://www.codewars.com/kata/57356c55867b9b7a60000bd7
// my solution: https://www.codewars.com/kata/reviews/5abf329e9bbc420d7b0008d4/groups/68784fa0be94791af828920e
