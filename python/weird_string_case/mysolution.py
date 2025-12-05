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
