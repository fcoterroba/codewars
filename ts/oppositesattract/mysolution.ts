export function lovefunc(flower1: number, flower2: number): boolean {
    return (flower1 % 2 === 0 && flower2 % 2 !== 0) || (flower1 % 2 !== 0 && flower2 % 2 === 0);
}

// original kata: https://www.codewars.com/kata/555086d53eac039a2a000083/train/typescript
// my solution: https://www.codewars.com/kata/reviews/6134891f2eec6d0001fd8e86/groups/61386f9406206d0001df49c5