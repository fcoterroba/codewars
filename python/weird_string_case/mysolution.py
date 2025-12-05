def to_weird_case(words):
    result = []
    for word in words.split():
        new_word = ""
        for i, char in enumerate(word):
            if i % 2 == 0:
                new_word += char.upper()
            else:
                new_word += char.lower()
        result.append(new_word)
    return " ".join(result)

# original kata: https://www.codewars.com/kata/52b757663a95b11b3d00062d
# my solution: https://www.codewars.com/kata/reviews/5589f7d194c148aae600001e/groups/663b3d1c15dd1d00014b41ec
