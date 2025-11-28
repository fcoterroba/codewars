def solution(roman: str) -> int:
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(len(roman)):
        if i + 1 < len(roman) and roman_dict[roman[i]] < roman_dict[roman[i + 1]]:
            result -= roman_dict[roman[i]]
        else:
            result += roman_dict[roman[i]]
    return result


# original kata: https://www.codewars.com/kata/51b62bf6a9c58071c600001bhttps://www.codewars.com/kata/51b6249c4612257ac0000005
# my solution: https://www.codewars.com/kata/reviews/54589d1e36f34f3045000003/groups/6929817c34a5e4b8979006aa
