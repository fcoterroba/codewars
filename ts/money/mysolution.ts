export function calculateYears(principal: number, interest: number, tax: number, desired: number): number {
    let years = 0;
    let current = principal;

    while (current < desired) {
        current += current * interest * (1 - tax);
        years++;
    }

    return years;
}

// original kata: https://www.codewars.com/kata/563f037412e5ada593000114
// my solution: https://www.codewars.com/kata/reviews/673083f030786694b28811c7/groups/69dcb78bd0151b4680a19c27
