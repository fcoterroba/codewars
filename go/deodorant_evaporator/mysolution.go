package kata

import "math"

func Evaporator(content float64, evapPerDay int, threshold int) int {
    remaining := float64(threshold) / 100.0
    dailyFactor := 1.0 - float64(evapPerDay)/100.0
    return int(math.Ceil(math.Log(remaining) / math.Log(dailyFactor)))
}

// original kata: https://www.codewars.com/kata/5506b230a11c0aeab3000c1f
// my solution: https://www.codewars.com/kata/reviews/5c2785f44b1d7700017ea01c/groups/6a16a2bc409bb2220c5edb00
