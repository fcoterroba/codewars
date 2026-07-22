package kata

import "strings"

func VertMirror(s string) string {
    lines := strings.Split(s, "\n")
    for i, line := range lines {
        runes := []rune(line)
        for l, r := 0, len(runes)-1; l < r; l, r = l+1, r-1 {
            runes[l], runes[r] = runes[r], runes[l]
        }
        lines[i] = string(runes)
    }
    return strings.Join(lines, "\n")
}

func HorMirror(s string) string {
    lines := strings.Split(s, "\n")
    for l, r := 0, len(lines)-1; l < r; l, r = l+1, r-1 {
        lines[l], lines[r] = lines[r], lines[l]
    }
    return strings.Join(lines, "\n")
}

type FParam func(string) string

func Oper(f FParam, x string) string {
    return f(x)
}

// original kata: https://www.codewars.com/kata/56dbe0e313c2f63be4000b25
// my solution: https://www.codewars.com/kata/reviews/5c2f6918aa853b0001be9b19/groups/6a607b0133c019a2f0e25580
