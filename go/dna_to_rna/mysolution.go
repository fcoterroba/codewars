package kata

import (
  "strings"
)

func DNAtoRNA(dna string) string {
  return strings.Replace(dna, "T", "U", -1)
}

// original kata: https://www.codewars.com/kata/5556282156230d0e5e000089
// my solution: https://www.codewars.com/kata/reviews/5c3b52bb38ed0c0001f43b2e/groups/5c3b52bd38ed0c0001f43b32
