package kata

import (
	"strconv"
	"strings"
)

func HighAndLow(in string) string {
	fields := strings.Fields(in)

	high, _ := strconv.Atoi(fields[0])
	low := high

	for _, f := range fields[1:] {
		n, _ := strconv.Atoi(f)
		if n > high {
			high = n
		}
		if n < low {
			low = n
		}
	}

	return strconv.Itoa(high) + " " + strconv.Itoa(low)
}

// original kata: https://www.codewars.com/kata/554b4ac871d6813a03000035
// my solution: https://www.codewars.com/kata/reviews/5bd029a0abc6619b260001e2/groups/6ab3912a1b95cdef12584b76
