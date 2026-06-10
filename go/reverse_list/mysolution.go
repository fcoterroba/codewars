package kata

func ReverseList(lst []int) []int {
    for i, j := 0, len(lst)-1; i < j; i, j = i+1, j-1 {
        lst[i], lst[j] = lst[j], lst[i]
    }
    return lst
}

// original kata: https://www.codewars.com/kata/57a04da9e298a7ee43000111
// my solution: https://www.codewars.com/kata/reviews/62dc2d0c92f0ac00019029c7/groups/62dc78a1cc3dce00014bc307
