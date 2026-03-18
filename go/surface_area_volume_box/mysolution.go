package kata

func GetSize(w, h, d int) [2]int {
    surface := 2 * (w*h + h*d + w*d)
    volume  := w * h * d
    return [2]int{surface, volume}
}

// original kata: https://www.codewars.com/kata/565f5825379664a26b00007c
// my solution: https://www.codewars.com/kata/reviews/5dabca081944dd00016fbe1f/groups/63dffab026e4310001b02d7e
