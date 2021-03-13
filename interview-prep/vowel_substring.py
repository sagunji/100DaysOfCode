def numberOfVowels(value):
    count = sum(map(value.count, ["a", "e", "i", "o", "u"]))

    vowelMap = {"s": value, "c": count}
    return vowelMap


def findSubstring(s, k):
    maxValue = {"s": "", "c": 0}

    for i in range(0, (len(s) - k)):
        sub = s[i : i + k]
        detail = numberOfVowels(sub)
        if detail["c"] > maxValue["c"]:
            maxValue = detail

    if maxValue["s"] == "":
        return "Not found!"

    return maxValue["s"]


print(findSubstring("caberqiitefeg", 6))

