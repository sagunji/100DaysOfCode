def rotLeft(a, d):
    rot = d % len(a)
    rotated = a[rot : len(a)] + a[0:rot]
    return rotated


rotLeft([1, 2, 3, 4, 5], 7)

