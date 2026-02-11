package kata

func GetGrade(a, b, c int) rune {
	average := (a + b + c) / 3
	if average >= 90 {
		return 'A'
	} else if average >= 80 {
		return 'B'
	} else if average >= 70 {
		return 'C'
	} else if average >= 60 {
		return 'D'
	} else {
		return 'F'
	}
}

// original kata: https://www.codewars.com/kata/55cbd4ba903825f7970000f5
// my solution: https://www.codewars.com/kata/reviews/5d75672f1997750001e85f1f/groups/6057b343c0fd4c0001193fac
