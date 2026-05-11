export function areYouPlayingBanjo(name: string): string {
  return name[0].toLowerCase() === "r"
    ? `${name} plays banjo`
    : `${name} does not play banjo`
}

// original kata: https://www.codewars.com/kata/53af2b8861023f1d88000832
// my solution: https://www.codewars.com/kata/reviews/616c40f74c598600017cefe7/groups/617c0d3070df420001ec200c
