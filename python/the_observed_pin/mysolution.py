def get_pins(observed):
    adjacent = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['2', '1', '3', '5'],
        '3': ['3', '2', '6'],
        '4': ['4', '1', '5', '7'],
        '5': ['5', '2', '4', '6', '8'],
        '6': ['6', '3', '5', '9'],
        '7': ['7', '4', '8'],
        '8': ['8', '5', '7', '9', '0'],
        '9': ['9', '6', '8']
    }
    
    if not observed:
        return ['']
    
    result = []
    first_digit = observed[0]
    first_variations = adjacent[first_digit]
    
    rest_variations = get_pins(observed[1:])
    
    for digit in first_variations:
        for rest in rest_variations:
            result.append(digit + rest)
    
    return result

# original kata: https://www.codewars.com/kata/5263c6999e0f40dee200059d
# my solution: https://www.codewars.com/kata/reviews/5490a78cefb597b0a100019d/groups/698f1e720bc9799996c1a836