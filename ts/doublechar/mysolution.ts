export function doubleChar(str: string): string {
  return str
    .split("")
    .map((char) => char + char)
    .join("");
}

// original kata: https://www.codewars.com/kata/56b1f01c247c01db92000076
// my solution: https://www.codewars.com/kata/reviews/616db73b9dac820001805a14/groups/625ceac1687ab10001de4469