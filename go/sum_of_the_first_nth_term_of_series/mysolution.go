package kata

import "fmt"

func SeriesSum(n int) string {
	sum := 0.0
	for i := 0; i < n; i++ {
		sum += 1.0 / float64(1+3*i)
	}
	return fmt.Sprintf("%.2f", sum)
}

// original kata: https://www.codewars.com/kata/555eded1ad94b00403000071
// my solution: https://www.codewars.com/kata/reviews/65fab74ffe624f00018f3284/groups/672e68c001b33bfb9159b506
