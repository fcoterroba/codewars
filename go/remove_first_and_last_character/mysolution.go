package kata

func RemoveChar(word string) string {
    if len(word) <= 2 {
        return ""
    }
    return word[1 : len(word)-1]
}

// original kata: https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0
// my solution: https://www.codewars.com/kata/reviews/5ac003d820d0515fae00112c/groups/5b534b90f4046b2609000f8a
