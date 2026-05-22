def open_or_senior(data):
    return ["Senior" if age >= 55 and handicap > 7 else "Open" for age, handicap in data]

# original kata: https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa
# my solution: https://www.codewars.com/kata/reviews/5502c9e8b3216ec63c0001ac/groups/5ef025b98e66be00014c3413
