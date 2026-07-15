package kata

import (
	"crypto/md5"
	"encoding/hex"
)

func PassHash(str string) string {
	sum := md5.Sum([]byte(str))
	return hex.EncodeToString(sum[:])
}

// original kata: https://www.codewars.com/kata/54207f9677730acd490000d1
// my solution: https://www.codewars.com/kata/reviews/5d8a5a0e5052240001ab7947/groups/692056350a6fe6e5881c771c
