package kata

func GetCount(str string) (count int) {
	for _, c := range str {
		switch c {
		case 'a', 'e', 'i', 'o', 'u':
			count++
		}
	}
	return count
}

// original kata: https://www.codewars.com/kata/54ff3102c1bad923760001f3
// my solution: https://www.codewars.com/kata/reviews/5bd0d703dfa73b037c000610/groups/5bd0d752abc66115eb002188
