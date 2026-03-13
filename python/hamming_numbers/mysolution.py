def hamming(n):
    h = [1] * n
    i2 = i3 = i5 = 0

    for i in range(1, n):
        next2 = h[i2] * 2
        next3 = h[i3] * 3
        next5 = h[i5] * 5

        h[i] = min(next2, next3, next5)

        if h[i] == next2: i2 += 1
        if h[i] == next3: i3 += 1
        if h[i] == next5: i5 += 1

    return h[n - 1]

# original kata: https://www.codewars.com/kata/526d84b98f428f14a60008da
# my solution: https://www.codewars.com/kata/reviews/53d0337689316446e6000035/groups/69b3cdfee38a6575b07fc984
