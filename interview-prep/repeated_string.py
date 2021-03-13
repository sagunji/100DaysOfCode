def repeatedString(s, n):
    slen = len(s)
    fRepeat = int(n / slen)
    remRepeat = n % slen
    subOfS = s[0:remRepeat]

    aCounter = 0

    for c in s:
        if c == "a":
            aCounter = aCounter + 1

    totalAs = aCounter * fRepeat

    for sub in subOfS:
        if sub == "a":
            totalAs = totalAs + 1

    return totalAs

