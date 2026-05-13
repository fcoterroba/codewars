package kata

func Number(busStops [][2]int) int {
    people := 0
    for _, stop := range busStops {
        people += stop[0] - stop[1]
    }
    return people
}

// original kata: https://www.codewars.com/kata/5648b12ce68d9daa6b000099
// my solution: https://www.codewars.com/kata/reviews/62bc021eafd1270001ede104/groups/639a4f08b997ee0001e99324
