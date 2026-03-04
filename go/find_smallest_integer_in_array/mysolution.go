package kata

func SmallestIntegerFinder(numbers []int) int {
  min := numbers[0]
  for _,n := range numbers[1:] {
    if n < min {
      min = n
    }
  }
  return min
}

// original kata: https://www.codewars.com/kata/55a2d7ebe362935a210000b2
// my solution: https://www.codewars.com/kata/reviews/611acffa32d4430001834ca7/groups/611ad059d16a210001e1e9b7
