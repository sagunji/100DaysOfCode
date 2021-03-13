def jumpingOnClouds(c):
    n = len(c)
    # 2 jumps
    count = 0
    # 1 jumps
    i = 0
    while i < n - 1:
        if c[i] == "0":
            i += 1
        i += 1
        count += 1

    return count


jumpingOnClouds("0010010")

