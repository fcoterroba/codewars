package kata

import "strings"

func DNAStrand(dna string) string {
    replacer := strings.NewReplacer("A", "T", "T", "A", "C", "G", "G", "C")
    return replacer.Replace(dna)
}

// original kata: https://www.codewars.com/kata/554e4a2f232cdd87d9000038
// my solution: https://www.codewars.com/kata/reviews/5bdf4214aa4b1fe36e000f12/groups/61f08c93c38b8a0001cab9f3
