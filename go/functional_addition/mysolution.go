package kata

func Add(n int) func(int) int {
    return func(x int) int {
        return x + n
    }
}

// original kata: https://www.codewars.com/kata/538835ae443aae6e03000547
// my solution: https://www.codewars.com/kata/reviews/5cb0d5a4a87081000150db04/groups/5cb191520839f30001b5b8cc
